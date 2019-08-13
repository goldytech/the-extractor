from typing import List, Tuple

from spacy_text_summary.spacy_singleton import SpacySingleton
from text_summary.text_summary_base import TextSummaryBase


# Spacy Strategy

class SpacySummary(TextSummaryBase):
    def get_words_and_sentences(text: str) -> tuple:
        spacy_singleton = SpacySingleton()
        doc = spacy_singleton.spacy_nlp(text)
        sent: str
        sentences = [sent for sent in doc.sents]
        words = [token.text for token in doc if token.text not in spacy_singleton.stopwords and token.is_punct != True]
        words_and_sentences: Tuple[List[str], List[str]] = (words, sentences)
        return words_and_sentences
