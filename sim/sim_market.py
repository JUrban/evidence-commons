"""
Simulation of the truth-market layer (toy model, transparent assumptions).

Claims: N claims, each with a latent replication probability q ~ Beta(a,b) with mean ~0.55
        (in line with observed replication rates), realized truth y ~ Bernoulli(q),
        reliance weight w ~ Pareto (heavy tail), and a 'citation' proxy that is weakly
        informative about both q and w.
Traders: T traders with skill s_i in [0,1]. Each trader who looks at a claim observes
        signal = q + noise, noise sd = sigma_hi*(1-s_i) + sigma_lo*s_i.
        Traders look at claims with probability increasing in reliance (attention follows w).
        Each trader trades against an LMSR market maker toward its posterior belief,
        subject to a per-trader position limit (fraction of b).
Market: LMSR with liquidity b; price p = e^{q/b}/(1+e^{q/b}); resolution fee on notional.
Resolution allocation: choose K claims to resolve by (a) random, (b) open interest, (c) V=w*p(1-p).
Outcome metrics: Brier of final prices vs baseline; reliance-weighted uncertainty captured;
        expected loss avoided; ledger separation; manipulation resistance.
"""
import numpy as np, json, os
os.makedirs('figures', exist_ok=True); os.makedirs('results', exist_ok=True)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)

# ---------------- parameters ----------------
N = 5000          # claims
T = 200           # active forecasters (the decision-market study had 162)
b = 300.0         # LMSR liquidity
K = 150           # resolutions affordable
limit_frac = 0.5  # position limit as multiple of b (max single-principal move ~0.50->0.62)
trade_cap = 0.3   # per-trade cap as multiple of b
fee = 0.005       # resolution fee on notional
rounds = 3        # trading passes (traders revisit)

# ---------------- claims ----------------
q = rng.beta(2.2, 1.8, N)                      # mean ~0.55
y = (rng.random(N) < q).astype(int)            # realized truth
w = (rng.pareto(1.2, N) + 1.0)                 # reliance weight, heavy tail
w = w / w.mean()
cit = 0.3*np.log(w) + 0.6*(q-0.5) + rng.normal(0, 0.8, N)   # weak proxy

# ---------------- traders ----------------
skill = rng.beta(2, 5, T)                      # most traders modest, some skilled
sig_hi, sig_lo = 0.35, 0.05
noise_sd = sig_hi*(1-skill) + sig_lo*skill

def lmsr_price(qty):
    return 1.0/(1.0+np.exp(-qty/b))

def run_market(manip=None, limits=True, seed=11, record=None):
    """Returns final prices, open interest, per-trader positions, cash, and manipulation shifts."""
    r_ = np.random.default_rng(seed)
    qty = np.zeros(N)                # net contracts sold by maker
    pos = np.zeros((T, N))           # trader positions (+ long yes, - short)
    cash = np.zeros(T)
    # attention: probability a trader looks at a claim rises with reliance; most claims get few looks
    look_p = np.clip(0.0045*(w**1.3), 0.0005, 0.6)
    shifts = {}
    for r in range(rounds):
        order = r_.permutation(T)
        for i in order:
            looks = r_.random(N) < look_p
            idx = np.where(looks)[0]
            if idx.size == 0: continue
            belief = np.clip(q[idx] + r_.normal(0, noise_sd[i], idx.size), 0.02, 0.98)
            if record is not None:
                for j,bl in zip(idx,belief): record.append((i,j,bl))
            # trade partially toward belief: aggressiveness rises with skill; per-trade cap
            target_qty = b*np.log(belief/(1-belief))
            alpha = 0.15 + 0.5*skill[i]
            delta = np.clip(alpha*(target_qty - qty[idx]), -trade_cap*b, trade_cap*b)
            if limits:
                new_pos = np.clip(pos[i, idx] + delta, -limit_frac*b, limit_frac*b)
                delta = new_pos - pos[i, idx]
            # cost via LMSR cost function C(q)=b*ln(1+e^{q/b})
            q0 = qty[idx]; q1 = q0 + delta
            cost = b*(np.logaddexp(0, q1/b) - np.logaddexp(0, q0/b))
            cash[i] -= cost.sum()
            pos[i, idx] += delta
            qty[idx] = q1
        if manip is not None and r == 0:
            # after round 1, a manipulator pushes selected claims toward 0.85 with a large budget
            midx = manip
            before = lmsr_price(qty[midx]).copy()
            for j in midx:
                target = b*np.log(0.85/0.15)
                delta = target - qty[j]
                if limits:
                    delta = np.clip(delta, -limit_frac*b, limit_frac*b)
                qty[j] += delta
            shifts['immediate'] = float(np.mean(lmsr_price(qty[midx]) - before))
    price = lmsr_price(qty)
    open_interest = np.abs(pos).sum(axis=0)   # contracts outstanding
    if manip is not None:
        shifts['final_vs_clean'] = None
    return price, open_interest, pos, cash, shifts

