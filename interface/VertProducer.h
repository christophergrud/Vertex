// -*- C++ -*-
//
// Original Author:  Brian Drell
//         Created:  Fri May 18 22:57:40 CEST 2007
// $Id: VertProducer.cc,v 1.56 2011/12/23 08:13:39 innocent Exp $
//
// ---- Modified By: Christopher Grud
//

#ifndef RECOVERTEX__V0_PRODUCER_H
#define RECOVERTEX__V0_PRODUCER_H

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/Framework/interface/ESHandle.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
//#include "DataFormats/V0Candidate/interface/V0Candidate.h"
#include "DataFormats/Candidate/interface/VertexCompositeCandidate.h"

#include "MyAnalysis/Vertex/interface/VertFitter.h"

class VertProducer : public edm::EDProducer {
public:
  explicit VertProducer(const edm::ParameterSet&);
  ~VertProducer();

private:
  //virtual void beginJob() ;
  virtual void beginJob();
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  edm::ParameterSet theParams;
      
};

#endif
