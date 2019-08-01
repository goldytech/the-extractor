import abc


class TextSummaryBase(metaclass=abc.ABCMeta):

    # @abc.abstractmethod
    # def summarize(self, text):
    #     pass

    @abc.abstractmethod
    def get_words_and_sentences(text: str) -> tuple:
        return [], []
