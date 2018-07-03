from core import Query, Sesame
from django.template.defaultfilters import slugify
from .comments import Comments
from .structure import Structure


class BasicDeveloperHumanFactors(object):
    """
    Topic: Basic Developer Human Factors
    """

    COMMENTS = 0
    STRUCTURE = 1

    def __init__(self):
        """
        Create a topic.
        """

        result = self.get_information()

        self.uri = "http://www.semanticweb.org/ontologies/2018/Knowledge/Basic_Developer_Human_Factors"
        self.title = result['title']['value']
        self.description = result['description']['value']
        self.slug = slugify(self.title)

    def get_information(self):
        """
        Get the information from triple store
        """

        query = """
            PREFIX knowledge: <http://www.semanticweb.org/ontologies/2018/Knowledge/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title ?description
            WHERE {
              knowledge:Basic_Developer_Human_Factors dc:title ?title ;
              dc:description ?description
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_subtopic(self, subtopic=None):
        """
        Get a specific subtopic.
        """

        if subtopic == self.COMMENTS:
            return Comments()
        elif subtopic == self.STRUCTURE:
            return Structure()
        else:
            return [
                Comments(),
                Structure()
            ]
