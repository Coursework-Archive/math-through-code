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
| Week        | Topic                                                                        | Status          | Notes                      |
|-------------|------------------------------------------------------------------------------|-----------------|----------------------------|
| Preliminary | Enroll at edX – MITx Introduction to Computational Thinking and Data Science | 🟩 Done         | Completed on Oct  25       |
| Week 1      | Optimization and Knapsack Problem                                            | 🟩 Done         | Completed Nov 1            |
| Week 2      | Decision Trees and Dynamic Programming                                       | 🟩 Done         | Completed Nov 1            |
| Week 3      | Graph Problems                                                               | 🟩 Done         | Completed Nov 8            |
|             | Problem Set 1                                                                | 🟩 Done         | Completed Nov 2            |
| Week 4      | Plotting                                                                     | 🟩 Done         | Completed Nov 8            |
|             | Stochastic Thinking                                                          | 🟩 Done         | Completed Nov 8            |
| Week 5      | Random Walks                                                                 | 🟨 In Progress  |                            |
|             | Problem Set 2                                                                | 🟨 In Progress  | _Due Nov 20_               | 
| Week 6      | Midterm                                                                      | ⬜ Not Started   | **Start Review by Nov 14** |
|             | Inferential Statistics                                                       | ⬜ Not Started   |                            |
|             | Monte Carlo Simulations                                                      | ⬜ Not Started   |                            |
| Week 7      | Sampling and Standard Error                                                  | ⬜ Not Started   | w7 : Nov 26 - Dec 2        |
|             | Problem Set 3                                                                | ⬜ Not Started   | _Due Dec 4_                |
| Week 8      | Experimental Data                                                            | ⬜ Not Started   | w8 : Dec 3 - Dec 9         |
|             | Problem Set 4                                                                | ⬜ Not Started   | _Due Dec 11_               |
| Week 9      | Machine Learning                                                             | ⬜ Not Started   | w9 : Dec 10 - Dec 16       | 
|             | Statistical Fallacies                                                        | ⬜ Not Started   |                            | 
|             | Review & Final Exam                                                          | ⬜ Not Started   | **Start Review Dec 6**     |
|             | Certificate + Repo Polish                                                    | ⬜ Not Started   | Complete by EOY            |

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

