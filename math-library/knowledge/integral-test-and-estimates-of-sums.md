# The Integral Test and Estimates of Sums

Module 6 · Section 11.3

## Purpose

Series tests determine whether a series converges or diverges. No single test works for every series. Establishing convergence does not usually give the exact sum.

## The Integral Test

Let $a_n=f(n)$. If $f$ is **continuous, positive, and decreasing** on $[N,\infty)$, then:

```math
\boxed{\sum_{n=N}^{\infty} a_n \text{ converges}
\Longleftrightarrow
\int_N^{\infty} f(x)\,dx \text{ converges}}
```

- A finite improper integral means the series converges.
- A divergent improper integral means the series diverges.
- The series and integral need not have the same value.
- Conditions may hold only after finitely many terms; removing those terms does not change convergence.

### Procedure

1. Define $f(x)$ by replacing $n$ with $x$ in $a_n$.
2. Check continuity and positivity on the relevant interval.
3. Show that $f$ decreases, often by checking $f'(x)<0$.
4. Write the improper integral as a limit.
5. Evaluate the limit and state the corresponding conclusion for the series.

```math
\int_N^{\infty} f(x)\,dx
=\lim_{t\to\infty}\int_N^t f(x)\,dx
```

### Check the terms first

```math
\boxed{\lim_{n\to\infty}a_n\ne0
\Longrightarrow \sum a_n\text{ diverges}}
```

If the limit does not exist, the series also diverges. If the limit is zero, the Divergence Test is inconclusive: another test is needed.

Approaching zero is necessary for convergence, but it is not an additional hypothesis of the Integral Test. A positive decreasing function can approach a positive number; in that case both its series and integral diverge.

---

## Why the Integral Test Works

Assume the conditions hold from $x=1$ and $a_n=f(n)$. Each rectangle has width $1$, so its area equals its height.

### Right endpoints: rectangles below the curve

On $[k-1,k]$, the height is $f(k)=a_k$. Because $f$ decreases, the rectangle lies below the curve.

```math
a_2+a_3+\cdots+a_n\le\int_1^n f(x)\,dx
```

The first rectangle has height $a_2=f(2)$ and occupies $[1,2]$. Thus $a_1$ is absent from the rectangle sum, even though the integral starts at $1$.

Add $a_1$ to obtain the partial sum:

```math
s_n=a_1+a_2+\cdots+a_n
\le a_1+\int_1^n f(x)\,dx
\le a_1+\int_1^{\infty} f(x)\,dx
```

If the improper integral equals a finite number $F$, then $s_n\le a_1+F$. Positive terms make $(s_n)$ increasing. An increasing sequence bounded above converges, so the series converges.

### Left endpoints: rectangles above the curve

On $[k,k+1]$, the height is $f(k)=a_k$. The rectangle lies above the decreasing curve.

```math
\int_1^n f(x)\,dx
\le a_1+a_2+\cdots+a_{n-1}=s_{n-1}
```

If the integral grows without bound as $n\to\infty$, this inequality forces the partial sums to grow without bound. The series diverges.

---

## The p-Series Test

A p-series has the form:

```math
\sum_{n=1}^{\infty}\frac{1}{n^p}
```

```math
\boxed{\begin{aligned}
p>1&\Longrightarrow\text{converges},\\
p\le1&\Longrightarrow\text{diverges}.
\end{aligned}}
```

### Recognition

| Term | Rewrite | Value of $p$ |
|---|---|---|
| $1/n^2$ | $n^{-2}$ | $2$ |
| $1/\sqrt[3]{n}$ | $n^{-1/3}$ | $1/3$ |
| $1/n^{1.001}$ | $n^{-1.001}$ | $1.001$ |
| $1/n$ | $n^{-1}$ | $1$ |

The harmonic series $\sum_{n=1}^{\infty}1/n$ diverges: $p=1$ is the boundary and belongs to the divergent case. Slow growth is still unbounded growth.

### Connection to integration

For $p\ne1$:

```math
\int_1^t x^{-p}\,dx
=\frac{t^{1-p}-1}{1-p}
```

- If $p>1$, then $1-p<0$, so $t^{1-p}\to0$ and the integral converges.
- If $0<p<1$, then $1-p>0$, so the integral diverges.
- If $p=1$, the integral is $\ln t\to\infty$.
- If $p\le0$, the series terms do not approach zero.

Once the p-series form is recognized, use the test directly; repeating the integration is unnecessary.

A constant multiple can be factored out. A term such as $1/(n^2-1)$ is not itself in p-series form; resemblance alone does not justify the p-series Test.

**Module 6 instruction for Section 11.3:** If the series is not a p-series, use the Integral Test.

---

## Partial Sums and Remainders

For a convergent series with positive terms:

```math
s=\sum_{k=1}^{\infty}a_k,
\qquad s_n=\sum_{k=1}^n a_k
```

```math
\boxed{R_n=s-s_n=\sum_{k=n+1}^{\infty}a_k}
```

- $s$: exact sum.
- $s_n$: approximation using the first $n$ terms.
- $R_n$: remainder, or error; it starts with $a_{n+1}$.
- Positive terms give $s_n<s$, so the partial sum underestimates the sum.

## Remainder Estimate

If $a_k=f(k)$, the series converges, and $f$ is continuous, positive, and decreasing for $x\ge n$, then:

```math
\boxed{\int_{n+1}^{\infty}f(x)\,dx
\le R_n\le
\int_n^{\infty}f(x)\,dx}
```

### Remember the bounds

- Start at $n+1$ for the **lower** error bound.
- Start at $n$ for the **upper** error bound.
- For a positive function, starting farther right leaves less area.

The tail rectangles occupy $[n,\infty)$ with right-endpoint heights $a_{n+1},a_{n+2},\ldots$ and lie below the curve. Shift those same heights to left endpoints on $[n+1,\infty)$ and they lie above the curve. These two arrangements bound the same remainder.

## Choosing Enough Terms

To guarantee error less than a tolerance $\varepsilon$:

1. Find the upper error bound $U_n=\int_n^{\infty}f(x)\,dx$.
2. Solve $U_n<\varepsilon$.
3. Choose an integer $n$ satisfying the inequality.

```math
\boxed{R_n\le U_n<\varepsilon
\Longrightarrow \lvert s-s_n\rvert<\varepsilon}
```

For a requirement of error **at most** $\varepsilon$, using $U_n\le\varepsilon$ is sufficient. Keep strict and non-strict inequalities consistent with the wording.

## Improved Bounds for the Sum

Add $s_n$ to all three parts of the remainder estimate:

```math
\boxed{s_n+\int_{n+1}^{\infty}f(x)\,dx
\le s\le
s_n+\int_n^{\infty}f(x)\,dx}
```

This gives an interval containing the exact sum, rather than only an error bound.

## Quick Review

| Goal | Tool |
|---|---|
| Determine convergence of a p-series | Compare $p$ with $1$ |
| Apply the Integral Test | Check continuity, positivity, and decrease; evaluate the improper integral |
| Bound the error in $s_n$ | Bound $R_n$ between the two tail integrals |
| Guarantee a tolerance | Make the upper error bound small enough |
| Improve the estimate of $s$ | Add $s_n$ to both remainder bounds |

**Keep the distinction:** A convergence test establishes whether a finite sum exists. An error estimate measures how closely a partial sum approximates that sum.
