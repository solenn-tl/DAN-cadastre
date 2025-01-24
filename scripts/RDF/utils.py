from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS
import uuid

class RDFUtil:
    def __init__(self):
        # Initialize the RDF graph
        self.graph = Graph()
        # Define common namespaces
        self.ADDR = Namespace("http://rdf.geohistoricaldata.org/def/address#")
        self.CAD = Namespace("http://rdf.geohistoricaldata.org/def/cadastre#")
        self.SOURCE = Namespace("http://rdf.geohistoricaldata.org/id/source/")
        self.TAXPAYER = Namespace("http://rdf.geohistoricaldata.org/id/taxpayer/")
        self.graph.bind("addr", self.ADDR)
        self.graph.bind("cad", self.CAD)
        self.graph.bind("source", self.SOURCE)

    def add_taxpayer(self, taxpayer_json, element_uuid:str):
        """
        Convert a taxpayer JSON feature to RDF and add it to the graph. Can contain one to many taxpayers

        :param taxpayer_json: Dictionary containing person data
        Example: {
            "name"
            "firstnames"
            "address"
            "activity"
            "title"
            "familystatus"
            "birthname"
        }
        """
        counter = 1
        for taxpayer in taxpayer_json["entities_json"]["taxpayers"]:
            person_uri = URIRef(self.TAXPAYER[taxpayer_json["element_uuid"] + '_taxpayer_' + str(counter)])
            self.graph.add((person_uri, RDF.type, self.CAD.Taxpayer))
            
            #RDFS Label
            if len(taxpayer_json['name']) > 0 and len(taxpayer_json['firstnames']) > 0:
                self.graph.add((person_uri, RDFS.label, Literal(taxpayer_json['name'] + ' ' + taxpayer_json['firstnames'])))
            else:
                self.graph.add((person_uri, RDFS.label, Literal(taxpayer_json['name'])))
                
            #Taxpayer properties
            if len(taxpayer_json['name']) > 0:
                self.graph.add((person_uri, self.CAD.taxpayerLabel, Literal(taxpayer_json['name'])))
            if len(taxpayer_json['firstnames']) > 0:
                self.graph.add((person_uri, self.CAD.taxpayerFirstName, Literal(taxpayer_json['firstnames'])))
            if len(taxpayer_json['activity']) > 0:
                for elem in taxpayer_json['activity']:
                    self.graph.add((person_uri, self.CAD.taxpayerActivity, Literal(elem)))
            if len(taxpayer_json['address']) > 0:
                for elem in taxpayer_json['address']:
                    self.graph.add((person_uri, self.CAD.taxpayerAddress, Literal(elem)))
            if len(taxpayer_json['title']) > 0:
                for elem in taxpayer_json['title']:
                    self.graph.add((person_uri, self.CAD.taxpayerTitle, Literal(elem)))
            if len(taxpayer_json['familystatus']) > 0:
                for elem in taxpayer_json['familystatus']:
                    self.graph.add((person_uri, self.CAD.taxpayerStatus, Literal(elem)))
            if len(taxpayer_json['birthname']) > 0:
                self.graph.add((person_uri, self.CAD.taxpayerBirthname, Literal(taxpayer_json['birthname'])))
    
            #Source
            self.graph.add((person_uri, self.CAD.fromSource, URIRef(self.SOURCE[element_uuid])))
            counter += 1