# Math Through Code

A long-term mathematics learning archive combining formal coursework, handwritten problem solving, computational notebooks, reusable references, and reflective study notes.

The repository has two goals:

1. Preserve evidence of completed mathematics coursework.
2. Build reusable mathematical knowledge and Python utilities for future study in calculus, linear algebra, statistics, data science, artificial intelligence, and graduate-level work.

---

## Repository Architecture

```text
math-through-code/
├── berkeley-ext-calculus-I/
├── berkeley-ext-calculus-II/
├── berkeley-ext-linear-algebra/
├── berkeley-ext-statistics/
├── math-library/
│   ├── knowledge/
│   ├── src/coursework_math/
│   ├── tests/
│   ├── README.md
│   └── pyproject.toml
└── README.md
```

Course directories preserve course-specific learning evidence. The shared library contains reusable knowledge and installable Python utilities.

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

The [`math-library/`](math-library/) directory is an installable subproject that can be used by Calculus II and later course repositories.

It has two distinct responsibilities:

### Knowledge Base

[`math-library/knowledge/`](math-library/knowledge/) contains reusable Markdown references and supporting images, including:

- Algebraic and exponent rules.
- Logarithms and inverse functions.
- Trigonometric identities and unit-circle references.
- Limits and continuity patterns.
- Derivative and antiderivative references.
- Integration strategies and applications.
- Motion and graph-analysis references.

### Python Package

[`math-library/src/coursework_math/`](math-library/src/coursework_math/) contains reusable code for:

- Explicit and implicit equation plotting.
- Point, polyline, and piecewise-function plotting.
- Axis and LaTeX formatting.
- Epsilon-delta visualization.
- Notebook-safe image display.
- Notebook sanitization and PDF export.

Other repositories can install the package locally in editable mode or directly from the GitHub subdirectory. Complete instructions are in the [math-library README](math-library/README.md).

### Promotion Rule

Material begins inside the course where it was learned.

A concept may be promoted into the shared library when it becomes:

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
- Links to relevant shared-library references and package examples.

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

Code is used to strengthen mathematical understanding rather than replace written reasoning.

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
7. Promote reusable material into `math-library/knowledge/` or `coursework_math` when appropriate.
8. Archive official records privately after course completion.

---

## Naming and Maintenance Conventions

- Use descriptive, lowercase directory names.
- Use lowercase, hyphen-separated names for knowledge-base Markdown files.
- Keep generated exports out of version control when the source notebook is tracked.
- Store reusable knowledge images under `math-library/knowledge/images/`.
- Keep reusable Python code under `math-library/src/coursework_math/`.
- Treat the package-level public imports as stable; keep internal helpers private.
- Correct mathematical errors in the source reference rather than adding contradictory notes elsewhere.
- Preserve the distinction between completed work, active study, and planned coursework.

---

## Long-Term Direction

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
