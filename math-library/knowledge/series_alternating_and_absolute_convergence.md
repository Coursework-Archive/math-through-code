
# Series — Alternating Series and Absolute Convergence

## 1. Overview

An **alternating series** is a series whose terms alternate between positive and negative values.

Unlike the convergence tests for positive-term series, the Alternating Series Test uses the changing signs of the terms to establish convergence.

Section 11.5 introduces:

1. Alternating Series Test
2. Estimating sums of alternating series
3. Absolute convergence
4. Conditional convergence
5. Rearrangements of infinite series

---

## 2. Recognizing Alternating Series

An alternating series typically contains a factor involving $(-1)^n$.

### Common Forms

```math
\boxed{
\sum_{n=1}^{\infty}(-1)^n b_n
}
```

or

```math
\boxed{
\sum_{n=1}^{\infty}(-1)^{n-1}b_n
}
```

where $b_n>0$.

### Sign Patterns

| Expression | First term when $n=1$ |
|---|---|
| $(-1)^n$ | Negative |
| $(-1)^{n-1}$ | Positive |
| $(-1)^{n+1}$ | Positive |
| $(-1)^{2n}$ | Always positive |
| $(-1)^{2n+1}$ | Always negative |

**Recognition Rule**

```math
\boxed{
\begin{aligned}
(-1)^{\text{even}}&=1\\
(-1)^{\text{odd}}&=-1
\end{aligned}
}
```

A factor of $(-1)^{2n}$ does not produce alternating signs, because $2n$ is always even.

### Important Distinction

For an alternating series:

```math
a_n=(-1)^n b_n
```

- $a_n$ includes the alternating sign.
- $b_n$ represents the positive magnitude of the term.

The Alternating Series Test applies its conditions to **$b_n$, not $a_n$**.

---

## 3. Alternating Series Test

Consider an alternating series:

```math
\sum_{n=1}^{\infty}(-1)^{n-1}b_n
```

where $b_n>0$.

The series converges if both conditions are satisfied.

### Condition 1 — Decreasing Terms

```math
\boxed{b_{n+1}\leq b_n}
```

The magnitudes of consecutive terms must eventually decrease.

### Condition 2 — Limit Approaches Zero

```math
\boxed{\lim_{n\to\infty}b_n=0}
```

The magnitudes of the terms must approach zero.

### Main Recognition Rule

```math
\boxed{
\begin{aligned}
b_{n+1}&\leq b_n\\
\lim_{n\to\infty}b_n&=0
\end{aligned}
\Longrightarrow
\text{Convergent}
}
```

Both conditions are required.

The decreasing condition may begin after a finite number of terms because changing or removing finitely many initial terms does not affect convergence.

**Important:** If the conditions cannot be established, the Alternating Series Test is inconclusive unless the Test for Divergence applies.

---

## 4. Why the Alternating Series Test Works

Consider the alternating pattern:

```math
b_1-b_2+b_3-b_4+b_5-b_6+\cdots
```

Suppose:

```math
b_1\geq b_2\geq b_3\geq\cdots>0
```

and $b_n\to0$.

The terms alternate between adding and subtracting progressively smaller quantities.

### Partial Sums

```math
\begin{aligned}
s_1&=b_1\\
s_2&=b_1-b_2\\
s_3&=b_1-b_2+b_3\\
s_4&=b_1-b_2+b_3-b_4
\end{aligned}
```

Unlike positive-term series, the partial sums do not form one increasing sequence.

Instead, they move back and forth around the eventual sum $s$.

### Grouping Terms in Pairs

Consider the even partial sums:

```math
s_{2n}=(b_1-b_2)+(b_3-b_4)+\cdots
```

Each pair is nonnegative because the magnitudes are decreasing.

Therefore, the even partial sums form an increasing sequence.

Also:

```math
s_{2n}
=b_1-(b_2-b_3)-(b_4-b_5)-\cdots-b_{2n}
```

This shows that:

