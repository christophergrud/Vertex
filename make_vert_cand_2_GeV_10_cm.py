import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('python')

options.register('outFilename', 'whatsthis.root',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Output file name"
)
options.register('reportEvery', 1000,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "Report every N events (default is N=1000)"
)
options.register('triggerSelection', '',
    VarParsing.multiplicity.list,
    VarParsing.varType.string,
    "Trigger selection"
)
options.register('useJetProbaTree', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use jet probability tree"
)
options.register('applyFatJetMuonTagging', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply muon tagging to fat jets"
)
options.register('applyFatJetBTagging', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply b tagging to fat jets"
)
options.register('fatJetDoubleTagging', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Require fat jets to be double-tagged"
)
options.register('processSubJets', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Process subjets"
)
options.register('applySubJetMuonTagging', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply muon tagging to subjets"
)
options.register('applySubJetBTagging', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply b tagging to subjets"
)
options.register('dynamicMuonSubJetDR', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use dynamic muon-subjet dR requirement"
)
options.register('applySFs', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply b-tagging SFs"
)
options.register('useFlavorCategories', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use flavor categories for MC distributions"
)
options.register('useRelaxedMuonID', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use relaxed muon ID"
)
options.register('fatJetPtMin', 300.,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Minimum fat jet Pt"
)
options.register('fatJetPtMax', 1.E6,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Maximum fat jet Pt"
)
options.register('fatJetPrunedMassMin', 0.,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Minimum fat jet pruned mass"
)
options.register('fatJetPrunedMassMax', 1.E6,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Maximum fat jet pruned mass"
)
options.register('fatJetBDiscrCut', 0.244,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "B discriminator cut for fat jets"
)
options.register('subJetBDiscrCut', 0.244,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "B discriminator cut for fat jets"
)
options.register('SFbShift', 0.,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Shift in SFb in units of sigmas"
)
options.register('SFlShift', 0.,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Shift in SFl in units of sigmas"
)
options.register('doPUReweighting', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Do pileup reweighting"
)

## 'maxEvents' is already registered by the Framework, changing default value
options.setDefault('maxEvents', 10000)

options.parseArguments()

#print options

process = cms.Process("BTagVal")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'START53_V27::All'

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load('Configuration.StandardSequences.Reconstruction_cff')

process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.cerr.default.limit = 10

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) ) # Keep as such

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        #'/store/user/cgrud/HTo2LongLivedTo4L/HTo2LongLivedTo4L_RECO/5e15970c9cd660dcfbbfda7d7e828bfd/'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_100_1_ehz.root'
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_100_1_xzz.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_10_1_JWD.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_11_1_jgP.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_12_1_Jcl.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_13_1_E9I.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_14_1_YJx.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_15_1_Nac.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_16_1_esk.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_17_1_F4v.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_18_1_yU0.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_19_1_zjg.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_1_1_frN.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_20_1_IWq.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_21_1_sDr.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_22_1_Jb4.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_23_1_Aha.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_24_1_y04.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_25_1_tEo.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_26_1_0zk.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_27_1_k0q.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_28_1_Yx3.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_29_1_RDJ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_2_1_8Dq.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_30_1_cAG.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_31_1_EV5.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_32_1_b9c.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_33_1_4Mo.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_34_1_OMh.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_35_1_VDm.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_36_1_vCk.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_37_1_QFK.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_38_1_6bd.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_39_1_HpS.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_3_1_Ehj.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_40_1_xWy.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_41_1_GY6.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_42_1_WcB.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_43_1_Vdx.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_44_1_6kR.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_45_1_Vs2.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_46_1_jDt.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_47_1_RHb.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_48_1_5mo.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_49_1_hYN.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_4_1_OZs.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_50_1_AK1.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_51_1_YxR.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_52_1_JS4.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_53_1_Rnd.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_54_1_kcx.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_55_1_EUj.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_56_1_tXK.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_57_1_IBa.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_58_1_KAl.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_59_1_yFs.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_5_1_lI3.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_60_1_HcQ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_61_1_x5R.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_62_1_Rcx.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_63_1_A2v.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_64_1_msi.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_65_1_2Ec.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_66_1_Ul4.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_67_1_NUN.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_68_1_MT7.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_69_1_ljz.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_6_1_cKZ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_70_1_1AS.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_71_1_Ffw.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_72_1_G2r.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_73_1_qNx.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_74_1_rVp.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_75_1_uTW.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_76_1_NfZ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_77_1_bi4.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_78_1_osv.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_79_1_x1o.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_7_1_9ZP.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_80_1_uAa.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_81_1_J2P.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_82_1_q3q.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_83_1_hEF.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_84_1_beZ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_85_1_Vrc.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_86_1_8Wl.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_87_1_W5a.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_88_1_V0A.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_89_1_vJJ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_8_1_XSg.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_90_1_fSm.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_91_1_qVF.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_92_1_Qni.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_93_1_BVA.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_94_1_95z.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_95_1_wM0.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_96_1_UTK.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_97_1_azh.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_98_1_cUk.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_99_1_7uI.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_9_1_Jdy.root'
    )
)

