# Contribution records

`make_contribution_record.py` generates `RECORD.md` quarterly (CI workflow `contribution-record.yml`, or run by hand with an optional `--since` date as the first argument). It counts, per contributor: commits touching the master document, schemas, templates, tools, simulation and records; AI-assisted commits by model (from `Assisted-by:` trailers); sustained challenges from `records/challenges/`; resolutions performed from `records/resolutions/`.

Lines changed are not counted anywhere. That is deliberate.
