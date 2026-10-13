"""
A starting point: how many question parts and marks each topic has had, 2017 to 2025.

Run it from this folder:  python3 analyse.py
Then change it to answer your own questions, for example:
  - Which topics come up every year?
  - Which spec points (spec-points.csv) have never been tagged?
  - How many marks each year are maths skills (the `skills` column starts with "MS")?
"""
import csv
from collections import Counter

rows = list(csv.DictReader(open("courses/aqa-7402-biology/questions.csv")))

parts = Counter(r["topic"] for r in rows)
marks = Counter()
for r in rows:
    marks[r["topic"]] += int(r["marks"])

print(f"{len(rows)} question parts, {sum(marks.values())} marks\n")
print(f"{'Topic':<45} {'Parts':>5} {'Marks':>5}")
for topic, n in parts.most_common():
    print(f"{topic:<45} {n:>5} {marks[topic]:>5}")
