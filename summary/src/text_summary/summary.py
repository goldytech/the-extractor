import re
from collections import Counter, defaultdict
from heapq import nlargest
from typing import List

from text_summary.summary_options import SummaryOptions
from text_summary.text_summary_base import TextSummaryBase
from text_summary.text_summary_factory import TextSummaryFactory


def summarize(text_to_be_summarized: str, nlp_engine: SummaryOptions, size_of_summary) -> List[str]:
    """

    :param size_of_summary: int
    :return: List[str]
    :param text_to_be_summarized: str
    :type nlp_engine: SummaryOptions
    """
    nlp_factory = TextSummaryFactory(nlp_engine)
    nlp_instance: TextSummaryBase = nlp_factory.get_instance
    words: List[str]
    sentences: List[str]
    (words, sentences) = nlp_instance.get_words_and_sentences(text=text_to_be_summarized)
    words_frequency: Counter[str] = Counter(words)
    ranking = defaultdict(int)
    for i, sent in enumerate(sentences):
        w: object
        for w in re.findall(r"\w+", sent.text):
            if w in words_frequency:
                ranking[i] += words_frequency[w]

    sentences_index = nlargest(size_of_summary, ranking, key=ranking.get)
    return [sentences[j] for j in sorted(sentences_index)]



