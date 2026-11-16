
# Series — Comparison Tests

## 1. Overview

The Comparison Tests determine whether a series converges or diverges by comparing it with a known series.

Let:

- $\sum a_n$ = the series being tested.
- $\sum b_n$ = a known comparison series.

Both tests require positive terms.

The two methods are:

1. **Direct Comparison Test** — Compare terms using inequalities.
2. **Limit Comparison Test** — Compare the ratio of corresponding terms as $n \to \infty$.

### Standard Comparison Series

The most useful comparison series are the p-series and geometric series.

**p-Series**

```math
\boxed{\sum_{n=1}^{\infty}\frac{1}{n^p}}
```

- $p>1$ → Converges.
- $p\leq 1$ → Diverges.

**Geometric Series**

```math
\boxed{\sum_{n=0}^{\infty}ar^n}
```

- $\lvert r\rvert<1$ → Converges.
- $\lvert r\rvert\geq 1$ → Diverges.

---

## 2. Direct Comparison Test

Suppose $\sum a_n$ and $\sum b_n$ have positive terms.

### Case 1 — Proving Convergence

If

```math
0\leq a_n\leq b_n
```

and $\sum b_n$ converges, then $\sum a_n$ also converges.

**Recognition Rule**

```math
\boxed{\text{Smaller than a convergent series}
\Longrightarrow \text{Convergent}}
```

### Case 2 — Proving Divergence

If

```math
0\leq b_n\leq a_n
```

and $\sum b_n$ diverges, then $\sum a_n$ also diverges.

**Recognition Rule**

```math
\boxed{\text{Larger than a divergent series}
\Longrightarrow \text{Divergent}}
```

### When the Test Is Inconclusive

The following comparisons do not establish convergence or divergence:

- Larger than a convergent series.
- Smaller than a divergent series.

**Important:** The direction of the inequality determines whether the Direct Comparison Test can establish a conclusion.

### Why the Test Works

For positive terms, the sequence of partial sums is increasing.

If

```math
a_n\leq b_n
```

then

```math
\sum_{i=1}^{n}a_i\leq\sum_{i=1}^{n}b_i
```

If $\sum b_n$ converges, its partial sums are bounded above.

Therefore, the partial sums of $\sum a_n$ are also bounded above.

An increasing, bounded sequence converges.

Consequently, $\sum a_n$ converges.

This connects the Comparison Test to the **Monotone Convergence Theorem for Sequences**.

---

## 3. Limit Comparison Test

Suppose $\sum a_n$ and $\sum b_n$ have positive terms.

Calculate:

```math
\boxed{c=\lim_{n\to\infty}\frac{a_n}{b_n}}
```

### Main Rule

If

```math
0<c<\infty
```

then both series have the same convergence behavior.

- If $\sum b_n$ converges, $\sum a_n$ converges.
- If $\sum b_n$ diverges, $\sum a_n$ diverges.

The constant $c$ may be any positive, finite number.

### Intuition

Suppose

```math
\lim_{n\to\infty}\frac{a_n}{b_n}=2
```

For sufficiently large $n$:

```math
a_n\approx 2b_n
```

Multiplying the terms of a series by a positive constant does not change whether it converges or diverges.

### Special Cases

The following extensions apply to positive-term series.

**Case 1: $c=0$**

If

```math
\lim_{n\to\infty}\frac{a_n}{b_n}=0
```

and $\sum b_n$ converges, then $\sum a_n$ converges.

If $\sum b_n$ diverges, the result is inconclusive.

**Case 2: $c=\infty$**

If

```math
\lim_{n\to\infty}\frac{a_n}{b_n}=\infty
```

and $\sum b_n$ diverges, then $\sum a_n$ diverges.

If $\sum b_n$ converges, the result is inconclusive.

### Recognition Rule

```math
\boxed{
0<c<\infty
\Longrightarrow
\text{Both series behave alike}
}
```

---

## 4. Choosing the Comparison Series

The first task is identifying a known series $\sum b_n$.

For rational expressions, focus on the terms with the highest powers of $n$.

### Dominant-Term Method

Consider the general expression:

```math
a_n=\frac{P(n)}{Q(n)}
```

where $P(n)$ and $Q(n)$ are polynomials.

For large $n$, the highest-degree terms dominate.

If

```math
P(n)\sim an^m
\qquad
Q(n)\sim bn^k
```

then

```math
a_n\sim\frac{a}{b}n^{m-k}
```

The notation $\sim$ means the ratio of the two expressions approaches 1.

For comparison purposes, positive constant factors may be omitted.

### Example

Consider the practice series:

```math
\sum_{n=1}^{\infty}
\frac{3n+2}{n^4+5}
```

The dominant terms are:

```math
\frac{3n}{n^4}=\frac{3}{n^3}
```

A suitable comparison series is:

```math
\boxed{b_n=\frac{1}{n^3}}
```

This is a convergent p-series because $p=3>1$.

**Recognition Rule**

```math
\boxed{
\frac{n^m}{n^k}
=
\frac{1}{n^{k-m}}
\quad\text{when }k>m
}
```

The dominant terms help select $b_n$; a comparison test is still needed to justify the conclusion.

---

## 5. Evaluating the Limit Comparison

After selecting $b_n$, calculate:

```math
\lim_{n\to\infty}\frac{a_n}{b_n}
```

### Dividing by a Fraction

Instead of dividing by $b_n$, multiply by its reciprocal.

```math
\boxed{
\frac{a_n}{b_n}
=
a_n\cdot\frac{1}{b_n}
}
```

### Example

Using the practice series:

```math
a_n=\frac{3n+2}{n^4+5}
\qquad
b_n=\frac{1}{n^3}
```

Form the ratio:

