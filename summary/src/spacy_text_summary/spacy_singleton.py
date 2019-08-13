from typing import List

import spacy
from spacy.lang.en import STOP_WORDS

from .singleton_meta import Singleton


# Singleton class of Spacy
class SpacySingleton(metaclass=Singleton):
    spacy_nlp: object
    stopwords: List[str]

    def __init__(self):
        self.spacy_nlp = spacy.load('en_core_web_sm')
        self.stopwords = list(STOP_WORDS)
