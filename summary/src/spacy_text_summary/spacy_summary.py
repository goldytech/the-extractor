from text_summary.text_summary_base import TextSummaryBase


class SpacySummary(TextSummaryBase):
    def summarize(self, text):
        return 'from SpaCy'