```math
\frac{a_n}{b_n}
=
\frac{3n+2}{n^4+5}\cdot n^3
```

Simplify:

```math
=\frac{3n^4+2n^3}{n^4+5}
```

Divide numerator and denominator by $n^4$:

```math
=\frac{3+\frac{2}{n}}{1+\frac{5}{n^4}}
```

Evaluate:

```math
\lim_{n\to\infty}
\frac{3+\frac{2}{n}}{1+\frac{5}{n^4}}
=3
```

Since $0<3<\infty$, both series have the same convergence behavior.

The comparison series $\sum 1/n^3$ converges.

Therefore, the original series **converges by the Limit Comparison Test**.

---

## 6. Establishing Inequalities

For the Direct Comparison Test, we must establish an inequality between $a_n$ and $b_n$.

### Rule 1 — Same Positive Numerator

The larger positive denominator produces the smaller fraction.

```math
\frac{1}{n^3}<\frac{1}{n^2}
\qquad (n>1)
```

### Rule 2 — Same Positive Denominator

The larger numerator produces the larger fraction.

```math
\frac{n+1}{n^3}>\frac{n}{n^3}
```

### Rule 3 — Larger Numerator and Smaller Denominator

For positive numerators and denominators, a larger numerator together with a smaller denominator produces a larger fraction.

### Rule 4 — Conflicting Changes

If one fraction has both a larger numerator and a larger denominator, the comparison is not immediately clear.

Use algebra or cross multiplication to establish the inequality.

For positive denominators:

```math
\boxed{
\frac{A}{B}\leq\frac{C}{D}
\Longleftrightarrow
AD\leq BC
}
```

**Important:** Verify that denominators are positive before cross multiplying without changing the inequality direction.

---

## 7. Choosing Between the Tests

| Situation | Preferred Approach |
|---|---|
| A simple inequality is apparent | Direct Comparison |
| Rational expression with dominant powers | Limit Comparison |
| Expressions behave similarly for large $n$ | Limit Comparison |
| Need to prove a series is smaller than a convergent series | Direct Comparison |
| Need to prove a series is larger than a divergent series | Direct Comparison |
| Comparison limit is positive and finite | Limit Comparison |

The instructor recommends considering the Limit Comparison Test first for many positive-term series because it often avoids complicated inequalities.

---

## 8. Writing a Complete Solution

Use the instructor's three-step process.

### Step 1 — Select the Comparison Series

Identify $b_n$ and explain why $\sum b_n$ converges or diverges.

For example:

```math
b_n=\frac{1}{n^p}
```

State the value of $p$ and apply the p-series rule.

### Step 2 — Apply the Comparison Test

**Direct Comparison:**

Establish the appropriate inequality:

```math
a_n\leq b_n
\quad\text{or}\quad
a_n\geq b_n
```

Explain why the inequality is true.

**Limit Comparison:**

Calculate:

```math
\lim_{n\to\infty}\frac{a_n}{b_n}=c
```

Determine whether the limit satisfies the conditions of the test.

### Step 3 — State the Conclusion

Explicitly state:

- Whether the series converges or diverges.
- Which comparison test justifies the conclusion.

**Suggested wording:**

"The series converges by the Limit Comparison Test because the comparison series converges and the limit is a positive, finite constant."

---

## 9. Estimating Sums Using Comparison

The Direct Comparison Test can also help estimate the error when approximating the sum of a convergent series.

Let:

```math
s=\sum_{n=1}^{\infty}a_n
```

The $n$th partial sum is:

```math
s_n=\sum_{i=1}^{n}a_i
```

The remainder is:

```math
\boxed{
R_n=s-s_n=\sum_{i=n+1}^{\infty}a_i
}
```

For a known comparison series $\sum b_n$, define:

```math
T_n=\sum_{i=n+1}^{\infty}b_i
```

If

```math
0\leq a_n\leq b_n
```

and the comparison series converges, then:

```math
\boxed{0\leq R_n\leq T_n}
```

The remainder of the comparison series provides an upper bound on the approximation error.

- For a p-series, the Integral Test remainder estimate may be useful.
- For a geometric series, the remainder can be calculated using the geometric series formula.

---

## 10. Recognition Rules — Quick Reference

| Condition | Conclusion |
|---|---|
| $0\leq a_n\leq b_n$, $\sum b_n$ converges | $\sum a_n$ converges |
| $0\leq b_n\leq a_n$, $\sum b_n$ diverges | $\sum a_n$ diverges |
| $a_n\geq b_n$, $\sum b_n$ converges | Inconclusive |
| $a_n\leq b_n$, $\sum b_n$ diverges | Inconclusive |
| $\lim a_n/b_n=c$, $0<c<\infty$ | Both behave alike |
| $\lim a_n/b_n=0$, $\sum b_n$ converges | $\sum a_n$ converges |
| $\lim a_n/b_n=\infty$, $\sum b_n$ diverges | $\sum a_n$ diverges |

### Final Memory Cues

**Direct Comparison**

```math
\boxed{
\begin{aligned}
\text{Smaller + Convergent} &\Rightarrow \text{Convergent}\\
\text{Larger + Divergent} &\Rightarrow \text{Divergent}
\end{aligned}
}
```

**Limit Comparison**

```math
\boxed{
\lim_{n\to\infty}\frac{a_n}{b_n}=c,
\quad 0<c<\infty
\Rightarrow
\text{Same behavior}
}
```

**Choosing $b_n$**

```math
\boxed{
\text{Identify dominant terms}
\rightarrow
\text{Select known series}
\rightarrow
\text{Apply test}
}
```

**Proof Reminder**

An intuitive expectation that a series converges or diverges is useful for choosing a comparison series, but it does not replace a mathematical justification.
