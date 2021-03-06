import io
import re

from collections import Counter

FILE_PATH = r'.\multiverse.txt'
REGULAR_EXPRESS = r'[A-Za-z]+'


class WordFrequencyStatistics(object):
    def __init__(self, file, regex):
        """
        Generate a tuple, its first element is a word, the second is its appear times.

        :param file: File path from global variable FILE_PATH, make sure the file encoding is utf-8.
        :param regex: Regular express from global variable REGULAR_EXPRESS.
        """
        self.file = file
        self.regex = regex

        with io.open(self.file, encoding='utf-8') as f:
            # use io.open instead of open which is only functional in Python 3.
            data = f.read()
            word_list = [single.lower() for single in re.findall(self.regex, data)]

            # Define a dictionary, key-value: <word>-<times>.
            statistics_dict = dict()

            # Iterate word_list to see if there's a match word, if match failed create a key-value pairs
            # as <word>-0 in statistics_dict, otherwise make its times plus 1.
            for word in word_list:
                statistics_dict[word] = statistics_dict.get(word, 0) + 1
            self.mapping = statistics_dict

    def sort_mapping(self, n=5):
        """
        Return first <n> words of the sorted tuple.

        :param n: How many words should be return, default 5.
        """
        counter = Counter(self.mapping)
        return counter.most_common(n)


if __name__ == '__main__':
    statistics = WordFrequencyStatistics(FILE_PATH, REGULAR_EXPRESS)
    result = statistics.sort_mapping()
    for item in result:
        print(item)
