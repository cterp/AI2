import glob
import os
import re

from collections import Counter
from decimal import *
from prettytable import PrettyTable

getcontext().prec = 8  # set the precision desired for Decimals


"""
This program takes as input a list of words and assumes there are text files in
the same directory. Returns the document with the highest term frequency (TF)
score for each word and the TF score for that word in that document.

A TF score is computed for each word w_i in each document d_j by computing the
frequency of that word in that document. The formula is given by:
TF(w_i, d_j) = (number of times w_i occurs in d_j) / (number of words in d_j).
"""


def tokens(text):
    """
    Given an input string, this function removes punctuation,
    converts all characters to lowercase, and splits words by whitespace.

    For example, tokens("Hello! This is a sentence.") returns:
    ['hello', 'this', 'is', 'a', 'sentence']

    :param text: String to tokenize
    :return: List of tokenized words
    """
    return re.findall('[a-z]+', text.lower())


def text_files_in_cwd():
    """
    Returns a list of text files (filenames only, not their full paths) in
    the current working directory.

    :return: List of text files in current working directory
    """
    cwd = os.getcwd() + "/*.txt"
    file_list = glob.glob(cwd)
    return [os.path.basename(file) for file in file_list]


# preliminary stuff: read in from files
def import_counts():
    """
    Stores word count data by document in a dictionary. Text files in the
    current working directory are read in as strings, tokenized, and then
    its words are counted.

    Word count data is represented by a Counter object, whose keys are words
    appearing in the document and values are the counts of that word.

    :return: Dictionary of Counter objects keyed by filename. For example:
    {'mobydick-chapter1.txt': Counter({'the': 124, 'of': 81, ...}) ...}
    """
    data = {}
    files = text_files_in_cwd()
    for file in files:
        with open(file, 'r') as f:  # shorthand for try-finally blocks
            data[file] = Counter(tokens(f.read()))

    return data


def term_frequency(words):
    """
    Takes as input a list of words, and using the set of documents in the
    current working directory, computes term frequency scores for each given
    word in each document. For a usage example see the main() function.

    :param words: List of words for which to compute maximum term
    frequency scores
    :return: Prints to console the maximum term frequency and corresponding
    document for each word in the given list
    """
    counts = import_counts()
    scores = {}
    if not len(words):
        print("Please supply a list of words!")
        return

    for word in words:
        scores[word] = {}
        for doc in text_files_in_cwd():
            filename = os.path.basename(doc)
            word_count_in_document = Decimal(counts[filename][word])
            words_in_document = Decimal(sum(counts[filename].values()))
            scores[word][filename] = word_count_in_document / words_in_document

    find_highest_tfs_and_print(scores)


def find_highest_tfs_and_print(scores):
    """
    For each word, finds the document for which the word has the highest term
    frequency score. Prints the word, document name, and the word's term
    frequency score in that document.

    :param scores: Dictionary containing term frequencies across all documents
    for a given word. Keys are words, and values are dictionaries that map
    filenames to term frequency scores. For example:
        {'queequeg': {'mobydick-chapter1.txt': Decimal('0'),
        'mobydick-chapter3.txt': Decimal('0.00066844920')}
    """
    t = PrettyTable(['word', 'document', 'term frequency score'])  # table header
    for word in scores.keys():
        # find highest score and corresponding document for the given word
        highest = max(scores[word].items(), key=lambda x: x[1])
        t.add_row([word, highest[0], highest[1]])  # word, document, score

    print(t)


def main():
    term_frequency(['queequeg', 'whale', 'sea'])


if __name__ == "__main__":
    main()
