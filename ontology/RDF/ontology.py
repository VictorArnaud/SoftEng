from rdflib import Graph
from knowledge import Knowledge
# from academic import AcademicDomain

graph = Graph()
Knowledge(graph)
# AcademicDomain(graph)
graph.serialize("ontology/RDF/softeng.rdf")


# PREFIX ---------------------------------------------------
# dc = "http://purl.org/dc/elements/1.1/"
# rdfs = "http://www.w3.org/2000/01/rdf-schema#"
# rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
# es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"
# dbpedia = "http://dbpedia.org/resource/"
