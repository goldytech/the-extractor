import abc


class TextSummaryBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def summarize(self, text):
        pass
