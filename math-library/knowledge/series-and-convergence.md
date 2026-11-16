# Series and Convergence

A **sequence** is an ordered list of terms. A **series** adds the terms of a sequence.

```math
a_1,a_2,a_3,\ldots \qquad \text{(sequence)}
```

```math
\sum_{n=1}^{\infty}a_n=a_1+a_2+a_3+\cdots \qquad \text{(series)}
```

---

## Partial Sums

A partial sum adds the first $n$ terms of a series.

```math
\boxed{s_n=\sum_{i=1}^{n}a_i=a_1+a_2+\cdots+a_n}
```

The partial sums $s_1,s_2,s_3,\ldots$ form a sequence.

### Convergence Rule

A series **converges** if its sequence of partial sums approaches a finite number $s$.

```math
\boxed{\lim_{n\to\infty}s_n=s\quad\Longrightarrow\quad\sum_{n=1}^{\infty}a_n=s}
```

A series **diverges** if the partial sums do not approach a finite number.

### Recognition Rule

- **Sequence question:** Examine the limit of the individual terms $a_n$.
- **Series question:** Examine the limit of the partial sums $s_n$.
- Do **not** assume that $a_n\to0$ means the series converges.

---

## Geometric Series

Each term is the preceding term multiplied by the same **common ratio** $r$.

```math
\boxed{a+ar+ar^2+ar^3+\cdots=\sum_{n=0}^{\infty}ar^n}
```

Here $a$ is the first term and $r$ is the common ratio.

### Convergence and Sum

For $a\ne0$:

| Condition | Result |
|---|---|
| $\lvert r\rvert<1$ | Converges |
| $\lvert r\rvert\ge1$ | Diverges |

When $\lvert r\rvert<1$:

```math
\boxed{S=\frac{a}{1-r}}
```

### Finite Partial Sum

For $r\ne1$, the first $n$ terms sum to:

```math
\boxed{s_n=\frac{a(1-r^n)}{1-r}}
```

If $\lvert r\rvert<1$, then $r^n\to0$, leaving $S=a/(1-r)$.

### Recognition Rule

Look for a fixed ratio between consecutive terms:

```math
r=\frac{a_{n+1}}{a_n}
```

For example:

```math
\frac12+\frac14+\frac18+\frac1{16}+\cdots
```

- First term: $a=1/2$
- Common ratio: $r=1/2$
- Since $\lvert r\rvert<1$, the series converges.

```math
S=\frac{1/2}{1-1/2}=1
```

### Starting-Index Reminder

Both forms are valid, but the exponent changes:

```math
\sum_{n=0}^{\infty}ar^n
\qquad\text{and}\qquad
\sum_{n=1}^{\infty}ar^{n-1}
```

In either form, $a$ represents the first term.

---

## Geometric Power Series

A geometric series may contain a variable:

```math
1+x+x^2+x^3+\cdots=\sum_{n=0}^{\infty}x^n
```

Here $a=1$ and $r=x$. Therefore:

```math
\boxed{\sum_{n=0}^{\infty}x^n=\frac{1}{1-x}\qquad(\lvert x\rvert<1)}
```

This is an introductory example of a **power series**.

---

## Harmonic Series

```math
\boxed{\sum_{n=1}^{\infty}\frac1n=1+\frac12+\frac13+\frac14+\cdots}
```

The harmonic series **diverges**, even though its terms approach zero.

```math
\lim_{n\to\infty}\frac1n=0
```

### Why It Diverges

Grouping successive terms produces groups with sums at least $1/2$:

```math
1+\frac12+\left(\frac13+\frac14\right)
+\left(\frac15+\cdots+\frac18\right)+\cdots
```

There are infinitely many such groups, so the partial sums grow without bound.

### Memory Rule

```math
\boxed{a_n\to0\ \text{does not guarantee}\ \sum a_n\ \text{converges}}
```

---

## Test for Divergence

**Theorem:** If a series converges, its individual terms must approach zero.