```math
s_{2n}\leq b_1
```

The even partial sums are increasing and bounded above, so they converge.

The odd partial sums differ from the even partial sums by a term whose magnitude approaches zero.

Consequently, both subsequences converge to the same limit.

### Connection to Previous Topics

This proof uses the same principle encountered in Section 11.3 and Section 11.4:

```math
\boxed{
\text{Increasing + Bounded Above}
\Longrightarrow
\text{Convergent}
}
```

---

## 5. Verifying Decreasing Terms

The first condition of the Alternating Series Test can sometimes be difficult to establish.

There are two common methods.

### Method 1 — Compare Consecutive Terms

Show:

```math
\boxed{b_{n+1}\leq b_n}
```

Substitute $n+1$ into the formula for $b_n$ and establish the inequality.

This approach is useful when the inequality is straightforward.

### Method 2 — Use the Derivative

If direct comparison is difficult, define a function $f(x)$ corresponding to $b_n$.

```math
f(n)=b_n
```

Find:

```math
f'(x)
```

If:

```math
\boxed{f'(x)<0}
```

for all sufficiently large $x$, then $f(x)$ is decreasing over that interval.

Therefore, the corresponding terms $b_n$ are eventually decreasing.

### Recognition Rule

```math
\boxed{
f'(x)<0
\Longrightarrow
f(x)\text{ is decreasing}
}
```

**Important:** A negative derivative establishes decreasing behavior, but it does not establish convergence by itself.

We must also verify:

```math
\lim_{n\to\infty}b_n=0
```

---

## 6. Test for Divergence

The Test for Divergence applies to every infinite series, including alternating series.

If:

```math
\boxed{
\lim_{n\to\infty}a_n\neq0
}
```

or the term limit does not exist, then:

```math
\boxed{\sum a_n\text{ diverges}}
```

### Important Distinction

If the limit of the terms is zero, this does not prove convergence.

```math
\boxed{
\lim_{n\to\infty}a_n=0
\not\Longrightarrow
\sum a_n\text{ converges}
}
```

For the Alternating Series Test, we must also show that the positive magnitudes eventually decrease.

---

## 7. Alternating Signs Can Produce Convergence

The harmonic series:

```math
\sum_{n=1}^{\infty}\frac{1}{n}
```

diverges.

However, the alternating harmonic series:

```math
\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}
```

converges by the Alternating Series Test.

This demonstrates that changing the signs of terms can change the convergence behavior of a series.

### Recognition Rule

```math
\boxed{
\text{Positive-term divergence}
\not\Longrightarrow
\text{Alternating-series divergence}
}
```

Alternating signs can allow convergence through cancellation.

However, alternating signs do not automatically guarantee convergence.

---

## 8. Alternating Series Estimation Theorem

Suppose a convergent alternating series satisfies the conditions of the Alternating Series Test.

Let:

```math
s=\sum_{n=1}^{\infty}a_n
```

and let the first $n$ terms produce the partial sum:

```math
s_n=\sum_{i=1}^{n}a_i
```

The remainder is:

```math
R_n=s-s_n
```

### Error Bound

The absolute error is at most the magnitude of the first omitted term.

```math
\boxed{|R_n|=|s-s_n|\leq b_{n+1}}
```

This is the **Alternating Series Estimation Theorem**.

### Interpretation

If the first $n$ terms are used to approximate the infinite sum, the approximation error cannot exceed the magnitude of the next term.

The exact sum lies between two consecutive partial sums.

### Procedure — Estimating Error

1. Verify that the Alternating Series Test conditions hold.
2. Determine the number of terms used in the approximation.
3. Find the magnitude of the next term, $b_{n+1}$.
4. Use $b_{n+1}$ as an upper bound on the error.

### Required Accuracy

To guarantee an error no greater than a specified tolerance $\varepsilon$, choose $n$ such that:

```math
\boxed{b_{n+1}\leq\varepsilon}
```

### Recognition Rule