rec=[]
price, oi, pos, cash, _ = run_market(record=rec)
rec=np.array(rec)

# ---------------- pricing accuracy ----------------
def brier(p, y): return np.mean((p-y)**2)
priced = oi > 0
brier_market = brier(price[priced], y[priced])
# baseline: logistic fit of citation proxy to truth (in-sample, generous to baseline)
from numpy.linalg import lstsq
X = np.column_stack([np.ones(N), cit])
# simple logistic via Newton
beta = np.zeros(2)
for _ in range(25):
    z = X@beta; pr = 1/(1+np.exp(-z))
    W = pr*(1-pr)
    grad = X.T@(y-pr); H = -(X*W[:,None]).T@X
    beta = beta - np.linalg.solve(H, grad)
p_cit = 1/(1+np.exp(-(X@beta)))
brier_cit = brier(p_cit[priced], y[priced])
brier_base = brier(np.full(priced.sum(), y[priced].mean()), y[priced])
brier_truthq = brier(q[priced], y[priced])   # best possible given latent q

# ---------------- resolution allocation ----------------
V = w*price*(1-price)
def captured(sel):
    U = w*q*(1-q)            # true reliance-weighted uncertainty
    return U[sel].sum()/U.sum()
def loss_avoided(sel):
    # a reliant party acts on claim if price>0.5; loss = w if it acts on a false claim
    # or fails to act on a true one; resolution removes that loss for selected claims
    acts = price > 0.5
    loss = w*((acts & (y==0)) | (~acts & (y==1)))
    return loss[sel].sum()/loss.sum()
sel_rand = rng.choice(N, K, replace=False)
sel_oi = np.argsort(-oi)[:K]
sel_V = np.argsort(-V)[:K]
sel_cit = np.argsort(-cit)[:K]
alloc = {k:(captured(s), loss_avoided(s)) for k,s in
         [("random",sel_rand),("citations",sel_cit),("open interest",sel_oi),("V = w·p(1−p)",sel_V)]}

# ---------------- ledger separation ----------------
# each recorded trade carries the trader's explicit belief; score with Brier on resolved claims
h = rng.random(N) < 0.5
def trader_brier(mask):
    out = np.full(T, np.nan)
    ti = rec[:,0].astype(int); cj = rec[:,1].astype(int); bl = rec[:,2]
    for i in range(T):
        m = (ti==i) & mask[cj]
        if m.sum() < 8: continue
        out[i] = np.mean((bl[m] - y[cj[m]])**2)
    return out
b1 = trader_brier(h); b2 = trader_brier(~h)
payoff = pos*y[None,:]; pnl = cash + payoff.sum(axis=1)
ok = ~np.isnan(b1) & ~np.isnan(b2)
from scipy.stats import spearmanr
rho_halves = spearmanr(b1[ok], b2[ok]).correlation
rho_skill = spearmanr(-skill[ok], b1[ok]).correlation

