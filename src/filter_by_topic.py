import csv

import click

BEST_IN_TEXT = "Best in "
HEADERS = ["post_title", "post_subtitle", "topic"]


REALIGN = {
    "Self": "Health",
    "Mental Health": "Health",
    "Psychology": "Health",
    "Disability": "Health",
    "Fitness": "Health",
    "Race": "Society",
    "Women": "Society",
    "Relationships": "Society",
    "Basic Income": "Society",
    "Religion": "Society",
    "Social Media": "Society",
    "Family": "Society",
    "Immigration": "Politics",
    "Election 2020": "Politics",
    "Art": "Culture",
    "Music": "Culture",
    "History": "Culture",
    "Comics": "Books",
    "Book Excerpts": "Books",
    "Writing": "Poetry-Writing",
    "Poetry": "Poetry-Writing",
    "Film": "Media",
    "TV": "Media",
    "Self-Driving Cars": "Data Science",
    "Machine Learning": "Data Science",
    "Artificial Intelligence": "Data Science",
    "Startups": "Business",
    "Money": "Business",
    "Venture Capital": "Business",
    "Freelancing": "Business",
    "Blockchain": "Cryptocurrency",
    "Neuroscience": "Science",
    "Biotech": "Science",
    "Math": "Science",
    "Makers": "Creativity",
    "Design": "Creativity",
    "Style": "Creativity",
    "World": "Politics-Economy",
    "Economy": "Politics-Economy",
    "Politics": "Politics-Economy",
    "Justice": "Politics-Economy",
    "Gun Control": "Politics-Economy",
    "Digital Life": "Lifestyle",
    "Work": "Lifestyle",
    "Productivity": "Lifestyle",
    "Gadgets": "Technology",
    "Humor": "Genere",
    "True Crime": "Genere",
    "Fiction": "Genere",
    "Transportation": "Cities",
    "Accessibility": "Cities",
    "Visual Design": "UX",
    "Programming": "Software Engineering",
    "Javascript": "Software Engineering",
    "iOS Dev": "Mobile Dev",
    "Android Dev": "Mobile Dev",
    "Spirituality": "Philosophy",
    "Mindfulness": "Philosophy",
    "LGBTQIA": "Sexuality",
    "Privacy": "Cybersecurity",
    "Parenting": "Parenting-Education",
    "Education": "Parenting-Education",
    "Psychedelics": "Drugs",
    "Addiction": "Drugs",
    "Cannabis": "Drugs",
    "Pets": "Environment",
    "Travel": "Environment",
    "Future": "Space-Future",
    "Space": "Space-Future",
    "Sports": "Sports-Outdoors",
    "Outdoors": "Sports-Outdoors",
}


def realign_topic(topic):
    return REALIGN.get(topic, topic)


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
            new_row["topic"] = realign_topic(
                thing["section_title"][len(BEST_IN_TEXT) :]
            )
            writer.writerow(new_row)
            already_seen.add(thing["post_url"])


if __name__ == "__main__":
    filter_by_topic()
