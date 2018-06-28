from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class Required(object):
    """
    Required
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Required'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Classification'),
        ))
        graph.add((
            URIRef(es + 'Required'),
            URIRef(dc + 'title'),
            Literal('Required', lang='en')
        ))
        graph.add((
            URIRef(es + 'Required'),
            URIRef(dc + 'description'),
            Literal("""
                The required disciplines are those, as the name says, that are
                essential to be taken by the students to obtain the bachelor's
                degree.
            """, lang='en')
        ))
