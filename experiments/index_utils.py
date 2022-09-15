import os
import json
from typing import Dict, Any, List, Callable

import pandas as pd
from tqdm.notebook import tqdm
from elasticsearch import Elasticsearch

from config import DEFAULT_SETTINGS_PATH, DEFAULT_INDEX_NAME


class IndexUtil:

    def __init__(self, index_name: str = DEFAULT_INDEX_NAME, elasticsearch_url: str = 'http://elasticsearch:9200'):
        self.index_name = index_name
        self.elastic_connector = Elasticsearch(elasticsearch_url)

    @staticmethod
    def get_default_settings(path=DEFAULT_SETTINGS_PATH):
        with open(path) as f:
            settings = json.load(f)
        return settings

    @staticmethod
    def get_default_mappings() -> Dict[str, Any]:
        return {
            "properties": {
                "article_id": {
                    "type": "keyword"
                },
                "text": {
                    "type": "text"
                },
            }
        }

    @staticmethod
    def set_shards_in_settings(settings: Dict[str, Any], shards: int = 1, replicas: int = 0) -> Dict[str, Any]:
        settings["number_of_shards"] = shards
        settings["number_of_replicas"] = replicas
        return settings

    def create_index(self, mappings: Dict[str, Any] = None, settings: Dict[str, Any] = None) -> None:
        if not self.elastic_connector.indices.exists(self.index_name):
            body = {
                "mappings": self.get_default_mappings() if mappings is None else mappings,
                "settings": self.get_default_settings() if settings is None else settings,
            }
            return self.elastic_connector.indices.create(self.index_name, body=body, ignore=400)

    def delete_index(self):
        if self.elastic_connector.indices.exists(self.index_name):
            self.elastic_connector.indices.delete(self.index_name, ignore=[400, 404])

    def index_document(self, document: Dict[str, Any]):
        return self.elastic_connector.index(index=self.index_name, document=document)

    def index_all_docs(self, documents: List[Dict[str, Any]], mapping_func: Callable):
        for doc in tqdm(documents):
            self.index_document(mapping_func(doc))

    def default_query(self, query: str, limit=10):
        res = self.elastic_connector.search(
            index=self.index_name,
            size=limit,
            query={
                "multi_match": {
                  "query": query,
                  "fields": ["text"],
                }
            }
        )
        results = [(hit["_source"]) for hit in res['hits']['hits']]
        return results
