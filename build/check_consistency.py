#!/usr/bin/env python3
"""Consistency scan for the documents.

1. Every 'Section N.M' / 'Section N' / 'Appendix X' reference must resolve to a heading in the same file
   (only enforced for the master, which has numbered sections).
2. No phrasing superseded by a design change may appear outside the revision record.

Exit non-zero on failure. Extend SUPERSEDED when the design moves.
"""
import re, sys, pathlib

SUPERSEDED = [
    # (regex, reason)
    (r"open interest cross(es|ing) the (protocol's stated )?cost", "trigger is the resolution fund reaching the protocol cost (v3.4)"),
    (r"resolution trigger: open interest", "trigger is the resolution fund (v3.4)"),
    (r"top decile of open interest", "priority is confirmed reliance x uncertainty (v3.4)"),
    (r"money at stake on a claim crosses", "open interest is traders' money; the fund pays (v1.1)"),
    (r"subsidy pool pays for the resolution", "the resolution fund pays, not the market-maker subsidy (v1.1)"),
    (r"needs to know buys", "reliant parties hedge and pay for resolution; they do not buy to express reliance (v1.1)"),
    (r"returned with the market's premium", "premium is paid from forfeited bonds weighted by contest (v1.1)"),
    (r"submission caps per author.*(this proposal|we propose)", "submission caps were withdrawn"),
]

def headings(text):
    secs=set()
    for m in re.finditer(r"^#{2,3}\s+(\d+(?:\.\d+)?)\b", text, re.M):
        secs.add(m.group(1))
    apps=set(re.findall(r"^##\s+Appendix\s+([A-Z])\b", text, re.M))
    return secs, apps

def check(path):
    text=pathlib.Path(path).read_text(encoding="utf-8")
    problems=[]
    # split off revision record so its self-descriptions are not flagged
    body=text.split("Revision record")[0] if "Revision record" in text else text
    for pat,reason in SUPERSEDED:
        for m in re.finditer(pat, body, re.I):
            line=body[:m.start()].count("\n")+1
            problems.append(f"{path}:{line}: superseded phrasing '{m.group(0)[:60]}' — {reason}")
    secs,apps=headings(text)
    if len(secs)>10:  # numbered document
        for m in re.finditer(r"\bSections?\s+(\d+(?:\.\d+)?)", body):
            ref=m.group(1)
            if ref not in secs and ref.split('.')[0] not in secs:
                line=body[:m.start()].count("\n")+1
                problems.append(f"{path}:{line}: reference to Section {ref} does not resolve")
        for m in re.finditer(r"\bAppendix\s+([A-Z])\b", body):
            if m.group(1) not in apps:
                line=body[:m.start()].count("\n")+1
                problems.append(f"{path}:{line}: reference to Appendix {m.group(1)} does not resolve")
    return problems

if __name__=="__main__":
    allp=[]
    for p in sys.argv[1:]:
        allp+=check(p)
    for p in allp: print(p)
    print(f"{len(allp)} problem(s)")
    sys.exit(1 if allp else 0)
