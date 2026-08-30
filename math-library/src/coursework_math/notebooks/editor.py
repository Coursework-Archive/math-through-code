from pathlib import Path

import nbformat


def parse_questions(value: str) -> list[int]:
    """Convert '1-5, 8, 10-12' into a list of question numbers."""
    questions = []

    for part in value.split(","):
        part = part.strip()

        if "-" in part:
            start, end = part.split("-", maxsplit=1)
            questions.extend(range(int(start), int(end) + 1))
        else:
            questions.append(int(part))

    return questions


def add_group_questions(
    notebook,
    group: str,
    questions: list[int],
) -> None:
    """Add one group and its question cells to a notebook."""

    notebook.cells.append(
        nbformat.v4.new_markdown_cell(
            f"# Group {group}"
        )
    )

    for index, question in enumerate(questions):
        is_last = index == len(questions) - 1

        content = f"---\n\n## Question {question}"

        if is_last:
            content += "\n\n\n\n---"

        notebook.cells.append(
            nbformat.v4.new_markdown_cell(
                content
            )
        )


def update_notebook(
    notebook_path: str,
    groups: list[tuple[str, list[int]]],
) -> None:
    path = Path(notebook_path)

    # Add .ipynb automatically if omitted
    if path.suffix != ".ipynb":
        path = path.with_suffix(".ipynb")

    is_new = not path.exists()

    if is_new:
        path.parent.mkdir(parents=True, exist_ok=True)

        notebook = nbformat.v4.new_notebook()

        # Only new notebooks get this first cell
        notebook.cells.append(
            nbformat.v4.new_markdown_cell(
                r"\setcounter{secnumdepth}{0}"
            )
        )
    else:
        with path.open("r", encoding="utf-8") as file:
            notebook = nbformat.read(file, as_version=4)

    total_questions = 0

    for group, questions in groups:
        add_group_questions(
            notebook,
            group,
            questions,
        )

        total_questions += len(questions)

    with path.open("w", encoding="utf-8") as file:
        nbformat.write(notebook, file)

    action = "Created" if is_new else "Updated"

    print(
        f"\n{action} {path.name}: "
        f"{len(groups)} groups with "
        f"{total_questions} questions."
    )


if __name__ == "__main__":
    notebook_path = input(
        "Notebook name or path: "
    ).strip()

    number_of_groups = int(
        input("Number of groups: ").strip()
    )

    groups = []

    for index in range(number_of_groups):
        print(
            f"\nGroup {index + 1} "
            f"of {number_of_groups}"
        )

        group = input("Group: ").strip()

        question_input = input(
            "Questions: "
        ).strip()

        questions = parse_questions(
            question_input
        )

        groups.append(
            (group, questions)
        )

    update_notebook(
        notebook_path,
        groups,
    )