#!/bin/bash
/bin/pwd
/bin/uname -a
/bin/hostname

source /cvmfs/oasis.opensciencegrid.org/osg-software/osg-wn-client/3.4/current/el6-x86_64/setup.sh
echo $PWD
export X509_USER_PROXY=$PWD/x509up_u7355  # id -u alheld
voms-proxy-info --all
export SCRAM_ARCH=slc6_amd64_gcc493
source /cvmfs/cms.cern.ch/cmsset_default.sh
scramv1 project CMSSW CMSSW_7_6_7
cd CMSSW_7_6_7/src
eval `scramv1 runtime -sh`
cp -r ../../PhysObjectExtractorTool ./
scram b

INP=$1
echo "input: $INP"
OUTP=datasets/`echo $INP | egrep "RunIIFall15MiniAODv2\/(.*)" -o`
echo "output: $OUTP"

cp -r ../../poet_cfg.py .
echo "running cmsRun poet_cfg.py $INP"
cmsRun poet_cfg.py $INP
echo "saving to out.root"

export HOME=$PWD
cp ../../micromamba_env.tar.gz .
tar -zxf micromamba_env.tar.gz
cp ../../micromamba_init.sh .
cp -r ../../micromamba .
source micromamba_init.sh
micromamba activate

cp ../../merge_trees.py .

ls -al

OLDP=$PYTHONPATH
export PYTHONPATH=""
python merge_trees.py "out.root"
export PYTHONPATH=$OLDP

ls -al

echo "xrdcp -f -p out_merged.root root://xrootd-local.unl.edu:1094//store/user/AGC/$OUTP"
xrdcp -f -p out_merged.root root://xrootd-local.unl.edu:1094//store/user/AGC/$OUTP
