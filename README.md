# Exam Insights data

Data about past exam questions, for students and teachers who want to run their own analysis. Which topics come up most? Which spec points haven't been examined recently? How many marks are maths skills?

Each course has its own folder in `courses/`.

## AQA A-level Biology (7402)

**Source:** AQA A-level Biology (7402) past papers, 2017 to 2025, Papers 1 to 3. Each question part is tagged with the specification points it assesses.

This dataset is not affiliated with or endorsed by AQA. It contains facts about the questions (year, paper, marks, topic, tags), not the questions themselves. The past papers are on [AQA's website](https://www.aqa.org.uk/subjects/biology/a-level/biology-7402/assessment-resources).

### Files

In `courses/aqa-7402-biology/`:

| File | What's in it |
|---|---|
| `questions.csv` | One row per question part (920 parts, 2565 marks) |
| `spec-points.csv` | Every spec point used in the tags, with its unit and reference number (e.g. 3.1.3) |
| `skills.csv` | The skill codes used in the tags and what type of skill each one is |

**Columns in `questions.csv`:**

| Column | Example | Meaning |
|---|---|---|
| `id` | `256` | A unique number for the question part |
| `year` | `2017` | Exam year |
| `paper` | `1` | Paper 1, 2 or 3 |
| `question` | `1.1` | Question number as printed on the paper |
| `marks` | `3` | Marks available |
| `command_word` | `Describe` | What the question asks you to do (blank for some parts) |
| `unit` | `3.4` | Specification section |
| `topic` | `DNA and protein synthesis` | Topic of the question |
| `spec_points` | `protein-synthesis-transcription; dna-rna-dna-structure` | Content spec points it tests (look them up in `spec-points.csv`) |
| `skills` | `MS 0.3` | Skill codes it tests |

### How the questions are tagged

Each question **part** (e.g. 3.2, not just question 3) is tagged with the specification points it assesses, using the AQA A-level Biology (7402) specification.

- **Content tags** name the spec point, e.g. `lipids-fatty-acids`. `spec-points.csv` lists each one with its name and reference number.
- **Skills tags** use AQA's own skill codes: **MS** (maths skills), **AT** (apparatus and techniques) and **PS** (practical skills), e.g. `MS 0.3` for a percentage calculation. Their full descriptions are in the appendices of the [AQA specification](https://www.aqa.org.uk/subjects/biology/a-level/biology-7402/specification/specification-at-a-glance).
- **A part can have several tags.** 395 of the 920 parts have two or more, e.g. a question on fatty acid structure *and* melting point is tagged with both spec points.
- Tags are based on what the question part asks you to know or do, not just its topic heading. A calculation set in an ecology context gets the ecology spec point *and* the maths skill.

**Not tagged:** the essays (Paper 3, the last question). The titles can draw on almost any part of the specification.

### Disagree with a tag? Retag it

Tagging is a judgement call. Two people can read the same question and link it to different spec points. You're encouraged to check the tags, change them, or add your own. Some ideas:

- Retag a paper yourself, then compare your tags with these. Where you disagree, ask which spec point the mark scheme is really rewarding.
- Add a column for your own tags and see whether it changes which topics look most examined.

If you think a tag is wrong, open an issue on this repo.

### Get started

`analyse.py` counts the question parts and marks for each topic. It needs Python 3 and nothing else:

```
python3 analyse.py
```

Use it as a starting point for your own questions.

### See it on the website

These tags power the **Exam Insights** page on [Random Walker](https://www.arandomwalker.xyz/insights/). It shows which topics come up most, how each one is tested, and common mistakes from the examiner reports. Do your own analysis first, then compare.

## Licence

MIT (see `LICENSE`).