```math
\boxed{
\text{Error Bound}
=
\text{Magnitude of First Omitted Term}
}
```

This is often simpler than estimating the remainder of a positive-term series using the Integral Test.

---

## 9. Absolute Convergence

A series $\sum a_n$ is **absolutely convergent** if the series of absolute values converges.

### Definition

```math
\boxed{
\sum_{n=1}^{\infty}|a_n|
\text{ converges}
\Longrightarrow
\sum_{n=1}^{\infty}a_n
\text{ is absolutely convergent}
}
```

Taking absolute values removes the signs from individual terms.

For example, if:

```math
a_n=\frac{(-1)^n}{n^3}
```

then:

```math
|a_n|=\frac{1}{n^3}
```

The absolute-value series is a convergent p-series because $p=3>1$.

### Absolute Convergence Theorem

If a series converges absolutely, then the original series converges.

```math
\boxed{
\sum |a_n|\text{ converges}
\Longrightarrow
\sum a_n\text{ converges}
}
```

Absolute convergence is a stronger condition than ordinary convergence.

### Important Distinction

The converse is not necessarily true.

A series may converge even when the corresponding absolute-value series diverges.

---

## 10. Conditional Convergence

A series is **conditionally convergent** if the original series converges but its absolute-value series diverges.

### Definition

```math
\boxed{
\begin{aligned}
\sum a_n&\text{ converges}\\
\sum |a_n|&\text{ diverges}
\end{aligned}
\Longrightarrow
\text{Conditionally Convergent}
}
```

### Example — Alternating Harmonic Series

Consider:

```math
\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}
```

The original series converges by the Alternating Series Test.

Taking absolute values gives:

```math
\sum_{n=1}^{\infty}\frac{1}{n}
```

This is the divergent harmonic series.

Therefore, the alternating harmonic series is conditionally convergent.

### Recognition Rule

```math
\boxed{
\text{Converges with signs but diverges without signs}
\Longrightarrow
\text{Conditional Convergence}
}
```

---

## 11. Determining Absolute or Conditional Convergence

When a problem asks whether a series is absolutely convergent, conditionally convergent, or divergent, use the following procedure.

### Step 1 — Test Absolute Convergence

Form:

```math
\sum_{n=1}^{\infty}|a_n|
```

Apply an appropriate positive-term convergence test.

Possible tests include:

- p-Series Test
- Geometric Series Test
- Direct Comparison Test
- Limit Comparison Test
- Integral Test

### Step 2 — Interpret the Result

If $\sum |a_n|$ converges:

```math
\boxed{\text{Absolutely Convergent}}
```

The original series must also converge.

If $\sum |a_n|$ diverges, continue to Step 3.

### Step 3 — Test the Original Series

If the original series is alternating, consider the Alternating Series Test.

If the original series converges:

```math
\boxed{\text{Conditionally Convergent}}
```

If the original series diverges:

```math
\boxed{\text{Divergent}}
```

### Decision Table

| Absolute-value series | Original series | Classification |
|---|---|---|
| Converges | Converges | Absolutely convergent |
| Diverges | Converges | Conditionally convergent |
| Diverges | Diverges | Divergent |

If the original series remains unclassified after the tests used, additional analysis is required.

---

## 12. Rearrangements of Infinite Series

A rearrangement changes the order of the terms in an infinite series without omitting or repeating terms.

For finite sums, changing the order does not change the result.

For infinite series, the situation depends on the type of convergence.

### Absolutely Convergent Series

Rearranging the terms of an absolutely convergent series does not change its sum.

```math
\boxed{
\text{Absolute Convergence}
\Longrightarrow
\text{Rearrangements Preserve the Sum}
}
```

### Conditionally Convergent Series

Rearranging the terms of a conditionally convergent series can change its sum.

The textbook illustrates this using the alternating harmonic series:

```math
1-\frac12+\frac13-\frac14+\cdots=\ln 2
```

A rearrangement that places two positive terms before each negative term produces a different sum:

