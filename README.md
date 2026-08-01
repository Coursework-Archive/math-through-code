# Math Through Code

A long-term mathematics learning archive that combines formal coursework, handwritten problem solving, computational notebooks, reusable reference material, and reflective study notes.

The repository is organized around two goals:

1. Preserve evidence of completed mathematics coursework.
2. Build a reusable mathematics library that supports future study in calculus, linear algebra, statistics, data science, artificial intelligence, and graduate-level work.

---

## Repository Architecture

```text
math-through-code/
├── berkeley-ext-calculus-I/
│   ├── handwritten/
│   ├── notebooks/
│   ├── exam-prep/
│   ├── reflections/
│   └── README.md
├── berkeley-ext-calculus-II/
│   ├── handwritten/
│   ├── notebooks/
│   ├── exam-prep/
│   ├── reflections/
│   └── README.md
├── berkeley-ext-linear-algebra/
├── berkeley-ext-statistics/
├── math-library/
└── README.md
```

The structure separates course-specific evidence from reusable mathematical knowledge.

---

## Course Archives

Each course directory records the learning process for one formal course.

Course folders may contain:

- Handwritten assignments and worked solutions.
- Jupyter notebooks used to verify, explore, or visualize concepts.
- Midterm and final exam preparation.
- Error logs and pattern-recognition notes.
- Course timelines and assignment trackers.
- Reflections on progress, difficulties, and lessons learned.
- References to privately archived official records.

### Current and Planned Courses

| Course Area | Directory | Status |
|---|---|---|
| UC Berkeley Extension Calculus I | [`berkeley-ext-calculus-I/`](berkeley-ext-calculus-I/) | Completed |
| UC Berkeley Extension Calculus II | [`berkeley-ext-calculus-II/`](berkeley-ext-calculus-II/) | Planned / In Progress |
| UC Berkeley Extension Linear Algebra | [`berkeley-ext-linear-algebra/`](berkeley-ext-linear-algebra/) | Planned |
| UC Berkeley Extension Statistics | [`berkeley-ext-statistics/`](berkeley-ext-statistics/) | Planned |

Additional mathematics coursework may be added as the academic plan develops through 2027 and beyond.

---

## Shared Math Library

The [`math-library/`](math-library/) directory contains material that is useful across multiple courses.

Examples include:

- Algebraic and exponent rules.
- Logarithms and inverse functions.
- Trigonometric identities and unit-circle references.
- Limits and continuity patterns.
- Derivative and antiderivative references.
- Integration strategies and applications.
- Motion and graph-analysis references.
- Plotting and visualization helpers.
- Notebook export and image utilities.

### Promotion Rule

Material begins inside the course where it was learned.

A concept may be promoted into `math-library/` when it becomes:

- Correctly verified.
- General enough to apply outside one assignment.
- Useful in more than one course.
- Organized as a reusable explanation, formula reference, decision rule, or computational helper.

Course-specific schedules, exam dates, instructor feedback, assignment answers, and personal study logs remain inside the applicable course directory.

---

## Standard Course Structure

New course directories should generally follow this pattern:

```text
course-name/
├── handwritten/
│   ├── assignments/
│   ├── midterm/
│   └── final/
├── notebooks/
├── exam-prep/
├── reflections/
└── README.md
```

Not every course must use every directory. The structure can be adjusted when the course format requires it.

### Course README Expectations

Each course README should document:

- Course title and number.
- Units and prerequisites.
- Required textbook or resources.
- Official module or topic sequence.
- Assignment and exam tracker.
- Grading structure.
- Enrollment and completion timeline.
- Study workflow.
- Reflection workflow.
- Links to relevant shared-library references.

---

## Public and Private Record Boundary

This public repository contains original learning artifacts, including:

- Personal notes and reflections.
- Original code and notebooks.
- Handwritten problem-solving work where appropriate.
- Study guides and error logs.
- Reusable mathematical references.

Official academic records are archived privately and are not committed to this repository.

Private records include:

- Official syllabi when redistribution is restricted.
- Final grades and achievement reports.
- Official transcripts.
- Instructor communications.
- Personally identifying or account-related documents.

For every completed course, the private archive should retain:

1. The syllabus.
2. The final grade or achievement report.
3. The official transcript when available.
4. A short personal reflection.

---

## Computational Learning Approach

The repository uses code to strengthen mathematical understanding rather than replace written reasoning.

Computational work may be used to:

- Verify symbolic or numerical results.
- Plot functions and geometric regions.
- Explore parameter changes.
- Compare exact and approximate methods.
- Test convergence behavior.
- Simulate statistical processes.
- Translate mathematical ideas into executable Python.

Written derivations remain important because the goal is to understand both the mathematics and its computational representation.

---

## Study and Documentation Workflow

A typical learning cycle is:

1. Review the assigned concept and examples.
2. Solve representative problems by hand.
3. Record mistakes and recognition patterns.
4. Use code to verify or visualize selected results.
5. Review instructor feedback.
6. Write a brief reflection.
7. Promote reusable material into `math-library/` when appropriate.
8. Archive official records privately after course completion.

---

## Naming and Maintenance Conventions

- Use descriptive, lowercase directory names.
- Prefer Markdown for reusable references and reflections.
- Keep generated exports out of version control when the source notebook or document is already tracked.
- Store shared images under `math-library/images/` unless they are course-specific.
- Keep reusable utilities under `math-library/tools/` or another clearly named shared directory.
- Correct mathematical errors in the source reference rather than adding contradictory notes elsewhere.
- Preserve the distinction between completed work, active study, and planned coursework.

---

## Long-Term Direction

This repository is intended to show the development of mathematical maturity over time.

The progression is expected to move through:

- Calculus I and II.
- Linear algebra.
- Probability and statistics.
- Discrete and computational mathematics where useful.
- Mathematical foundations for machine learning and artificial intelligence.
- Graduate-level preparation and future Berkeley coursework.

The aim is not simply to collect assignments. The aim is to build a coherent, searchable record of how mathematical understanding developed and how that understanding can be applied through code.

---

_Last updated: August 2026_
