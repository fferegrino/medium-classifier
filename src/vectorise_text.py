import pickle
from pathlib import Path

import click
import pandas as pd
import scipy.sparse
from sklearn.feature_extraction.text import CountVectorizer

from tokenisation import tokenize


@click.command()
@click.argument("input-folder", type=click.Path(file_okay=False))
@click.argument("features-folder", type=click.Path(file_okay=False))
@click.argument("vectoriser-folder", type=click.Path(file_okay=False))
@click.option("--max-features", type=int, default=None)
def vectorise_text(input_folder, features_folder, vectoriser_folder, max_features):
    input_folder = Path(input_folder)
    features_folder = Path(features_folder)
    features_folder.mkdir(parents=True, exist_ok=True)
    vectoriser_folder = Path(vectoriser_folder)
    vectoriser_folder.mkdir(parents=True, exist_ok=True)
    vectoriser_file = Path(vectoriser_folder, "text_vectoriser.pkl")

    articles_train = pd.read_csv(input_folder / "train.csv")
    articles_test = pd.read_csv(input_folder / "test.csv")

    def merge_text(data):
        return data["post_title"] + " " + data["post_subtitle"]

    training_text = merge_text(articles_train)
    testing_text = merge_text(articles_test)

    vectorizer = CountVectorizer(
        binary=True, analyzer=tokenize, max_features=max_features
    )

    training_vectors = vectorizer.fit_transform(training_text)
    testing_vectors = vectorizer.transform(testing_text)

    with open(vectoriser_file, "wb") as fin:
        pickle.dump(vectorizer, fin)

    scipy.sparse.save_npz(
        features_folder / "training_text_vectors.npz", training_vectors
    )
    scipy.sparse.save_npz(features_folder / "testing_text_vectors.npz", testing_vectors)


if __name__ == "__main__":
    vectorise_text()
