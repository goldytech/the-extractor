from typing import List, Tuple

from spacy_text_summary.spacy_singleton import SpacySingleton
from text_summary.text_summary_base import TextSummaryBase


class SpacySummary(TextSummaryBase):
    # def summarize(self, text):
    #     spacy_singleton = SpacySingleton()
    #     doc = spacy_singleton.spacy_nlp(text)
    #     tokens = [token.text for token in doc if token.text not in spacy_singleton.stopwords]
    #     word_frequencies = {}
    #     for token in tokens:
    #         #word_frequencies[token] = 1 if token not in word_frequencies.keys() else word_frequencies[token] =  word_frequencies[token] 1
    #          if token not in word_frequencies.keys():
    #              word_frequencies[token] = 1
    #          else:
    #              word_frequencies[token] +=1

    def get_words_and_sentences(text: str) -> tuple:
        spacy_singleton = SpacySingleton()
        doc = spacy_singleton.spacy_nlp(text)
        sent: str
        sentences = [sent for sent in doc.sents]
        words = [token.text for token in doc if token.text not in spacy_singleton.stopwords and token.is_punct != True]
        words_and_sentences: Tuple[List[str], List[str]] = (words, sentences)
        return words_and_sentences
