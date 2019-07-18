from text_summary.text_summary_base import TextSummaryBase


class NltkSummary(TextSummaryBase):
    def summarize(self, text):
        return "from nltk"
