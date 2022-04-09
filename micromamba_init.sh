# >>> mamba initialize >>>
# !! Contents within this block are managed by 'mamba init' !!
export MAMBA_EXE="$PWD/micromamba";
export MAMBA_ROOT_PREFIX="micromamba_env";
__mamba_setup="$('$PWD/bin/micromamba' shell hook --shell bash --prefix 'micromamba_env' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__mamba_setup"
else
    if [ -f "micromamba_env/etc/profile.d/micromamba.sh" ]; then
        . "micromamba_env/etc/profile.d/micromamba.sh"
    else
        export  PATH="micromamba_env/bin:$PATH"  # extra space after export prevents interference from conda init
    fi
fi
unset __mamba_setup
# <<< mamba initialize <<<