# ---------------- manipulation ----------------
midx = rng.choice(np.where(oi>50)[0], 50, replace=False)   # liquid claims
p_nolim, oi_nl, _, _, sh_nl = run_market(manip=midx, limits=False, seed=11)
p_lim, oi_l, _, _, sh_l = run_market(manip=midx, limits=True, seed=11)
p_clean, _, _, _, _ = run_market(seed=11)
manip_shift_nolim = float(np.mean(p_nolim[midx]-p_clean[midx]))
manip_shift_lim = float(np.mean(p_lim[midx]-p_clean[midx]))
imm_nolim = sh_nl['immediate']; imm_lim = sh_l['immediate']
# residual error on manipulated claims vs clean
err_nolim = np.mean(np.abs(p_nolim[midx]-q[midx])); err_lim = np.mean(np.abs(p_lim[midx]-q[midx])); err_clean=np.mean(np.abs(p_clean[midx]-q[midx]))

# ---------------- bond pool ----------------
# hosts bond 800 claims: 400 chosen among high-reliance (contested), 400 trivially-true low-reliance
hi = np.argsort(-w)[:2000]; lo = np.argsort(w)[:2000]
bonded_hi = rng.choice(hi, 400, replace=False); bonded_lo = rng.choice(lo, 400, replace=False)
bond = 1500.0
forf_hi = (y[bonded_hi]==0).sum()*bond; forf_lo=(y[bonded_lo]==0).sum()*bond
pool = forf_hi+forf_lo
surv_hi = bonded_hi[y[bonded_hi]==1]; surv_lo = bonded_lo[y[bonded_lo]==1]
weights = np.concatenate([oi[surv_hi], oi[surv_lo]])
prem = pool*weights/weights.sum() if weights.sum()>0 else weights*0
prem_hi = prem[:surv_hi.size].mean() if surv_hi.size else 0; prem_lo = prem[surv_hi.size:].mean() if surv_lo.size else 0

# ---------------- coverage ----------------
share_priced = priced.mean(); share_liquid = (oi > 50).mean()
trades_per_trader = len(rec)/T
rho_pnl_skill = spearmanr(skill, pnl).correlation

results = dict(N=N,T=T,b=b,K=K,
  brier_market=round(brier_market,4), brier_citation=round(brier_cit,4), brier_base=round(brier_base,4), brier_oracle=round(brier_truthq,4),
  share_priced=round(share_priced,3), share_liquid=round(share_liquid,3), trades_per_trader=round(trades_per_trader,1),
  alloc={k:(round(a,3),round(l,3)) for k,(a,l) in alloc.items()},
  rho_halves=round(rho_halves,3), rho_skill=round(rho_skill,3), rho_pnl_skill=round(rho_pnl_skill,3),
  manip_immediate_nolim=round(imm_nolim,3), manip_immediate_lim=round(imm_lim,3),
  manip_final_nolim=round(manip_shift_nolim,3), manip_final_lim=round(manip_shift_lim,3),
  err_clean=round(err_clean,3), err_nolim=round(err_nolim,3), err_lim=round(err_lim,3),
  bond_pool=round(pool), premium_contested=round(prem_hi), premium_trivial=round(prem_lo),
  forfeited_hi=int((y[bonded_hi]==0).sum()), forfeited_lo=int((y[bonded_lo]==0).sum()))
print(json.dumps(results, indent=1))
json.dump(results, open('results/sim_results.json','w'), indent=1)

# ---------------- figures ----------------
plt.rcParams.update({'font.size':9, 'font.family':'DejaVu Sans'})
# Fig 1 calibration
fig,ax=plt.subplots(figsize=(5,3.4))
bins=np.linspace(0,1,11); idx=np.digitize(price[priced],bins)-1
xs=[];ys=[];ns=[]
for k in range(10):
    m=idx==k
    if m.sum()>20: xs.append(price[priced][m].mean()); ys.append(y[priced][m].mean()); ns.append(m.sum())
ax.plot([0,1],[0,1],'--',color='gray',lw=1,label='perfect calibration')
ax.scatter(xs,ys,s=[n/8 for n in ns],color='#1f4e79',label='market price bins (size ∝ n)')
ax.set_xlabel('final market price'); ax.set_ylabel('fraction that replicated'); ax.set_title('Calibration of simulated market prices')
ax.legend(loc='upper left',frameon=False); ax.set_xlim(0,1); ax.set_ylim(0,1)
plt.tight_layout(); plt.savefig('figures/sim_calibration.png',dpi=160); plt.close()

