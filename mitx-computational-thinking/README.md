# 🧮 mitx-computational-thinking 
*MITx – “Introduction to Computational Thinking and Data Science”*
Why it fits: Focuses on modeling and algorithmic reasoning, with Python examples. 
If you want a deep, code-integrated mathematical course.

edX (Intermediate → Advanced)
Algorithms, simulation, optimization, probability modeling, and data-driven reasoning using Python + Jupyter.
9 weeks (6–8 hrs/week)
🔹 Mirrors your notebook-to-prod repo style.
🔹 Uses code-driven math with automation context (Monte Carlo, random seeds, optimization).
🔹 Great stepping stone for your math-through-code repo.

---

### 📘 Overview
This is my completion of the **MITx: Introduction to Computational Thinking and Data Science (6.00.2x)** course on [edX](https://www.edx.org/learn/computer-science/massachusetts-institute-of-technology-introduction-to-computational-thinking-and-data-science).  
It explores **simulation, probability, optimization, and data analysis** — all through executable code notebooks that connect theoretical concepts to real-world computation.

---
```text
### 🧩 Repository Structure
mitx-computational-thinking/
│
├── README.md                        # overview + course link + progress log
│
├── notebooks/
│   ├── 01_monte_carlo_simulation.ipynb
│   ├── 02_linear_regression_from_scratch.ipynb
│   ├── 03_optimization_and_random_search.ipynb
│
├── problem_sets/
│   ├── ps1/
│
└── notes/
    ├── syllabus.pdf
    ├── week1_optimization_and_knapsack_problem.md
    ├── week2_simulation_notes.md
    └── week3_modeling_notes.md
```

### 📚 Course Topics
The MITx 6.00.2x course includes:
- Randomness, simulation, and estimation
- Distributions and sampling
- Monte Carlo methods
- Optimization (brute-force, gradient, stochastic)
- Statistical thinking and data-driven modeling
- Machine learning basics and curve fitting

---

### 🧠 Planned Notebooks
| # | Concept | Notebook | Goal / Application |
|---|----------|-----------|-------------------|
| 1 | **Monte Carlo Simulation** | `01_monte_carlo_simulation.ipynb` | Estimate probabilities, model uncertainty — e.g., test flakiness or CI reliability. |
| 2 | **Regression & Model Fitting** | `02_linear_regression_from_scratch.ipynb` | Implement simple regressors; visualize residuals. |
| 3 | **Optimization** | `03_optimization_and_random_search.ipynb` | Compare brute-force and gradient-based methods. |
| 4 | **Stochastic Sampling** | *(Optional)* | Analyze distributions or automation timing variance. |

---

### 🧾 Progress Tracker
| Week        | Topic                                                                         | Status | Notes |
|-------------|-------------------------------------------------------------------------------|--------|-|
| Preliminary | Enroll at edX – MITx Introduction to Computational Thinking and Data Science  | 🟩 Done | Completed Oct 25 |
| Week 1      | Computational Thinking & Python Review                                        | 🟩 Done | Completed Nov 8 |
| Week 2      | Simulation & Randomness                                                       | 🟨 In Progress ||
| Week 3      | Distributions & Sampling                                                      | 🟨 In Progress ||
| Week 4      | Monte Carlo Methods                                                           | ⬜ Not Started ||
| Week 5      | Optimization & Search                                                         | ⬜ Not Started ||
| Week 6      | Data Analysis & Modeling                                                      | ⬜ Not Started ||
| Week 7      | Machine Learning Intro                                                        | ⬜ Not Started ||
| Week 8      | Review & Final Project                                                        | ⬜ Not Started ||
| Week 9      | Certificate + Repo Polish                                                     | ⬜ Not Started ||

---

### 🧩 Tools & Environment
- **Language:** Python 3.11+  
- **Environment:** `venv` or Conda  
- **Recommended Packages:**  
  `numpy`, `matplotlib`, `pandas`, `scipy`, `notebook`, `seaborn`

Initialize with:
```bash
python -m venv .venv
source .venv/bin/activate      # (or .venv\Scripts\activate on Windows)
pip install -r requirements.txt


📜 License

MIT License © 2025 Brittany L. Bales
For educational and demonstration purposes.

💡 Notes

This project bridges conceptual mathematics and real-world engineering by transforming abstract ideas into reproducible, data-driven code notebooks — making computational thinking tangible through practical experimentation.

