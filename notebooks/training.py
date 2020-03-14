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
from sklearn.svm import LinearSVC
from pathlib import Path
from scipy.sparse import load_npz
import pandas as pd

# %%
input_features_folder = "../data/features"
input_splits_folder = "../data/splits/"
model_output_folder = 

input_features_folder = Path(input_features_folder)
input_splits_folder = Path(input_splits_folder)

# %%
training_labels = pd.read_csv(input_splits_folder / "train.csv")["topic"]
training_vectors = load_npz(input_features_folder / "training_text_vectors.npz")

# %%
classifier = LinearSVC()
classifier.fit(training_vectors, training_labels)

# %%
