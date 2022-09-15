from typing import Dict, Any


class ScoringUtil:

    @staticmethod
    def set_similarity(settings: Dict[Any, str], similarity_function_name: str = 'bm25') -> None:
        return {
            'bm25': lambda settings: ScoringUtil.set_bm25_similarity(settings),
            'dfr': lambda settings: ScoringUtil.set_dfr_similarity(settings),
            'dfi': lambda settings: ScoringUtil.set_dfi_similarity(settings),
            'tfidf': lambda settings: ScoringUtil.set_tfidf_similarity(settings),
            'ib': lambda settings: ScoringUtil.set_ib_similarity(settings),
            'lm_d': lambda settings: ScoringUtil.set_lm_dirichlet_similarity(settings),
            'lm_jm': lambda settings: ScoringUtil.set_lm_jelinek_mercer_similarity(settings),
        }[similarity_function_name](settings)

    @staticmethod
    def set_bm25_similarity(settings: Dict[str, Any], b: float = 0.75, k1: float = 1.2) -> None:
        settings["index"] = {
          "similarity": {
              "default": {
                "type": "BM25",
                "b": 0.75,
                "k1": 1.2
              }
          }
        }

    @staticmethod
    def set_dfr_similarity(settings: Dict[str, Any]) -> None:
        settings["index"] = {
          "similarity": {
              "default": {
                  "type": "DFR",
                  "basic_model": "g",
                  "after_effect": "l",
                  "normalization": "h2",
                  "normalization.h2.c": "3.0"
              }
          }
        }

    @staticmethod
    def set_dfi_similarity(settings: Dict[str, Any]) -> None:
        settings["index"] = {
          "similarity": {
              "default": {
                  "type": "DFI",
              }
          }
        }

    @staticmethod
    def set_ib_similarity(settings: Dict[str, Any]) -> None:
        settings["index"] = {
          "similarity": {
              "default": {
                  "type": "DFI",
              }
          }
        }

    @staticmethod
    def set_lm_dirichlet_similarity(settings: Dict[str, Any]) -> None:
        settings["index"] = {
          "similarity": {
              "default": {
                  "type": "LMDirichlet",
              }
          }
        }

    @staticmethod
    def set_lm_jelinek_mercer_similarity(settings: Dict[str, Any]) -> None:
        print('jm')
        settings["index"] = {
          "similarity": {
              "default": {
                  "type": "LMJelinekMercer",
              }
          }
        }

    @staticmethod
    def set_tfidf_similarity(settings: Dict[str, Any]) -> None:
        settings["index"] = {
          "similarity": {
              "default": {
                    "type": "scripted",
                    "script": {
                      "source": "double tf = Math.sqrt(doc.freq); double idf = Math.log((field.docCount+1.0)/(term.docFreq+1.0)) + 1.0; double norm = 1/Math.sqrt(doc.length); return query.boost * tf * idf * norm;"
                    }
              }
          }
        }