```math
\sum_{n=1}^{\infty}a_n\text{ converges}
\quad\Longrightarrow\quad
\lim_{n\to\infty}a_n=0
```

Therefore:

```math
\boxed{\lim_{n\to\infty}a_n\ne0\ \text{or DNE}
\quad\Longrightarrow\quad
\sum_{n=1}^{\infty}a_n\text{ diverges}}
```

### Decision Rule

| Limit of $a_n$ | Conclusion |
|---|---|
| Nonzero finite number | Divergent |
| $+\infty$ or $-\infty$ | Divergent |
| Does not exist | Divergent |
| $0$ | Inconclusive — use another test |

### Example

```math
\sum_{n=1}^{\infty}\frac{n^2}{5n^2+4}
```

Check the term limit:

```math
\lim_{n\to\infty}\frac{n^2}{5n^2+4}=\frac15\ne0
```

Therefore the series **diverges**.

---

## Connection to Improper Integrals

Both infinite series and improper integrals are defined by limits.

```math
\sum_{n=1}^{\infty}a_n
=\lim_{N\to\infty}\sum_{n=1}^{N}a_n
```

```math
\int_1^{\infty}f(x)\,dx
=\lim_{t\to\infty}\int_1^t f(x)\,dx
```

A series adds discrete terms; an integral accumulates continuously.

---

## Properties of Convergent Series

If $\sum a_n$ and $\sum b_n$ converge, and $c$ is constant:

```math
\sum_{n=1}^{\infty}ca_n=c\sum_{n=1}^{\infty}a_n
```

```math
\sum_{n=1}^{\infty}(a_n\pm b_n)
=\sum_{n=1}^{\infty}a_n\pm\sum_{n=1}^{\infty}b_n
```

Changing finitely many terms does **not** change whether a series converges, but it can change its sum.

---

## Series Recognition Cheat Sheet

| If You See | Think |
|---|---|
| $a_1,a_2,a_3,\ldots$ | Sequence |
| $\sum a_n$ | Series; examine partial sums |
| $s_n=\sum_{i=1}^n a_i$ | Partial sum |
| $a+ar+ar^2+\cdots$ | Geometric series |
| $\lvert r\rvert<1$ | Geometric convergence |
| $\lvert r\rvert\ge1$ and $a\ne0$ | Geometric divergence |
| $\sum 1/n$ | Harmonic series; divergent |
| $\lim a_n\ne0$ or DNE | Divergence test proves divergence |
| $\lim a_n=0$ | Divergence test inconclusive |

---

## Series Problem-Solving Process

1. Identify the term $a_n$.
2. Check whether consecutive terms have a constant ratio (geometric pattern).
3. If geometric, determine the **first term** $a$ and **ratio** $r$.
4. Check $\lvert r\rvert<1$; if convergent, use $S=a/(1-r)$.
5. If not geometric, evaluate $\lim_{n\to\infty}a_n$ as a quick divergence test.
6. If that limit is zero, do **not** conclude convergence; another test is needed.

---

## Common Mistakes

1. **Confusing terms with partial sums:** $a_n$ is one term; $s_n$ adds the first $n$ terms.
2. **Assuming shrinking terms ensure convergence:** The harmonic series disproves this.
3. **Using the geometric sum formula when $\lvert r\rvert\ge1$:** The infinite sum formula requires convergence.
4. **Ignoring the starting index:** Check which expression is the actual first term.
5. **Treating the divergence test as a convergence test:** A zero term limit gives no conclusion.

---

## Memory Rules

```math
\boxed{\text{Series convergence}\iff\text{partial sums have a finite limit}}
```

```math
\boxed{\text{Geometric:}\quad\lvert r\rvert<1\Rightarrow S=\frac{a}{1-r}}
```

```math
\boxed{\lim a_n\ne0\ \text{or DNE}\Rightarrow\text{series diverges}}
```

**Source:** Calculus II, Section 11.2 (Infinite Series, Geometric Series, Harmonic Series, and Test for Divergence), with accompanying instructor notes.
