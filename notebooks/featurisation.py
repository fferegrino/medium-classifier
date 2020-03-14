# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords
from string import punctuation
import unidecode


from pathlib import Path

input_folder = Path("../data/splits/")

# %%
tokenizer = TweetTokenizer()
stemmer = PorterStemmer()
stop_words = set(punctuation) | set(stopwords.words('english'))

def contains_digit(token):
    return any((char.isdigit() for char in token))

def tokenize(text):
    new_tokens = []
    if not isinstance(text, str):
        return new_tokens
    tokens = [stemmer.stem(unidecode.unidecode(token).casefold()) for token in tokenizer.tokenize(text)]
    for token in tokens:
        if token in stop_words:
            continue
        if contains_digit(token):
            continue
        new_tokens.append(token)
    return new_tokens



# %%
articles_train = pd.read_csv(input_folder / "train.csv")
articles_test = pd.read_csv(input_folder / "test.csv")
articles_test.head()

# %%
vectorizer = CountVectorizer(binary=True, analyzer=tokenize)

# %%
all_text = articles_train["post_title"] + " " + articles_train["post_subtitle"]

# %%
vect = vectorizer.fit_transform(all_text)

# %%
articles_test.head()

# %%

# %%
vect

# %%
