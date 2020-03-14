import pickle
from pathlib import Path

import click
import pandas as pd
from scipy.sparse import load_npz
from sklearn.svm import LinearSVC


@click.command()
@click.argument("input-features-folder", type=click.Path(file_okay=False))
@click.argument("input-splits-folder", type=click.Path(file_okay=False))
@click.argument("model-folder", type=click.Path(file_okay=False))
def train(input_features_folder, input_splits_folder, model_folder):
    input_features_folder = Path(input_features_folder)
    input_splits_folder = Path(input_splits_folder)
    model_folder = Path(model_folder)

    training_labels = pd.read_csv(input_splits_folder / "train.csv")["topic"]
    training_vectors = load_npz(input_features_folder / "training_text_vectors.npz")

    classifier = LinearSVC()
    classifier.fit(training_vectors, training_labels)

    with open(model_folder / "medium-predictor.pkl", "wb") as fin:
        pickle.dump(classifier, fin)


if __name__ == "__main__":
    train()
