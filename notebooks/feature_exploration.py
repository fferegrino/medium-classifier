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
import matplotlib.pyplot as plt
import seaborn as sns

# %%
articles_filtered = pd.read_csv("../data/articles_filtered.csv")
articles_filtered["topic"] = pd.Categorical(articles_filtered["topic"])

# %%
counts = articles_filtered["topic"].value_counts()
counts.describe()

# %%
for a in counts.items():
    print(a)

# %%
merges = {
    "Self": "Health", "Mental Health": "Health", "Psychology": "Health",
    "Disability": "Health", "Fitness": "Health",
    
    "Race": "Society", "Women": "Society", "Relationships": "Society",
    "Basic Income": "Society", "Religion": "Society", "Social Media": "Society",
    "Family": "Society",
    
    "Immigration": "Politics", "Election 2020": "Politics",
    
    "Art":"Culture", "Music": "Culture", "History": "Culture",
    
    "Comics": "Books", "Book Excerpts": "Books",
    
    "Writing":"Poetry-Writing", "Poetry": "Poetry-Writing",
    
    "Film": "Media", "TV": "Media",
    
    "Self-Driving Cars": "Data Science",
    "Machine Learning": "Data Science",
    "Artificial Intelligence": "Data Science",
    
    "Startups": "Business", "Money": "Business",
    "Venture Capital": "Business", "Freelancing": "Business",
    
    "Blockchain": "Cryptocurrency",
    
    "Neuroscience":"Science", "Biotech": "Science", "Math": "Science",
    
    "Makers": "Creativity", "Design": "Creativity", "Style": "Creativity",
    
    "World": "Politics-Economy", "Economy": "Politics-Economy", "Politics": "Politics-Economy",
    "Justice": "Politics-Economy", "Gun Control":  "Politics-Economy", 
    
    "Digital Life": "Lifestyle", "Work": "Lifestyle", "Productivity": "Lifestyle",
    
    "Gadgets": "Technology",
    
    "Humor": "Genere",
    "True Crime": "Genere",
    "Fiction": "Genere",
    
    "Transportation": "Cities", "Accessibility": "Cities",
    
    "Visual Design": "UX",
    
    "Programming": "Software Engineering","Javascript": "Software Engineering",
    "iOS Dev": "Mobile Dev", "Android Dev": "Mobile Dev",
    
    "Spirituality": "Philosophy", "Mindfulness": "Philosophy",
    
    "LGBTQIA": "Sexuality",
    
    "Privacy": "Cybersecurity",
    
    "Parenting": "Parenting-Education", "Education": "Parenting-Education",
    
    "Psychedelics":"Drugs", "Addiction": "Drugs", "Cannabis": "Drugs",
    
    "Pets": "Environment", "Travel": "Environment",
    
    "Future": "Space-Future", "Space": "Space-Future",
    
    "Sports": "Sports-Outdoors", "Outdoors": "Sports-Outdoors",
    
}

def realign_topic(topic):
    return merges.get(topic, topic)


# %%
articles_filtered["realigned_topic"] = articles_filtered["topic"].apply(realign_topic)
articles_filtered["realigned_topic"].value_counts()

# %%
fig = plt.figure(figsize=(20, 10))
ax = fig.gca()
ax = sns.countplot(x="realigned_topic", data=articles_filtered, ax=ax)

# %%
