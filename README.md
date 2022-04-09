# opendata-miniaod-conversion

setup for running miniAOD->ntuple conversion for CMS 2015 Open Data at `t3.unl.edu`
- create conda env via `build_env.sh`
- `micromamba_init.sh` is needed for sourcing env in jobs
- custom POET configuration `poet_cfg.py` takes input file as arg and writes to `out.root`
- tree merging via `merge_trees.py`, resulting in `out_merged.root`
- job execution details are in `run.sh` (need to adjust `X509_USER_PROXY` to use correct id)
- submission script is `job.sub`
    - update this to include a full list of files
