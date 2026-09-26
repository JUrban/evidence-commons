from ec.recorder import WorkflowLog, verify_disclosure, merkle_root, merkle_proof, verify_proof, sha

def test_merkle_roundtrip():
    leaves = [sha(str(i)) for i in range(7)]
    root = merkle_root(leaves)
    for i in range(7): assert verify_proof(leaves[i], merkle_proof(leaves, i), root)
    assert not verify_proof(leaves[0], merkle_proof(leaves, 1), root)

def test_chain_and_tamper_detection():
    log = WorkflowLog("L1")
    for k in range(5): log.append("prompt", "a", {"k": k})
    log.checkpoint()
    assert log.verify_chain()
    log.entries[2].actor = "b"  # tamper
    assert not log.verify_chain()

def test_selective_disclosure_verifies_without_other_entries():
    log = WorkflowLog("L2")
    for k in range(6): log.append("human_edit", f"p{k}", {"text": f"secret {k}"})
    log.checkpoint()
    d = log.disclose([3])
    assert verify_disclosure(d) and len(d["entries"]) == 1 and d["entries"][0]["content"]["text"] == "secret 3"
    d["entries"][0]["content"]["text"] = "forged"
    assert not verify_disclosure(d)

def test_to_record_matches_schema_shape():
    log = WorkflowLog("L3"); log.append("decision", "w", {"b": 1}); log.checkpoint()
    r = log.to_record()
    assert set(r) >= {"id", "level", "entries", "checkpoints"} and r["checkpoints"][0]["merkle_root"]
