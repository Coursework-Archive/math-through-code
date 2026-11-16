# 11.1 — Sequences

## 1. Definition of a Sequence

An **infinite sequence** is an ordered list of numbers following a definite pattern.

$$
a_1,\ a_2,\ a_3,\ \ldots,\ a_n,\ \ldots
$$

- $a_n$ is the **nth term**.
- $n$ is a positive integer.
- $a_{n+1}$ is the successor of $a_n$.
- A sequence can be regarded as a function whose domain is the positive integers.

### Explicit and Recursive Sequences

**Explicit formula:** Determines $a_n$ directly from $n$.

$$
a_n=f(n)
$$

**Recursive formula:** Defines a term using one or more previous terms, together with initial values.

$$
a_{n+1}=f(a_n)
$$

---

## 2. Limit of a Sequence

### Intuitive Definition — Definition 1

A sequence $\{a_n\}$ converges to $L$ if its terms become arbitrarily close to $L$ as $n$ increases.

$$
\boxed{\lim_{n\to\infty}a_n=L}
$$

Equivalently,

$$
a_n\to L \quad \text{as } n\to\infty
$$

- **Convergent:** Approaches a finite limit.
- **Divergent:** Does not approach a finite limit.
- A divergent sequence may increase without bound or oscillate without approaching a single value.

### Precise Definition — Definition 2

A sequence converges to $L$ if, for every $\varepsilon>0$, there exists an integer $N$ such that

$$
\boxed{n>N\Longrightarrow |a_n-L|<\varepsilon}
$$

Equivalently,

$$
L-\varepsilon<a_n<L+\varepsilon
$$

**Recognition:**

- $\varepsilon$ determines **how close** the terms must be to $L$.
- $N$ determines **how far into the sequence** we must go.
- Every term after $N$ must remain within the interval.

A finite number of terms outside this interval does not prevent convergence.

---

## 3. Infinite Limits — Definition 3

A sequence diverges to positive infinity if its terms eventually exceed every positive number $M$.

$$
\boxed{\lim_{n\to\infty}a_n=\infty}
$$

For every $M>0$, there exists an integer $N$ such that

$$
n>N\Longrightarrow a_n>M
$$

Similarly, divergence to negative infinity means that the terms eventually become smaller than every negative threshold.

**Important:** An infinite limit indicates divergence, not convergence to a finite number.

---

## 4. Graphing a Sequence

A sequence is graphed using discrete points:

$$
(1,a_1),\ (2,a_2),\ (3,a_3),\ldots,(n,a_n)
$$

Unlike a continuous function, a sequence is defined only at integer indices.

**Recognition:** Examine the behavior of the plotted points as $n$ increases, rather than imagining a smooth curve connecting every point.

---

## 5. Properties of Convergent Sequences

### Theorem 4 — Connection to Function Limits

If $f(n)=a_n$ for positive integers $n$, and

$$
\lim_{x\to\infty}f(x)=L
$$

then

$$
\boxed{\lim_{n\to\infty}a_n=L}
$$

**Recognition:** A continuous-variable function can sometimes be used to evaluate a sequence limit.

This connection allows familiar Calculus I limit techniques, including L'Hôpital's Rule when its conditions are satisfied.

### Limit Laws for Sequences

Suppose

$$
\lim_{n\to\infty}a_n=A,\qquad
\lim_{n\to\infty}b_n=B
$$

where both limits are finite and $c$ is a constant.

**Sum Law**

$$
\lim_{n\to\infty}(a_n+b_n)=A+B
$$

**Difference Law**

$$
\lim_{n\to\infty}(a_n-b_n)=A-B
$$

**Constant Multiple Law**

$$
\lim_{n\to\infty}ca_n=cA
$$

**Product Law**

$$
\lim_{n\to\infty}(a_nb_n)=AB
$$

**Quotient Law**, provided $B\ne0$:

$$
\lim_{n\to\infty}\frac{a_n}{b_n}=\frac{A}{B}
$$

**Power Law**, for a power $p>0$ where the expressions are defined:

$$
\lim_{n\to\infty}a_n^p=A^p
$$

---

## 6. Squeeze Theorem for Sequences

If, for all sufficiently large $n$,

$$
a_n\le b_n\le c_n
$$

and

