import json
from typing import Callable, Union, List, Dict, Any, Tuple
from tqdm.notebook import tqdm


class ExperimentUtil:

    @staticmethod
    def get_dataset_paths(dataset_name: str) -> Tuple[str, str]:
        return {
            'squad_train': (
                '../data/squad_train_all/documents.json',
                '../data/squad_train_all/question_answers.json'
            ),
            'squad_10k': (
                '../data/squad_train_d10k_q1k/documents.json',
                '../data/squad_train_d10k_q1k/question_answers.json'
            ),
            'squad_1k': (
                '../data/squad_dev_d1000_q500/documents.json',
                '../data/squad_dev_d1000_q500/question_answers.json'
            ),
            'swift_ui': (
                '../data/swift-ui-course/documents.json',
                '../data/swift-ui-course/question_answers.json'
            ),
            'swift_additional': (
                '../data/processed/swift-ui-course_additional_fields/documents.json',
                '../data/processed/swift-ui-course_additional_fields/question_answers.json'
            ),
            'squad_10k_additional': (
                '../data/processed/squad_train_d10k_q1k_additional_fields/documents.json',
                '../data/processed/squad_train_d10k_q1k_additional_fields/question_answers.json'
            ),
        }[dataset_name]

    @staticmethod
    def load_dataset(dataset_name: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        documents_path, questions_path = ExperimentUtil.get_dataset_paths(dataset_name)
        with open(documents_path) as json_file:
            document_data = json.load(json_file)
        with open(questions_path) as json_file:
            question_data = json.load(json_file)
        return document_data['documents'], question_data['questions']

    @staticmethod
    def validate(index: str, questions: Dict[str, Any], query_func: Callable, top: int = 10):
        hits_10 = 0
        hits_5 = 0
        hits_3 = 0
        hits_1 = 0
        questions_count = len(questions)
        for question in tqdm(questions):
            expected_docs = question['documents_uuids']
            query = question['question']
            results = query_func(query, limit=top)
            results_ids_10 = [res['article_id'] for res in results]
            results_ids_5 = results_ids_10[:5]
            results_ids_3 = results_ids_10[:3]
            results_ids_1 = results_ids_10[:1]
            hist_list_10 = [expected in results_ids_10 for expected in expected_docs]
            hist_list_5 = [expected in results_ids_5 for expected in expected_docs]
            hist_list_3 = [expected in results_ids_3 for expected in expected_docs]
            hist_list_1 = [expected in results_ids_1 for expected in expected_docs]
            if any(hist_list_10):
                hits_10 += 1
            if any(hist_list_5):
                hits_5 += 1
            if any(hist_list_3):
                hits_3 += 1
            if any(hist_list_1):
                hits_1 += 1
        return {
            "hits@10": hits_10/questions_count,
            "hits@5": hits_5/questions_count,
            "hits@3": hits_3/questions_count,
            "hits@1": hits_1/questions_count,
        }
