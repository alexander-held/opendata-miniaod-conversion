# adapted from https://github.com/cms-opendata-analyses/PhysObjectExtractorTool/blob/2015MiniAOD/PhysObjectExtractor/python/poet_cfg.py
import os
import sys

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes

process = cms.Process("POET")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = "WARNING"
process.MessageLogger.categories.append("POET")
process.MessageLogger.cerr.INFO = cms.untracked.PSet(limit=cms.untracked.int32(-1))
process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(True))

# no limit on events
process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(-1))

# file to process is provided as argument
input_file = sys.argv[-1]
print "INFO - processing", input_file
process.source = cms.Source("PoolSource", fileNames=cms.untracked.vstring(sys.argv[-1]))

process.myelectrons = cms.EDAnalyzer(
    "ElectronAnalyzer",
    electrons=cms.InputTag("slimmedElectrons"),
    vertices=cms.InputTag("offlineSlimmedPrimaryVertices"),
)

process.mymuons = cms.EDAnalyzer(
    "MuonAnalyzer",
    muons=cms.InputTag("slimmedMuons"),
    vertices=cms.InputTag("offlineSlimmedPrimaryVertices"),
)

process.mytaus = cms.EDAnalyzer("TauAnalyzer", taus=cms.InputTag("slimmedTaus"))

process.myphotons = cms.EDAnalyzer(
    "PhotonAnalyzer", photons=cms.InputTag("slimmedPhotons")
)

process.mymets = cms.EDAnalyzer("MetAnalyzer", mets=cms.InputTag("slimmedMETs"))

process.mytriggers = cms.EDAnalyzer(
    "TriggObjectAnalyzer", objects=cms.InputTag("selectedPatTrigger")
)

process.mypvertex = cms.EDAnalyzer(
    "VertexAnalyzer",
    vertices=cms.InputTag("offlineSlimmedPrimaryVertices"),
    beams=cms.InputTag("offlineBeamSpot"),
)

process.mygenparticle = cms.EDAnalyzer(
    "GenParticleAnalyzer",
    pruned=cms.InputTag("prunedGenParticles"),
    # ---- Collect particles with specific "pdgid:status"
    # ---- if 0:0, collect them all
    input_particle=cms.vstring("1:11", "1:13", "1:22", "2:15"),
)

process.myjets = cms.EDAnalyzer("JetAnalyzer", jets=cms.InputTag("slimmedJets"))

cwd = os.getcwd()

# output file name (need to create folder structure?)
#output_name = "datasets/" + input_file.lstrip(
#    "root://eospublic.cern.ch//eos/opendata/cms/"
#)
#print "INFO - output file (relative)", output_name
#print "INFO - output file (absolute)", cwd + "/" + output_name

# ensure directory structure exists
#path = "/".join(output_name.split("/")[0:-1])
#print "INFO - output directory (relative)", path
#print "INFO - output directory (absolute)", cwd + "/" + path

#if not os.path.isdir(path):
#    try:
#        os.makedirs(path)
#        print "INFO - creating output directory"
#    except:
#        pass  # in case of a race condition where directory is created in parallel

process.TFileService = cms.Service("TFileService", fileName=cms.string("out.root"))

process.p = cms.Path(
    process.myelectrons
    + process.mymuons
    + process.mytaus
    + process.myphotons
    + process.mymets
    + process.mytriggers
    + process.mypvertex
    + process.mygenparticle
    + process.myjets
)