```math
1+\frac13-\frac12+\frac15+\frac17-\frac14+\cdots
```

This rearranged series has sum:

```math
\frac32\ln 2
```

### Riemann Rearrangement Theorem

If a series is conditionally convergent, its terms can be rearranged so that the new series converges to any prescribed real number.

### Recognition Rule

```math
\boxed{
\begin{aligned}
\text{Absolute convergence}
&\Rightarrow\text{Sum preserved}\\
\text{Conditional convergence}
&\Rightarrow\text{Sum may change}
\end{aligned}
}
```

The order of infinitely many terms matters when convergence is conditional.

---

## 13. Limitations and Test Selection

The positive-term convergence tests from earlier sections cannot generally be applied directly to alternating terms.

### Important Distinctions

- The p-Series Test and Integral Test apply to positive-term series.
- Direct and Limit Comparison are used for nonnegative-term series.
- The Alternating Series Test addresses sign alternation.
- Taking absolute values allows positive-term tests to be used when investigating absolute convergence.
- The Test for Divergence applies to all series.

### Recognition Table

| Situation | Test to Consider |
|---|---|
| Terms alternate in sign | Alternating Series Test |
| Need to verify decreasing magnitudes | Compare $b_{n+1}$ and $b_n$ |
| Decreasing inequality is complicated | Derivative Test for monotonicity |
| Term limit is nonzero or nonexistent | Test for Divergence |
| Need an approximation error bound | Alternating Series Estimation Theorem |
| Asked about absolute convergence | Test $\sum |a_n|$ |
| Original converges but absolute-value series diverges | Conditional convergence |
| Rearrangement of a conditionally convergent series | Riemann Rearrangement Theorem |

---

## 14. Presenting a Complete Solution

### Alternating Series Test — Three Steps

**Step 1 — Identify the Alternating Series**

Write the series in the form:

```math
\sum_{n=1}^{\infty}(-1)^n b_n
```

or:

```math
\sum_{n=1}^{\infty}(-1)^{n-1}b_n
```

Identify the positive magnitude $b_n$.

**Step 2 — Verify Both Conditions**

Show that the magnitudes are eventually decreasing:

```math
b_{n+1}\leq b_n
```

Then evaluate:

```math
\lim_{n\to\infty}b_n
```

**Step 3 — State the Conclusion**

State explicitly whether the Alternating Series Test establishes convergence.

If the problem also asks about absolute or conditional convergence, perform that analysis separately.

---

## 15. Quick Reference — Memory Cues

### Alternating Series Test

```math
\boxed{
\begin{aligned}
b_{n+1}&\leq b_n\\
\lim_{n\to\infty}b_n&=0
\end{aligned}
\Rightarrow
\text{Convergent}
}
```

### Decreasing Terms

```math
\boxed{f'(x)<0\Rightarrow f(x)\text{ decreasing}}
```

### Alternating Series Error Bound

```math
\boxed{|s-s_n|\leq b_{n+1}}
```

### Absolute Convergence

```math
\boxed{
\sum |a_n|\text{ converges}
\Rightarrow
\sum a_n\text{ converges}
}
```

### Conditional Convergence

```math
\boxed{
\begin{aligned}
\sum a_n&\text{ converges}\\
\sum |a_n|&\text{ diverges}
\end{aligned}
}
```

### Rearrangements

```math
\boxed{
\begin{aligned}
\text{Absolutely convergent}
&\Rightarrow\text{Same sum}\\
\text{Conditionally convergent}
&\Rightarrow\text{Sum may change}
\end{aligned}
}
```

### Final Recognition Rule

```math
\boxed{
\text{Identify Signs}
\rightarrow
\text{Choose Test}
\rightarrow
\text{Verify Conditions}
\rightarrow
\text{State Conclusion}
}
```

Remember that alternating signs alone do not prove convergence. The term magnitudes must eventually decrease to zero for the Alternating Series Test to establish convergence.
