# Math X12 (Calculus II)

This repository contains handwritten coursework, computational explorations,
exam-preparation materials, references, and reflections for **UC Berkeley Extension
MATH X12: Calculus II**.

Calculus II builds on limits, derivatives, integration, and the Fundamental Theorem
of Calculus from Calculus I. The course emphasizes methods of integration,
applications of integration, sequences and infinite series, power series, and
differential equations.

## Repository Structure

```text
.
├── handwritten/
│   ├── assignments/
│   ├── midterm/
│   └── final/
├── notebooks/
├── exam-prep/
├── reflections/
└── README.md
```

> Official course documents, the syllabus, achievement report, final grade, and
> transcripts are archived privately in Google Drive. This repository contains
> original coursework, study materials, code, and reflections.

---

## Course Information

- **Course:** Calculus II
- **Course Number:** MATH X12
- **Units:** 4 semester units
- **Prerequisite:** MATH X11 Calculus I or equivalent
- **Format:** Continuous enrollment / online
- **Completion Window:** 180 days from enrollment
- **Required Text:** *Calculus: Early Transcendentals*, James Stewart, 8th edition

## Learning Goals

By the end of the course, the goal is to be able to:

- Apply the major methods of integration.
- Use integrals to calculate arc length and surface area.
- Analyze sequences and infinite series.
- Apply convergence tests and estimate approximation error.
- Represent analytic functions with power series.
- Solve first- and second-order differential equations.
- Interpret differential equations in applied settings.
- Explain relationships among infinite series, functions, and differential equations.

---

# Assignment and Exam Tracker

## Modules 1–6: Integration and Beginning Series

| Module / Exam | Official Topic | Text Sections | Status |
|---|---|---:|---|
| Module 1 | Integration by Parts, Trigonometric Integrals, and Trigonometric Substitution | 7.1–7.3 | ⬜ Not Started |
| Module 2 | Partial Fractions and Strategies for Integration | 7.4–7.5 | ⬜ Not Started |
| Module 3 | Integration Tables, Approximate Integration, and Improper Integrals | 7.6–7.8 | ⬜ Not Started |
| Module 4 | Arc Length and Areas | 8.1–8.2 | ⬜ Not Started |
| Module 5 | Sequences and Series | 11.1–11.2 | ⬜ Not Started |
| Module 6 | Integral Test, Comparison Tests, and Alternating Series | 11.3–11.5 | ⬜ Not Started |
| **Midterm Exam** | **Modules 1–6** | **Comprehensive through Module 6** | ⬜ Not Started |

## Modules 7–12: Power Series and Differential Equations

| Module / Exam | Official Topic | Text Sections | Status |
|---|---|---:|---|
| Module 7 | Ratio and Root Tests, Strategies, and Power Series | 11.6–11.8 | ⬜ Not Started |
| Module 8 | Representing Functions as Power Series | 11.9–11.11 | ⬜ Not Started |
| Module 9 | Differential Equations: Models, Direction Fields, and Separable Equations | 9.1–9.3 | ⬜ Not Started |
| Module 10 | Models for Population Growth, Linear Equations, and Predator-Prey Systems | 9.4–9.6 | ⬜ Not Started |
| Module 11 | Second-Order Linear Equations and Nonhomogeneous Linear Equations | 17.1–17.2 | ⬜ Not Started |
| Module 12 | Applications and Series Solutions | 17.3–17.4 | ⬜ Not Started |
| **Final Exam** | **Comprehensive Modules 1–12** | **All assigned material** | ⬜ Not Started |

---

## Exam Requirements

### Midterm Exam

- Covers Modules 1–6.
- One-hour online exam.
- Open book and open notes.
- A non-programmable, non-graphing scientific calculator is permitted.
- Complete and receive grades for Modules 1–6 before taking the exam.
- Recommended minimum enrollment period: 45 days.
- Must be completed before the final exam and before the course end date.

### Final Exam

- Comprehensive across Modules 1–12.
- Two-hour online exam.
- Open book and open notes.
- A non-programmable, non-graphing scientific calculator is permitted.
- All assignments must be completed, graded, and returned first.
- Minimum enrollment period: 90 days.
- Must be completed on or before the 180-day course end date.
- A final-exam score of **70% or higher is required to pass the course**.

---

## Grading

| Category | Weight |
|---|---:|
| Written Assignments | 40% |
| Midterm Exam | 30% |
| Final Exam | 30% |

```text
Course Grade = (Assignment Average × 0.40)
             + (Midterm Exam × 0.30)
             + (Final Exam × 0.30)
```

> A calculated passing average does not override the final-exam requirement.
> A final-exam score below 70% results in a failing course grade.

---

## Course Timeline

- **Enrollment Date:** TBD
- **45-Day Midterm Eligibility Date:** TBD
- **90-Day Final Eligibility Date:** TBD
- **Course Completion Deadline:** TBD
- **Target Midterm Date:** TBD
- **Target Final Exam Date:** TBD

The final exam should be scheduled with enough time for instructor approval,
completion, grading, and unexpected delays before the course end date.

---

## Study Workflow

For each module:

1. Watch the module introduction.
2. Review the assigned textbook sections.
3. Watch the corresponding video lectures.
4. Read the module commentary and work through its examples.
5. Complete the assigned problems by hand.
6. Ask questions before submitting the assignment.
7. Submit one combined PDF for the module.
8. Wait for the assignment to be graded before submitting the next module.
9. Review instructor feedback and record recurring mistakes.
10. Add reusable ideas, formulas, or verification tools to the appropriate reference area.

## Reflection Workflow

After each module, record:

- Topics learned.
- Problems or concepts that required the most effort.
- Algebra or Calculus I skills that needed review.
- Mistakes identified through instructor feedback.
- Computational tools or notebooks created.
- Concepts that may be reusable in the future shared math library.

---

## Planned Shared Math Library Integration

Reusable material will eventually be promoted to a separate shared library rather
than duplicated across course repositories. Candidate areas include:

- Algebraic laws and identities.
- Exponent and logarithm rules.
- Trigonometric identities.
- Symbolic and numerical verification helpers.
- Plotting and visualization utilities.
- Convergence-test references.
- Common integration patterns.
- Error-estimation tools.
- Differential-equation helpers.

Course-specific assignments, exam preparation, and reflections will remain in this
repository.

---

## Status Legend

- ⬜ Not Started
- 🟨 In Progress
- ✅ Completed

---

_Last updated: August 2026_


```
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pip install -e "..\math-library[all]"
```