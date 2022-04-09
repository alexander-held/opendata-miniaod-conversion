wget -qO- https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj micromamba
./micromamba shell init -s bash -p micromamba_env

source micromamba_init.sh
micromamba activate
micromamba install python=3.10 -c conda-forge

micromamba install numpy -c conda-forge -y
python -m pip install uproot
micromamba install -y awkward -c conda-forge

tar -zcf micromamba_env.tar.gz micromamba_env
