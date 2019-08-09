import pytest

from nltk_text_summary.nltk_summary import NltkSummary
from spacy_text_summary.spacy_singleton import SpacySingleton
from spacy_text_summary.spacy_summary import SpacySummary
from text_summary.summary import summarize
from text_summary.summary_options import NlpEngines
from text_summary.text_summary_factory import TextSummaryFactory


@pytest.mark.parametrize("summary_options, expected_instance",
                         [
                             (NlpEngines.Spacy, SpacySummary),
                             (NlpEngines.Ntlk, NltkSummary)
                         ])
def test_given_the_summary_options_then_corresponding_instance_must_be_returned(summary_options, expected_instance):
    """
        Defines a test which asserts that correct instance is returned
    """
    summary_factory = TextSummaryFactory(summary_options)
    actual_instance = summary_factory.get_instance
    print(f"The type of spacy instance is {type(expected_instance)}")
    assert type(actual_instance) == type(expected_instance)


def test_given_when_spacy_instance_already_exists_then_new_instance_should_not_be_created():
    instance1 = SpacySingleton()
    instance2 = SpacySingleton()
    assert instance1 == instance2


@pytest.mark.parametrize("nlp_engine",
                         [
                             (NlpEngines.Spacy),
                             (NlpEngines.Ntlk)
                         ])
def test_summarize_function_for_given_nlp_engines(nlp_engine):
    text = "Nearly all applicants for US visas will have to submit their social media details under new rules by the " \
           "State Department.The State Department regulations say people will have to submit social media names and " \
           "five years' worth of email addresses and phone numbers.When proposed last year, authorities estimated the " \
           "proposal would affect 14.7 million people annually. Certain diplomatic and official visa applicants will " \
           "be exempt from the stringent new measures.However, people travelling to the US to work or to study will " \
           "have to hand over their information, the BBC reported.We are constantly working to find mechanisms to " \
           "improve our screening processes to protect US citizens, while supporting legitimate travel to the United " \
           "States,the department reportedly said.Previously, only applicants who needed additional vetting - such as " \
           "people who had been to parts of the world controlled by terrorist groups - would need to hand over this " \
           "data.But now applicants will have to give up their account names on a list of social media platforms, " \
           "and also volunteer the details of their accounts on any sites not listed.Anyone who lies about their " \
           "social media use could face serious immigration consequences, according to an official.The Trump " \
           "administration first proposed the rules in March 2018.At the time, the American Civil Liberties Union - a " \
           "civil rights group - said there is no evidence that such social media monitoring is effective or fair, " \
           "and said it would cause people to self-censor themselves online.US President Donald Trump made cracking " \
           "down on immigration a key plank of his election campaign in 2016.He called for extreme vetting of " \
           "immigrants before and during his time in office."

    summarize_result = summarize(text, 3, nlp_engine)
    expected_summarize_result = ['Nearly all applicants for US visas will have to submit their social media details '
                                 'under new rules by the State Department.',
                                 'The State Department regulations say people will have to submit social media names '
                                 'and five years'' worth of email addresses and phone numbers.',
                                 'The Trump administration first proposed the rules in March 2018.At the time the '
                                 'American Civil Liberties Union - a civil rights group - said there is no evidence '
                                 'that such social media monitoring is effective or fair and said it would cause '
                                 'people to self-censor themselves online.']

    assert len(summarize_result) == 3



