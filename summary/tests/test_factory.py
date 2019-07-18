import pytest

from nltk_text_summary.nltk_summary import NltkSummary
from spacy_text_summary.spacy_summary import SpacySummary
from text_summary.summary_options import SummaryOptions
from text_summary.text_summary_factory import TextSummaryFactory


@pytest.mark.parametrize("summary_options, expected_instance",
                         [
                             (SummaryOptions.Spacy, SpacySummary),
                             (SummaryOptions.Ntlk, NltkSummary)
                         ])
def test_given_the_summary_options_then_corresponding_instance_must_be_returned(summary_options, expected_instance):
    """
        Defines a test which asserts that correct instance is returned
    """
    summary_factory = TextSummaryFactory(summary_options)
    actual_instance = summary_factory.get_instance
    print(f"The type of spacy instance is {type(expected_instance)}")
    assert type(actual_instance) == type(expected_instance)
