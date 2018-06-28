from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class AlternateAbstractions(object):
    """
    Subtopic: Alternate Abstractions
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(es + 'Alternate_Abstraction'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Abstraction'),
        ))
        graph.add((
            URIRef(es + 'Alternate_Abstraction'),
            URIRef(dc + 'title'),
            Literal('Alternate Abstraction', lang='en')
        ))
        graph.add((
            URIRef(es + 'Alternate_Abstraction'),
            URIRef(dc + 'description'),
            Literal("""
                Sometimes it is useful to have multiple alternate
                abstractions for the same problem so that one can
                keep different perspectives in mind. For example,
                we can have a class diagram, a state chart, and a
                sequence diagram for the same software at the same
                level of abstraction. These alternate abstractions
                do not form a hierarchy but rather complement each
                other in helping understanding the problem and its
                solution. Though beneficial, it is as times difficult
                to keep alternate abstractions in sync.
            """, lang='en')
        ))
