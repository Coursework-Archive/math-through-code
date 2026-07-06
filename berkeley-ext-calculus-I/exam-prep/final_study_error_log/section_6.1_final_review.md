# SESSION 11 (5, 6, 9, 15, 17, 20, 23, 27, 31, 34) - 2 hr 30 mins

## Pattern: Area between curves with split integral

Mistake: I correctly split the area into two integrals, but I did not simplify the integrands first. Then, when evaluating the first interval, I handled the negative terms incorrectly by subtracting instead of adding the negatives.

### Type

- [x] Algebra
- [ ] Concept
- [ ] Recognition
- [x] Careless

### Fixed?

- [ ] Yes
- [x] Partial
- [ ] No

### Fix Rule

After splitting the area integral, simplify each integrand first, then evaluate carefully using:

$$
F(b)-F(a)
$$

not just “subtract the numbers.”


## Correct Setup

$$
A=\int_{-2}^{0}\left[(x^3-3x)-x\right]dx+\int_{0}^{2}\left[x-(x^3-3x)\right]dx
$$

Simplify before integrating:

$$
A=\int_{-2}^{0}(x^3-4x)\,dx+\int_{0}^{2}(4x-x^3)\,dx
$$

For the first integral:

$$
\int_{-2}^{0}(x^3-4x)\,dx
=
\left[\frac{x^4}{4}-2x^2\right]_{-2}^{0}
$$

$$
=0-\left(\frac{16}{4}-2(4)\right)
$$

$$
=0-(4-8)
$$

$$
=0-(-4)
$$

$$
=4
$$

Key sign check:

$$
0-(-4)=0+4=4
$$

---

## Pattern:

Most mistakes occur after the setup is already correct.

### Type

- [x] Algebra
- [ ] Concept
- [ ] Recognition
- [x] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

Slow down after the setup.

The setup earns the points; do not rush the antiderivative and evaluation.

---

## Pattern:

Coefficient simplification after distributing a constant outside the integral.

### Type

- [x] Algebra
- [ ] Concept
- [ ] Recognition
- [ ] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

After distributing a constant outside an integral, simplify each coefficient carefully before evaluating.

### Work

Starting from

$$
2\left[\frac{3}{4}(2x)^{4/3}-\frac{1}{4}x^2\right]_0^4
$$

distribute the factor of \(2\):

$$
\left[\frac{6}{4}(2x)^{4/3}-\frac{2}{4}x^2\right]_0^4
$$

Simplify the coefficients:

$$
\left[\frac{3}{2}(2x)^{4/3}-\frac{1}{2}x^2\right]_0^4
$$

Mistake:

$$
\frac{6}{4}
\rightarrow
\frac{3}{4}
\qquad\text{(incorrect)}
$$

Correct simplification:

$$
\frac{6}{4}
=
\frac{3}{2}
$$

### Reality Check

When simplifying fractions, divide the numerator and denominator by the same number:

$$
\frac{6}{4}
=
\frac{6\div2}{4\div2}
=
\frac{3}{2}.
$$

A coefficient that becomes smaller after multiplying by \(2\) should immediately be questioned.

---

## Pattern:

Mistake:

At \(x=\frac{\pi}{2}\),

$$
-\frac12\cos(\pi)-\sin\left(\frac{\pi}{2}\right)
$$

was copied/evaluated as

$$
-1-1
$$

instead of

$$
+\frac12-1=-\frac12.
$$

### Type

- [ ] Algebra
- [ ] Concept
- [ ] Recognition
- [x] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

Evaluate each term separately and write the numerical value of every trig function before combining signs.

---

## Pattern:

Mistake:

While evaluating the bounds,

$$
-\frac14-\frac24
$$

was combined incorrectly.

Correct subtraction:

$$
-\frac14-\frac24
=
-\left(\frac14+\frac24\right)
=
-\frac34.
$$

### Type

- [ ] Algebra
- [ ] Concept
- [ ] Recognition
- [x] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

When subtracting a negative quantity, keep the minus sign attached to the entire fraction and combine numerators only after confirming the sign of each term.

---


# SESSION 12 (38, 43, 44, 49, 50, 52) - 2 hrs 0 mins

## Pattern:

Tried to combine complicated functions into a single fraction or expression before integrating instead of integrating each term separately.

### Mistake

While solving area problems (especially #38), I tried to force the integrand into one expression by finding a common denominator or simplifying radicals. This created unnecessary algebra and made the problem much harder than it needed to be.

### Type

- [x] Algebra
- [x] Recognition
- [ ] Concept
- [ ] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

If the integrand is a sum or difference of functions that each have a recognizable antiderivative, integrate each term separately before attempting any algebraic simplification.
 
### Example

Instead of trying to simplify

$$
\int\left(\frac{x}{\sqrt{1+x^2}}-\frac{x}{\sqrt{9-x^2}}\right)\,dx,
$$

write

$$
\int\frac{x}{\sqrt{1+x^2}}\,dx
-
\int\frac{x}{\sqrt{9-x^2}}\,dx,
$$

and solve each integral using its own substitution.

### Why it Happened

I was applying my polynomial habit of simplifying everything first. That strategy does not generalize well to radicals, exponentials, logarithms, or trigonometric functions.

### Recognition Cue

If I see:
- radicals,
- exponentials,
- logarithms,
- trig or hyperbolic functions,

I should first ask:

> **Can I integrate each term separately?**

If the answer is yes, **do not combine the expressions.**

### Confidence

Before: 4/10

After: 9/10







# SESSION 13 (6, 17, 27, 31, 44, 50) - mins

## Pattern:

Transcribed the upper evaluation bound as **3** instead of **2**, causing the correct setup and algebra to produce the wrong final answer.

### Type

- [ ] Algebra
- [ ] Concept
- [ ] Recognition
- [x] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

Circle or underline the bounds immediately after setting up the definite integrals, then verify the evaluation bounds match the original integral before substituting values.

---

## Pattern:

Evaluated the antiderivative using the original interval after already using symmetry.

### Type

- [ ] Algebra
- [ ] Concept
- [ ] Recognition
- [x] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

If I use symmetry (multiply the integral by 2), I must also change the bounds to the reduced interval before evaluating. Always compare the evaluation bounds with the final integral immediately before substitution.


Total for 6/23 (1 hr 30 mins)
Total for 6/24 (1 hr)
Total for 6/25 (30 mins)
Total for 6/26 (1 hr 30 mins)
Total for 6/30 (2 hr 0 mins)
Total Study Cumulative Time (18 hrs 15 mins)