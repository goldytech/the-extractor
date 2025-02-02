from nltk_text_summary.nltk_summary import NltkSummary
from spacy_text_summary.spacy_summary import SpacySummary
from .summary_options import NlpEngines
from .text_summary_base import TextSummaryBase


class TextSummaryFactory:
    def __init__(self, summary_options: NlpEngines):
        """

        :type summary_options: NlpEngines
        """
        self.summary_options = summary_options

    @property
    def get_instance(self) -> TextSummaryBase:
        if self.summary_options == NlpEngines.Ntlk:
            return NltkSummary
        if self.summary_options == NlpEngines.Spacy:
            return SpacySummary
