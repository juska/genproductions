import FWCore.ParameterSet.Config as cms

# tune for pT-ordered showers
from Configuration.Generator.PythiaUEP0Settings_cfi import *

generator = cms.EDFilter(
    "Pythia6HadronizerFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(7000.0),
    crossSection = cms.untracked.double(0.1331),
    maxEventsToPrint = cms.untracked.int32(5),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock, 
        processParameters = cms.vstring(
            'MSEL=0           ! User defined processes', 
            'MSTJ(1)=1        ! Fragmentation/hadronization on or off', 
            'MSTP(61)=1       ! Parton showering on or off', 
            'MSTP(51)=10050   ! structure function chosen (external PDF CTEQ6m)', 
            'MSTP(52)=2       ! work with LHAPDF', 
            'PMAS(5,1)=4.75   ! b quark mass', 
            'PMAS(6,1)=172.5  ! t quark mass' 
            
            'MDME(210,1)=0    ! Higgs decay into dd',
            'MDME(211,1)=0    ! Higgs decay into uu',
            'MDME(212,1)=0    ! Higgs decay into ss',
            'MDME(213,1)=0    ! Higgs decay into cc',
            'MDME(214,1)=0    ! Higgs decay into bb',
            'MDME(215,1)=0    ! Higgs decay into tt',
            'MDME(216,1)=0    ! Higgs decay into bbbar prime',
            'MDME(217,1)=0    ! Higgs decay into ttbar prime',
            'MDME(218,1)=0    ! Higgs decay into e e',
            'MDME(219,1)=0    ! Higgs decay into mu mu',
            'MDME(220,1)=0    ! Higgs decay into tau tau',
            'MDME(221,1)=0    ! Higgs decay into tau tau prime',
            'MDME(222,1)=0    ! Higgs decay into g g',
            'MDME(223,1)=0    ! Higgs decay into gam gam',
            'MDME(224,1)=0    ! Higgs decay into gam Z',
            'MDME(225,1)=0    ! Higgs decay into Z Z',
            'MDME(226,1)=1    ! Higgs decay into W W',
            
            'MDME(190,1)=4    ! W decay into dbar u',
            'MDME(191,1)=4    ! W decay into dbar c',
            'MDME(192,1)=4    ! W decay into dbar t',
            'MDME(194,1)=4    ! W decay into sbar u',
            'MDME(195,1)=4    ! W decay into sbar c',
            'MDME(196,1)=4    ! W decay into sbar t',
            'MDME(198,1)=4    ! W decay into bbar u',
            'MDME(199,1)=4    ! W decay into bbar c',
            'MDME(200,1)=4    ! W decay into bbar t',
            'MDME(206,1)=5    ! W decay into e+ nu_e',
            'MDME(207,1)=5    ! W decay into mu+ nu_mu',
            'MDME(208,1)=0    ! W decay into tau+ nu_tau'
            ),
        parameterSets = cms.vstring(
            'pythiaUESettings', 
            'processParameters'
            )
        )
    )

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/POWHEG_PYTHIA6_qqH200_WW_lnujj_7TeV_cff.py,v $'),
    annotation = cms.untracked.string('POWHEG + PYTHIA6 - VBF Higgs -> WW -> lnujj at 7TeV')
    )

