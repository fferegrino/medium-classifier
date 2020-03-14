from pathlib import Path

import click
import pandas as pd
from sklearn.model_selection import train_test_split


@click.command()
@click.argument("input-file", type=click.Path(dir_okay=False, exists=True))
@click.argument("output-folder", type=click.Path(file_okay=False))
@click.option("--test-size", type=float, default=0.25)
@click.option("--stratify", is_flag=True)
def split_data(input_file, output_folder, test_size, stratify):
    articles_filtered = pd.read_csv(input_file)
    output_folder = Path(output_folder)
    output_folder.mkdir(exist_ok=True, parents=True)
    kwargs = {
        "test_size": test_size,
        "stratify": articles_filtered["topic"] if stratify else None,
    }
    train, test = train_test_split(articles_filtered, **kwargs)

    train.to_csv(Path(output_folder, "train.csv"), index=False)
    test.to_csv(Path(output_folder, "test.csv"), index=False)


if __name__ == "__main__":
    split_data()
