# Exam Insights Data

Data about past exam questions, for students and teachers who want to run their own analysis. Which topics come up most? Which spec points haven't been examined recently?

Note: This does NOT include any of the question, mark scheme, or examiner report material. It's just the question reference, tagged with topic/spec point and type of question.

Each course has its own folder in `courses/`.

## AQA A-level Biology (7402)

**Source:** AQA A-level Biology (7402) past papers, 2017 to 2025, Papers 1 to 3. Each question part is tagged with the specification points it assesses.

This dataset is not affiliated with or endorsed by AQA.

### The data

**[`questions.csv`](courses/aqa-7402-biology/questions.csv) is the data:** one row per question part (920 parts, 2565 marks). Open it in Excel, Google Sheets or any analysis tool.

**[Download questions.csv](https://raw.githubusercontent.com/VickyFouhy/exam_insights_data_public/main/courses/aqa-7402-biology/questions.csv)**, or click **Code → Download ZIP** at the top of this page for all the files.

The other two files are lookup tables for the tags:

| File | What it's for |
|---|---|
| [`spec-points.csv`](courses/aqa-7402-biology/spec-points.csv) | Turns a spec point tag (e.g. `lipids-fatty-acids`) into its name, unit and reference number (e.g. 3.1.3) |
| [`skills.csv`](courses/aqa-7402-biology/skills.csv) | Says what type of skill each skill code is (e.g. `MS 0.3` is a maths skill) |

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
- **Skills tags** use AQA's own skill codes: **MS** (maths skills), **AT** (apparatus and techniques) and **PS** (practical skills), e.g. `MS 0.3` for a percentage calculation. Their full descriptions are in the appendices of the AQA specification.
- **A part can have several tags.** 395 of the 920 parts have two or more, e.g. a question on fatty acid structure *and* melting point is tagged with both spec points.
- Tags are based on what the question part asks you to know or do, not just its topic heading. A calculation set in an ecology context gets the ecology spec point *and* the maths skill.

**Not tagged:** the essays (Paper 3, the last question). The titles can draw on almost any part of the specification.

### Disagree with a tag? Retag it

Tagging is a judgement call. Two people can read the same question and link it to different spec points. The reason for providing this data here is that you are encouraged to check the tags, change them, or add your own.

If you think a tag is wrong, open an issue on this repo.

### See it on the website

These tags power the **Exam Insights** page on [Random Walker](https://www.arandomwalker.xyz/insights/). It shows which topics come up most, how each one is tested, and common mistakes from the examiner reports. Do your own analysis first, then compare.

## Licence

MIT (see `LICENSE`).
