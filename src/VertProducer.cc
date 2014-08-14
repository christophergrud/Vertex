// -*- C++ -*-
//
// Original Author:  Brian Drell
//         Created:  Fri May 18 22:57:40 CEST 2007
// $Id: Producer.cc,v 1.56 2011/12/23 08:13:39 innocent Exp $
//
// ---- Modified By: Christopher Grud ----
//


// system include files
#include <memory>

#include "MyAnalysis/Vertex/interface/VertProducer.h"

// Constructor
VertProducer::VertProducer(const edm::ParameterSet& iConfig) :
  theParams(iConfig) {

   // Registering V0 Collections
  //produces<reco::VertexCollection>("Kshort");
  //produces<reco::VertexCollection>("Lambda");
  //produces<reco::VertexCollection>("LambdaBar");

  // Trying this with Candidates instead of the simple reco::Vertex
  //  produces< reco::VertexCompositeCandidateCollection >("Kshort");
  //  produces< reco::VertexCompositeCandidateCollection >("Lambda");
    produces< reco::VertexCompositeCandidateCollection >("MyVertices");  // *************************************************************************
  //produces< reco::VertexCompositeCandidateCollection >("LambdaBar");

}

// (Empty) Destructor
VertProducer::~VertProducer() {

}


//
// Methods
//

// Producer Method
void VertProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
   using namespace edm;

   // Create VertFitter object which reconstructs the vertices and creates
   //  (and contains) collections of Kshorts, Lambda0s
   VertFitter theVees(theParams, iEvent, iSetup);

   // Create auto_ptr for each collection to be stored in the Event
/*   std::auto_ptr< reco::VertexCompositeCandidateCollection > kShortCandidates( new reco::VertexCompositeCandidateCollection );
   kShortCandidates->reserve( theVees.getKshorts().size() ); 

   std::auto_ptr< reco::VertexCompositeCandidateCollection > lambdaCandidates( new reco::VertexCompositeCandidateCollection );
   lambdaCandidates->reserve( theVees.getLambdas().size() );

   std::copy( theVees.getKshorts().begin(), theVees.getKshorts().end(), std::back_inserter(*kShortCandidates) );
   std::copy( theVees.getLambdas().begin(), theVees.getLambdas().end(), std::back_inserter(*lambdaCandidates) ); */

   std::auto_ptr< reco::VertexCompositeCandidateCollection > myVertexCandidates( new reco::VertexCompositeCandidateCollection ); // *****************
   myVertexCandidates->reserve( theVees.getMyVertices().size() ); // ********************************************************************************

   std::copy( theVees.getMyVertices().begin(), theVees.getMyVertices().end(), std::back_inserter(*myVertexCandidates) );

   //std::cout<< "Size of Collection = " << theVees.getMyVertices().size() << std::endl;

   // Write the collections to the Event
   //iEvent.put( kShortCandidates, std::string("Kshort") );
   //iEvent.put( lambdaCandidates, std::string("Lambda") );
   iEvent.put(myVertexCandidates, std::string("MyVertices")); // ************************************************************************************

}


//void VertProducer::beginJob() {
void VertProducer::beginJob() {
}


void VertProducer::endJob() {
}

//define this as a plug-in
#include "FWCore/PluginManager/interface/ModuleDef.h"

DEFINE_FWK_MODULE(VertProducer);
//DEFINE_FWK_MODULE(V0finder);
