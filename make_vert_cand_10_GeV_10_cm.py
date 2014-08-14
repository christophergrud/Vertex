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
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_100_1_Mx4.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_10_1_guf.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_11_1_vEb.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_12_1_6fP.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_13_1_QoU.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_14_1_4I6.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_15_1_x6Z.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_16_1_6dr.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_17_1_6o2.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_18_1_zAa.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_19_1_n76.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_1_1_eLX.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_20_1_WeV.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_21_1_uSd.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_22_1_wD3.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_23_1_HUJ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_24_1_3ft.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_25_1_9Xi.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_26_1_TvY.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_27_1_wac.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_28_1_mAn.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_29_1_h8W.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_2_1_8ey.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_30_1_vFu.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_31_1_PDR.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_32_1_9AL.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_33_1_Nq3.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_34_1_o9B.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_35_1_29E.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_36_1_R5D.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_37_1_n9J.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_38_1_U24.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_39_1_tZ7.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_3_1_xVd.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_40_1_DUv.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_41_1_1Am.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_42_1_eM0.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_43_1_zSb.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_44_1_Se1.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_45_1_Chm.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_46_1_Xlk.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_47_1_cf5.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_48_1_aDi.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_49_1_mjy.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_4_1_1jR.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_50_1_D55.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_51_1_E3K.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_52_1_1Bq.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_53_1_j0b.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_54_1_dfr.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_55_1_elk.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_56_1_ged.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_57_1_9rf.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_58_1_Ak6.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_59_1_JLo.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_5_1_Z4c.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_60_1_NmJ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_61_1_G2U.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_62_1_sDr.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_63_1_7iI.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_64_1_kH5.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_65_1_uOK.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_66_1_xPg.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_67_1_GmJ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_68_1_EyK.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_69_1_J0d.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_6_1_s13.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_70_1_zCd.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_71_1_Rgr.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_72_1_e5g.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_73_1_SN4.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_74_1_vHp.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_75_1_hlT.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_76_1_nYB.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_77_1_ztO.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_78_1_EJx.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_79_1_JWy.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_7_1_uRb.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_80_1_faR.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_81_1_qDP.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_82_1_H19.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_83_1_LDU.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_84_1_yHv.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_85_1_xtR.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_86_1_o3M.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_87_1_MQ0.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_88_1_g2l.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_89_1_dSh.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_8_1_PFq.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_90_1_27t.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_91_1_VNw.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_92_1_3NV.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_93_1_fhf.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_94_1_4fC.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_95_1_iRG.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_96_1_Gg6.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_97_1_qbR.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_98_1_afj.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_99_1_7tZ.root',
        'file:/eos/uscms/store/user/cgrud85/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm/HTo2LongLivedTo4Mu_mass10_GeV_ctau_10_cm_Fixed_RECO/fe4dcd4503d15cd71a811a3397021d79/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_PU_9_1_p2n.root'
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
    fileName = cms.untracked.string('Mu_10_GeV_10_cm_with_2_new_cut.root'),
)

process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

process.p = cms.Path(process.generalVertCandidates)
#process.p = cms.Path(process.btagval + process.btagvalsubjetmu + process.btagvalsubjetbtag)
