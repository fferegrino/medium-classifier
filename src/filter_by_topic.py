import csv

import click

BEST_IN_TEXT = "Best in "
HEADERS = ["post_title", "post_subtitle", "topic"]


@click.command()
@click.argument("input-file", type=click.Path(dir_okay=False, exists=True))
@click.argument("output-file", type=click.Path(dir_okay=False, exists=False))
def filter_by_topic(input_file, output_file):
    already_seen = set()
    with open(input_file) as readable, open(output_file, "w") as writable:
        reader = csv.DictReader(readable)
        writer = csv.DictWriter(writable, fieldnames=HEADERS)
        writer.writeheader()
        for thing in reader:
            if thing["post_url"] in already_seen:
                continue
            if not thing["section_title"].startswith(BEST_IN_TEXT):
                continue

            new_row = {header: thing.get(header) for header in HEADERS}
            new_row["topic"] = thing["section_title"][len(BEST_IN_TEXT) :]
            writer.writerow(new_row)
            already_seen.add(thing["post_url"])


if __name__ == "__main__":
    filter_by_topic()
