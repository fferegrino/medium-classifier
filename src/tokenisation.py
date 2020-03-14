from string import punctuation

import unidecode
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

tokenizer = TweetTokenizer()
stemmer = PorterStemmer()
stop_words = set(punctuation) | set(stopwords.words("english"))


def contains_digit(token):
    return any((char.isdigit() for char in token))


def tokenize(text):
    new_tokens = []
    if not isinstance(text, str):
        return new_tokens
    tokens = [
        stemmer.stem(unidecode.unidecode(token).casefold())
        for token in tokenizer.tokenize(text)
    ]
    for token in tokens:
        if token in stop_words:
            continue
        if contains_digit(token):
            continue
        new_tokens.append(token)
    return new_tokens
