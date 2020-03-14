import pickle
from pathlib import Path

import click
import pandas as pd
import sklearn.metrics as metrics
from scipy.sparse import load_npz


@click.command()
@click.argument("input-features-folder", type=click.Path(file_okay=False))
@click.argument("input-splits-folder", type=click.Path(file_okay=False))
@click.argument("model", type=click.Path(dir_okay=False))
@click.argument("metrics_file", type=click.Path(dir_okay=False))
def train(input_features_folder, input_splits_folder, model, metrics_file):
    metrics_file = Path(metrics_file)
    metrics_file.parent.mkdir(exist_ok=True, parents=True)
    input_features_folder = Path(input_features_folder)
    input_splits_folder = Path(input_splits_folder)

    with open(model, "rb") as fout:
        model = pickle.load(fout)

    testing_labels = pd.read_csv(input_splits_folder / "test.csv")["topic"]
    testing_vectors = load_npz(input_features_folder / "testing_text_vectors.npz")

    y_pred = model.predict(testing_vectors)

    accuracy = metrics.accuracy_score(testing_labels, y_pred)

    with open(metrics_file, "w") as fd:
        fd.write("{:4f}\n".format(accuracy))


if __name__ == "__main__":
    train()
