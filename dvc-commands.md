This is a file that I maintain myself, just to keep track of what `dvc` commands I have executed, out of my interest of learning the tool.


## Filter the articles

This creates a csv file with unique articles, and their topics well defined

```shell script
dvc run -f filter_by_topic.dvc \
    -d src/filter_by_topic.py -d data/articles_mails.csv \
    -o data/articles_filtered.csv \
    python src/filter_by_topic.py data/articles_mails.csv data/articles_filtered.csv
```
 
## Generate data splits

This splits the data as we want it to be

```shell script
dvc run -f split_data.dvc \
    -d src/split_data.py -d data/articles_filtered.csv \
    -o data/splits/train.csv -o data/splits/test.csv \
    python src/split_data.py data/articles_filtered.csv data/splits/ --stratify
```