$$
\lim_{n\to\infty}a_n
=
\lim_{n\to\infty}c_n=L
$$

then

$$
\boxed{\lim_{n\to\infty}b_n=L}
$$

**Recognition:** Use the Squeeze Theorem when a sequence is trapped between two sequences with the same limit.

### Theorem 6 — Absolute Value

If

$$
\lim_{n\to\infty}|a_n|=0
$$

then

$$
\boxed{\lim_{n\to\infty}a_n=0}
$$

**Recognition:** Particularly useful when a sequence alternates between positive and negative values but its magnitude approaches zero.

---

## 7. Continuous Functions and Sequence Limits — Theorem 7

If

$$
\lim_{n\to\infty}a_n=L
$$

and $f$ is continuous at $L$, then

$$
\boxed{\lim_{n\to\infty}f(a_n)=f(L)}
$$

**Recognition:** Continuity permits substitution of the sequence's limit into the function.

---

## 8. Monotonic Sequences — Definition 10

A sequence is **increasing** if

$$
\boxed{a_n<a_{n+1}}
$$

for every $n\ge1$.

A sequence is **decreasing** if

$$
\boxed{a_n>a_{n+1}}
$$

for every $n\ge1$.

A sequence is called **monotonic** if it is increasing or decreasing.

### Methods for Identifying Monotonicity

1. Compare consecutive terms $a_n$ and $a_{n+1}$.
2. Examine the sign of $a_{n+1}-a_n$.
3. When $a_n=f(n)$, examine the derivative $f'(x)$ for the corresponding continuous function.

**Recognition:**

- Positive difference or derivative → increasing.
- Negative difference or derivative → decreasing.
- Monotonicity alone does not guarantee convergence.

---

## 9. Bounded Sequences — Definition 11

### Bounded Above

A sequence is bounded above if there exists a number $M$ such that

$$
\boxed{a_n\le M\quad\text{for all }n\ge1}
$$

$M$ is an **upper bound**.

### Bounded Below

A sequence is bounded below if there exists a number $m$ such that

$$
\boxed{m\le a_n\quad\text{for all }n\ge1}
$$

$m$ is a **lower bound**.

### Bounded Sequence

A sequence is bounded if it has both an upper and a lower bound:

$$
\boxed{m\le a_n\le M}
$$

---

## 10. Monotonic Sequence Theorem — Theorem 12

$$
\boxed{\text{Every bounded, monotonic sequence converges.}}
$$

More specifically:

- An increasing sequence that is bounded above converges.
- A decreasing sequence that is bounded below converges.

**Visualization:** The terms continue moving in one direction but cannot pass their bound, so they approach a finite limit.

**Important:** Boundedness alone does not guarantee convergence; an oscillating sequence can be bounded but divergent.

---

## 11. Recognition Rules for Sequence Limits

| Pattern | Useful Technique |
|---|---|
| Rational expression in $n$ | Divide by the highest relevant power of $n$ |
| Alternating signs | Examine absolute values or use the Squeeze Theorem |
| Powers $r^n$ | Apply geometric sequence behavior |
| Continuous function of $a_n$ | Apply the continuity theorem |
| Sequence trapped between two others | Use the Squeeze Theorem |
| Increasing and bounded above | Apply the Monotonic Sequence Theorem |
| Decreasing and bounded below | Apply the Monotonic Sequence Theorem |

### Geometric Sequence Recognition

For $a_n=r^n$:

$$
\boxed{
\begin{aligned}
|r|<1 &\Longrightarrow r^n\to0\\
r=1 &\Longrightarrow r^n\to1\\
r>1 &\Longrightarrow r^n\to\infty
\end{aligned}
}
$$

When $r=-1$, the sequence oscillates; when $r<-1$, it alternates with increasing magnitude. Neither converges.

---

## 12. Key Study Reminders

- Sequence terms are indexed by integers.
- Convergence requires a finite limit.
- The first few terms do not determine convergence.
- A sequence may diverge through unbounded growth or oscillation.
- Use familiar function limits when applicable.
- For monotonic sequences, compare consecutive terms.
- For boundedness, identify upper and lower bounds.
- **Monotonic + bounded → convergent.**
- Visualize the sequence to support understanding, but use the mathematical conditions to justify conclusions.
