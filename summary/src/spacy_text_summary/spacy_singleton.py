from typing import List

import spacy
from spacy.lang.en import STOP_WORDS

from .singleton_meta import Singleton


class SpacySingleton(metaclass=Singleton):
    doc: object
    stopwords: List[str]

    def __init__(self):
        self.doc = spacy.load('en_core_web_sm')
        self.stopwords = list(STOP_WORDS)
