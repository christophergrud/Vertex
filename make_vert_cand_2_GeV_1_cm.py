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
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_100_1_ROh.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_10_1_w4k.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_11_1_jbI.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_12_1_nBC.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_13_1_j6F.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_14_1_bl8.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_15_1_Uhm.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_16_1_oML.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_17_1_U5P.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_18_1_H4w.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_19_1_o59.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_1_1_OLz.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_20_1_vdJ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_21_1_bfe.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_22_1_sE8.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_23_1_V4B.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_24_1_hcT.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_25_1_4SQ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_26_1_C3x.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_27_1_vot.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_28_1_hEf.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_29_1_vSs.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_2_1_xdC.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_30_1_T9y.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_31_1_Lu4.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_32_1_qgH.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_33_1_y6u.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_34_1_Nof.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_35_1_XZe.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_36_1_97c.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_37_1_BvP.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_38_1_OXa.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_39_1_44M.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_3_1_OGE.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_40_1_4mO.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_41_1_fQv.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_42_1_Nb0.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_43_1_x9r.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_44_1_qlR.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_45_1_cWV.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_46_1_c27.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_47_1_0xd.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_48_1_Czu.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_49_1_S3D.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_4_1_Xjm.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_50_1_aS2.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_51_1_9mI.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_52_1_gFq.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_53_1_aKu.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_54_1_vAa.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_55_1_WZY.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_56_1_BcW.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_57_1_R5d.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_58_1_MbH.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_59_1_nLH.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_5_1_MKI.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_60_1_ngc.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_61_1_z3d.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_62_1_Vfk.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_63_1_lVZ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_64_1_rgj.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_65_1_fJg.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_66_1_qbO.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_67_1_5BW.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_68_1_pn0.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_69_1_nZD.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_6_1_528.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_70_1_IVR.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_71_1_jUd.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_72_1_hHD.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_73_1_QQ5.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_74_1_0HX.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_75_1_cFI.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_76_1_uve.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_77_1_nJR.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_78_1_lZp.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_79_1_pHZ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_7_1_Is2.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_80_1_Zua.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_81_1_pbu.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_82_1_Bs1.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_83_1_ApZ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_84_1_g5i.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_85_1_yKz.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_86_1_ta6.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_87_1_gWA.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_88_1_kSQ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_89_1_c0L.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_8_1_qkG.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_90_1_L6y.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_91_1_WmC.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_92_1_6pd.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_93_1_g3H.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_94_1_e1T.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_95_1_Qch.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_96_1_8DM.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_97_1_7cm.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_98_1_vJg.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_99_1_kEf.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm/HTo2LongLivedTo4Mu_mass2_GeV_ctau_1_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_9_1_3JR.root'
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
    fileName = cms.untracked.string('/eos/uscms/store/user/cgrud85/ROOTFiles/Mu_2_GeV_1_cm_with_2_new_cut.root'),
)

process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

process.p = cms.Path(process.generalVertCandidates)
#process.p = cms.Path(process.btagval + process.btagvalsubjetmu + process.btagvalsubjetbtag)
