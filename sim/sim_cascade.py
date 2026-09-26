"""Reliance-graph cascade experiment + sensitivity of the market simulation."""
import numpy as np, json, os
os.makedirs('figures', exist_ok=True); os.makedirs('results', exist_ok=True)
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
rng=np.random.default_rng(3)
N=5000
# preferential-attachment reliance DAG: each new claim relies on 0-3 earlier claims, chosen ∝ (1+in-degree)
indeg=np.zeros(N); parents=[[] for _ in range(N)]
for i in range(1,N):
    k=rng.choice([0,1,2,3],p=[0.3,0.4,0.2,0.1])
    if k==0: continue
    w=(1+indeg[:i]); w=w/w.sum()
    ps=rng.choice(i,size=min(k,i),replace=False,p=w)
    for p in ps: parents[i].append(p); indeg[p]+=1
children=[[] for _ in range(N)]
for i in range(N):
    for p in parents[i]: children[p].append(i)
def descendants(root):
    seen=set(); stack=[root]
    while stack:
        u=stack.pop()
        for c in children[u]:
            if c not in seen: seen.add(c); stack.append(c)
    return seen
q=rng.beta(2.2,1.8,N); y=(rng.random(N)<q).astype(int)
false_idx=np.where(y==0)[0]
# total dependents standing on false claims
dep_false=set()
for f in false_idx: dep_false|=descendants(f)
K=150
def flagged_by(sel):
    s=set()
    for c in sel:
        if y[c]==0: s|=descendants(c)
    return len(s)
rand=rng.choice(N,K,replace=False)
byload=np.argsort(-indeg)[:K]
# 'confirmed reliance' proxy: descendants count
desc_count=np.array([len(descendants(i)) for i in range(N)])
bydesc=np.argsort(-desc_count)[:K]
res=dict(total_false=int(len(false_idx)), dependents_on_false=int(len(dep_false)),
         flagged_random=flagged_by(rand), flagged_by_indegree=flagged_by(byload), flagged_by_descendants=flagged_by(bydesc),
         share_claims_with_any_dependents=float((desc_count>0).mean()), top1pct_share_of_dependents=float(np.sort(desc_count)[::-1][:50].sum()/desc_count.sum()))
print(json.dumps(res,indent=1)); json.dump(res,open('results/sim_cascade.json','w'),indent=1)
fig,ax=plt.subplots(figsize=(5,3.1))
labels=['random','highest in-degree','most descendants']; vals=[res['flagged_random'],res['flagged_by_indegree'],res['flagged_by_descendants']]
ax.bar(labels,vals,color=['#7f7f7f','#1f4e79','#9bbb59']); ax.set_ylabel('dependent claims flagged'); ax.set_title(f'Resolving {K} claims: dependents of false claims flagged (of {len(dep_false)})')
plt.tight_layout(); plt.savefig('figures/sim_cascade.png',dpi=160); plt.close()

# ---- sensitivity of market pricing (re-import model by exec with parameter overrides) ----
src=open('sim_market.py').read()
src=src.split("# ---------------- figures ----------------")[0]   # drop plotting
src=src.replace("json.dump(results, open('results/sim_results.json','w'), indent=1)","")
src=src.replace("print(json.dumps(results, indent=1))","")
def run(overrides):
    code=src
    for k,v in overrides.items(): code=code.replace(k,v,1)
    g={}
    exec(code,g)
    r=g['results']
    return r['brier_market'],r['brier_citation'],r['share_priced'],r['alloc']['open interest'][0],r['manip_final_lim']
rows=[]
for name,ov in [("baseline",{}),
                ("fewer forecasters (100)",{"T = 200":"T = 100"}),
                ("less skill (Beta(1,6))",{"skill = rng.beta(2, 5, T)":"skill = rng.beta(1, 6, T)"}),
                ("more skill (Beta(3,3))",{"skill = rng.beta(2, 5, T)":"skill = rng.beta(3, 3, T)"}),
                ("thin liquidity (b=100)",{"b = 300.0":"b = 100.0"}),
                ("deep liquidity (b=900)",{"b = 300.0":"b = 900.0"}),
                ("attention uncorrelated with reliance",{"look_p = np.clip(0.0045*(w**1.3), 0.0005, 0.6)":"look_p = np.full(N, 0.006)"})]:
    try:
        bm,bc,sp,cap,man=run(ov); rows.append((name,bm,bc,sp,cap,man))
        print(name,bm,bc,sp,cap,man)
    except Exception as e:
        print("ERR",name,e)
json.dump(rows,open('results/sim_sensitivity.json','w'),indent=1)