## Output file
process.TFileService = cms.Service("TFileService",
    fileName = cms.string(options.outFilename)
)

from inputFiles_cfi import *
process.btagval = cms.EDAnalyzer('BTagValidation',
    MaxEvents              = cms.int32(options.maxEvents),
    ReportEvery            = cms.int32(options.reportEvery),
    UseJetProbaTree        = cms.bool(options.useJetProbaTree),
    InputTTree             = cms.string('btagana/ttree'),
    InputFiles             = cms.vstring(FileNames),
    UseFlavorCategories    = cms.bool(options.useFlavorCategories),
    UseRelaxedMuonID       = cms.bool(options.useRelaxedMuonID),
    ApplyFatJetMuonTagging = cms.bool(options.applyFatJetMuonTagging),
    ApplyFatJetBTagging    = cms.bool(options.applyFatJetBTagging),
    FatJetDoubleTagging    = cms.bool(options.fatJetDoubleTagging),
    ProcessSubJets         = cms.bool(options.processSubJets),
    ApplySubJetMuonTagging = cms.bool(options.applySubJetMuonTagging),
    ApplySubJetBTagging    = cms.bool(options.applySubJetBTagging),
    DynamicMuonSubJetDR    = cms.bool(options.dynamicMuonSubJetDR),
    ApplySFs               = cms.bool(options.applySFs),
    FatJetBDiscrCut        = cms.double(options.fatJetBDiscrCut),
    SubJetBDiscrCut        = cms.double(options.subJetBDiscrCut),
    FatJetPtMin            = cms.double(options.fatJetPtMin),
    FatJetPtMax            = cms.double(options.fatJetPtMax),
    FatJetPrunedMassMin    = cms.double(options.fatJetPrunedMassMin),
    FatJetPrunedMassMax    = cms.double(options.fatJetPrunedMassMax),
    FatJetAbsEtaMax        = cms.double(2.4),
    SFbShift               = cms.double(options.SFbShift),
    SFlShift               = cms.double(options.SFlShift),
    DoPUReweighting        = cms.bool(options.doPUReweighting),
    File_PUDistMC          = cms.string('PUDistMC_Summer12_PU_S10.root'),
    File_PUDistData        = cms.string('PUDistData_Run2012ABCD.root'),
    Hist_PUDistMC          = cms.string('PUWeights_Summer12_S10PUWeights_Summer12_S10'),
    Hist_PUDistData        = cms.string('pileup'),
    TriggerSelection       = cms.vstring( # OR of all listed triggers applied, empty list --> no trigger selection applied
        options.triggerSelection
    ),
    TriggerPathNames       = cms.vstring(
        "HLT_Jet15U*",
        "HLT_Jet30_v*",
        "HLT_PFJet40_v*",
        "HLT_Jet30U*",
        "HLT_Jet60_v*",
        "HLT_Jet50U*",
        "HLT_Jet80_v*",
        "HLT_PFJet80_v*",
        "HLT_Jet70U*",
        "HLT_Jet110_v*",
        "HLT_Jet100U*",
        "HLT_Jet150_v*",
        "HLT_PFJet140_v*",
        "HLT_Jet140U*",
        "HLT_Jet190_v*",
        "HLT_PFJet200_v*",
        "HLT_Jet240_v*",
        "HLT_PFJet260_v*",
        "HLT_Jet300_v*",
        "HLT_PFJet320_v*",
        "HLT_DiPFJetAve320_v*",
        "HLT_PFJet400_v*",
        "HLT_DiJetAve15U*",
        "HLT_DiJetAve30_v*",
        "HLT_DiPFJetAve40_v*",
        "HLT_DiJetAve30U*",
        "HLT_DiJetAve60_v*",
        "HLT_DiPFJetAve80_v*",
        "HLT_DiJetAve50U*",
        "HLT_DiJetAve80_v*",
        "HLT_DiPFJetAve140_v*",
        "HLT_BTagMu_Jet10U*",
        "HLT_BTagMu_Jet20U*",
        "HLT_BTagMu_DiJet20U*",
        "HLT_BTagMu_DiJet20U_Mu5*",
        "HLT_BTagMu_DiJet20_Mu5*",
        "HLT_BTagMu_DiJet20_L1FastJet_Mu5_v*",
        "HLT_BTagMu_DiJet30U",
        "HLT_BTagMu_DiJet30U_v*",
        "HLT_BTagMu_DiJet30U_Mu5*",
        "HLT_BTagMu_DiJet60_Mu7*",
        "HLT_BTagMu_DiJet40_Mu5*",
        "HLT_BTagMu_DiJet20_L1FastJet_Mu5*",
        "HLT_BTagMu_DiJet80_Mu9*",
        "HLT_BTagMu_DiJet70_Mu5*",
        "HLT_BTagMu_DiJet70_L1FastJet_Mu5*",
        "HLT_BTagMu_DiJet100_Mu9_v*",
        "HLT_BTagMu_DiJet110_Mu5*",
        "HLT_BTagMu_DiJet110_L1FastJet_Mu5*",
        "HLT_BTagMu_Jet300_L1FastJet_Mu5*",
        "HLT_BTagMu_Jet300_Mu5*",
        "HLT_HT200",
        "HLT_HT240",
        "HLT_HT100U",
        "HLT_HT120U",
        "HLT_HT140U",
        "HLT_HT50U_v*",
        "HLT_HT100U_v*",
        "HLT_HT130U_v*",
        "HLT_HT140U_Eta3_v*",
        "HLT_HT140U_J30U_Eta3_v*",
        "HLT_HT150U_Eta3_v*",
        "HLT_HT150U_v*",
        "HLT_HT160U_Eta3_v*",
        "HLT_HT160U_v*",
        "HLT_HT200U_v*",
        "HLT_HT150_v*",
        "HLT_HT160_v*",
        "HLT_HT200_v*",
        "HLT_HT240_v*",
        "HLT_HT250_v*",
        "HLT_HT260_v*",
        "HLT_HT300_v*",
        "HLT_HT350_v*",
        "HLT_HT360_v*",
        "HLT_HT400_v*",
        "HLT_HT440_v*",
        "HLT_HT450_v*",
        "HLT_HT500_v*",
        "HLT_HT520_v*",
        "HLT_HT550_v*",
        "HLT_HT600_v*",
        "HLT_HT650_v*",
        "HLT_HT700_v*",
        "HLT_HT750_L1FastJet_v*",
        "HLT_HT750_v*",
        "HLT_HT2000_v*"
    )
)

#process.btagvalsubjetmu = process.btagval.clone(
    #ApplySubJetMuonTagging = cms.bool(not options.applySubJetMuonTagging),
#)

#process.btagvalsubjetbtag = process.btagval.clone(
    #ApplySubJetMuonTagging = cms.bool(not options.applySubJetMuonTagging),
    #ApplySubJetBTagging = cms.bool(True),
#)
process.load("MyAnalysis.Vertex.generalVertCandidates_cfi")
process.load("RecoVertex.V0Producer.generalV0Candidates_cfi")
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('/eos/uscms/store/user/cgrud85/ROOTFiles/Mu_2_GeV_10_cm_with_2_new_cut.root'),
)

process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

process.p = cms.Path(process.generalVertCandidates)
#process.p = cms.Path(process.btagval + process.btagvalsubjetmu + process.btagvalsubjetbtag)
