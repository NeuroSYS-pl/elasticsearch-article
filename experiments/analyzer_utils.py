from typing import List
from elasticsearch.client import IndicesClient

from index_utils import IndexUtil
from config import DEFAULT_INDEX_NAME


class AnalyzerUtil:

    def __init__(
        self,
        index_name: str = DEFAULT_INDEX_NAME,
        elasticsearch_url: str = 'http://elasticsearch:9200'
    ):
        self.index = IndexUtil(index_name)
        self.indices_client = IndicesClient(self.index.elastic_connector)
        self.index.create_index()

    def analyze(self, text: str, analyzer: str) -> List[str]:
        tokens = self.indices_client.analyze(
            index=self.index.index_name,
            body={
                "analyzer": analyzer,
                "text": text,
            }
        )
        return [token['token'] for token in tokens['tokens']]
