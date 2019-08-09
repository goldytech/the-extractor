from string import punctuation
from typing import List, Tuple

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

from text_summary.text_summary_base import TextSummaryBase


class NltkSummary(TextSummaryBase):
    def get_words_and_sentences(text: str) -> tuple:
        sentences = sent_tokenize(text)
        words = word_tokenize(text.lower())
        _stopwords = set(stopwords.words('english') + list(punctuation))
        words_without_stopwords = [word for word in words if word not in _stopwords]
        words_and_sentences: Tuple[List[str], List[str]] = (words_without_stopwords, sentences)
        return words_and_sentences