# Fig 2 allocation
fig,ax=plt.subplots(figsize=(5,3.2))
names=list(alloc.keys()); capt=[alloc[k][0]*100 for k in names]; loss=[alloc[k][1]*100 for k in names]
x=np.arange(len(names)); ax.bar(x-0.18,capt,0.36,color='#1f4e79',label='reliance-weighted uncertainty captured (%)')
ax.bar(x+0.18,loss,0.36,color='#c0504d',label='reliance-weighted loss avoided (%)')
ax.set_xticks(x); ax.set_xticklabels(names); ax.set_title(f'Selecting {K} of {N} claims to resolve: four rules')
ax.set_ylim(0,72); ax.legend(loc='upper left',frameon=False,fontsize=7.5); ax.set_ylabel('% of total')
plt.tight_layout(); plt.savefig('figures/sim_allocation.png',dpi=160); plt.close()

# Fig 3 ledger separation
fig,ax=plt.subplots(figsize=(5,3.4))
ax.scatter(b1[ok],b2[ok],s=8,alpha=0.5,color='#1f4e79')
ax.set_xlabel('trader Brier score, first half of claims'); ax.set_ylabel('trader Brier score, second half')
ax.set_title(f'Ledger separation: rank correlation ρ = {rho_halves:.2f}')
plt.tight_layout(); plt.savefig('figures/sim_ledger.png',dpi=160); plt.close()

# Fig 4 manipulation
fig,ax=plt.subplots(figsize=(5,3.2))
labels=['immediate shift,\nno limits','immediate shift,\nposition limits','final shift,\nno limits','final shift,\nposition limits']
vals=[imm_nolim,imm_lim,manip_shift_nolim,manip_shift_lim]
ax.bar(labels,vals,color=['#c0504d','#9bbb59','#c0504d','#9bbb59']); ax.set_ylabel('mean price shift on 50 targeted claims')
ax.axhline(0,color='gray',lw=0.8); ax.set_title('One deep-pocketed principal pushes 50 liquid claims toward 0.85')
plt.tight_layout(); plt.savefig('figures/sim_manipulation.png',dpi=160); plt.close()
print("figures written")

# ---------------- ledger reliability vs positions ----------------
def ledger_curve(rounds_list):
    out=[]
    global rounds
    saved=rounds
    for R in rounds_list:
        rounds=R
        rec2=[]; p2,oi2,pos2,cash2,_=run_market(seed=23, record=rec2); rec2=np.array(rec2)
        h2=np.random.default_rng(5).random(N)<0.5
        def tb(mask):
            o=np.full(T,np.nan); ti=rec2[:,0].astype(int); cj=rec2[:,1].astype(int); bl=rec2[:,2]
            for i in range(T):
                m=(ti==i)&mask[cj]
                if m.sum()<8: continue
                o[i]=np.mean((bl[m]-y[cj[m]])**2)
            return o
        x1=tb(h2); x2=tb(~h2); okk=~np.isnan(x1)&~np.isnan(x2)
        out.append((R, len(rec2)/T, spearmanr(x1[okk],x2[okk]).correlation, spearmanr(-skill[okk],x1[okk]).correlation))
    rounds=saved
    return out
curve=ledger_curve([3,6,12,24,48])
results['ledger_curve']=[(int(R),round(t,0),round(r1,3),round(r2,3)) for R,t,r1,r2 in curve]
json.dump(results, open('results/sim_results.json','w'), indent=1)
print("ledger curve (rounds, trades/trader, rho_halves, rho_skill):", results['ledger_curve'])
fig,ax=plt.subplots(figsize=(5,3.2))
ax.plot([c[1] for c in curve],[c[2] for c in curve],'o-',color='#1f4e79',label='split-half reliability of ledger (ρ)')
ax.plot([c[1] for c in curve],[c[3] for c in curve],'s--',color='#c0504d',label='correlation with latent skill (ρ)')
ax.set_xlabel('resolved positions per forecaster'); ax.set_ylabel('rank correlation'); ax.set_ylim(0,1)
ax.set_title('How many resolved positions a ledger needs'); ax.legend(frameon=False,fontsize=8)
plt.tight_layout(); plt.savefig('figures/sim_ledger.png',dpi=160); plt.close()
print("curve figure written")
