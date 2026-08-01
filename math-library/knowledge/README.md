# Shared Mathematics Knowledge Base

This folder contains reusable explanations, formula references, recognition rules, and supporting images for multiple mathematics courses.

## Current Scope

The initial material was developed during Calculus I and includes:

- algebra and exponent rules;
- functions and transformations;
- limits and continuity;
- trigonometry;
- differentiation and antiderivatives;
- applications of integration;
- motion and graph interpretation.

Calculus II material should be added here when it is broadly reusable, such as:

- integration-method references;
- convergence-test decision rules;
- power-series identities;
- approximation-error references;
- differential-equation patterns.

## Markdown and Math Formatting

Use GitHub-compatible math syntax:

- Inline math: `$f(x)=x^2$`.
- Display math: fenced `math` blocks.
- Keep table-cell formulas inline rather than placing display-math delimiters inside tables.
- Use supported operators such as `\operatorname{sech}` and `\operatorname{csch}` when a shorthand command does not render on GitHub.

Example:

````markdown
```math
\int_a^b f(x)\,dx
```
````

## Naming

Use lowercase, descriptive, hyphen-separated filenames:

```text
integration-by-parts.md
power-series.md
ratio-and-root-tests.md
```

## Boundary

Do not place submitted homework, exam plans, instructor comments, grades, transcripts, or personal reflections in this folder. Those belong in the applicable course repository or private academic archive.

## Images

Reusable images are stored in [`images/`](images/). Markdown files should reference them with relative paths such as:

```markdown
![Unit Circle](images/unit_circle.jpg)
```
