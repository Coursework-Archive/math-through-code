# SESSION 14 (11, 12, 16, 18, 21, 22, 23, 25, 26, 27) - mins
11
Simple disk method
Good warm-up
Reinforces writing the radius correctly.


## Pattern:
Careless errors when evaluating the final answer of a volume integral.

**Mistake:**

After correctly setting up the disk method and finding the antiderivative, I made two careless mistakes during the final evaluation:

1. I incorrectly treated

$$
(2)^2 + 2
$$

as

$$
2(2)^2 = 8,
$$

instead of

$$
4 + 2 = 6.
$$

This changed the correct value from

$$
\frac{26}{3}
$$

to

$$
\frac{32}{3}.
$$

2. I forgot to include the factor of

$$
\pi
$$

in the final answer, even though it was part of the original volume formula.

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

Before boxing a volume answer, perform a final check:
1. Verify the arithmetic after evaluating the bounds.
2. Make sure all constant factors (such as $\pi$, $\frac{1}{2}$, or coefficients) are carried through to the final answer.

---

12
Another straightforward disk problem with a reciprocal function.
Good practice integrating after the setup.

---

16
Rotation about the y-axis
Forces you to decide whether to integrate with respect to x or y.

## Pattern: Correct disk setup, arithmetic simplification error

Mistake:

I correctly used the disk method and set up the radius as $r(y)=\frac{y^2}{2}$. The integral and antiderivative were correct:

$$
V=\pi\int_0^4 \frac{y^4}{4}\,dy
=\pi\left[\frac{y^5}{20}\right]_0^4
$$

But when simplifying

$$
\frac{4^5}{20}=\frac{1024}{20},
$$

I accidentally changed the denominator to $48$ instead of simplifying $20$ correctly.

Correct simplification:

$$
\frac{1024}{20}
=
\frac{512}{10}
=
\frac{256}{5}
$$

So the correct answer is:

$$
\boxed{\frac{256\pi}{5}}
$$

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

When simplifying a fraction, divide the numerator and denominator by the same number; do not change the denominator from memory or mental shortcut.


--- 


18
Washer method.
Good practice determining outer vs. inner radius.

## Pattern:
Correctly set up the washer method but integrated the polynomial incorrectly, leading to the wrong final volume.

Mistake:
After expanding $(6-x^2)^2$, I integrated the $-12x^2$ term incorrectly.

I wrote

$$
\int -12x^2\,dx = -6x^2,
$$

but the correct antiderivative is

$$
\int -12x^2\,dx = -4x^3.
$$

The washer setup, radii, and bounds were all correct—the error was entirely in applying the power rule during integration.

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

When integrating a polynomial, integrate each term independently using the power rule: increase the exponent by one and divide by the new exponent. Before evaluating the bounds, verify that every term in the antiderivative has the correct exponent.

---



21
Rotation about y=1.
Excellent because the radius is distance to a line, not simply the function value.

---

22
Another shifted axis (y=−3).
Reinforces translating radii.


---


23
Trigonometric function.
Makes you think about radius first instead of immediately integrating.

## Pattern: Evaluating trigonometric functions at negative angles

Mistake:

When evaluating the antiderivative at the lower bound, I computed
$\tan\left(-\frac{\pi}{4}\right)$ incorrectly, which caused me to write
$-\pi-1$ instead of the correct value $-\pi+1$.

### Type

- [ ] Algebra
- [x] Concept
- [ ] Recognition
- [ ] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

For negative angles, either convert to the coterminal angle (e.g., $-\frac{\pi}{4}=\frac{7\pi}{4}$) or use the odd-function identity $\tan(-\theta)=-\tan(\theta)$. Always evaluate the trigonometric function first, then substitute it into the antiderivative before simplifying the signs.

---


25
Rotation about x=2.
Excellent practice for horizontal axes.

---

26
Rotation about x=−1.
Another translated-axis problem that strengthens setup.

## Pattern:
Shell method with a vertical axis of rotation.

Mistake:
I initially wrote the shell radius as \(-1 - x\) instead of measuring the positive distance from the axis to the slice. I also briefly forgot that \(\int \frac{1}{x}\,dx=\ln|x|\).

### Type

- [ ] Algebra
- [x] Concept
- [ ] Recognition
- [ ] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

For shell problems, the radius is always the **positive distance from the axis of rotation to the slice**. Determine which is farther to the right (or higher) and compute **right − left**. After simplifying the integrand, remember that \(\int \frac{1}{x}\,dx=\ln|x|\).

---

## Pattern:
Integrals involving $\frac{1}{x}$.

Mistake:
After simplifying the integrand to $1+\frac{1}{x}$, I did not immediately recognize that the antiderivative of $\frac{1}{x}$ is $\ln|x|$ and initially tried to apply the power rule.

### Type

- [ ] Algebra
- [ ] Concept
- [x] Recognition
- [ ] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

Always check for the special antiderivative $\frac{1}{x}$. The power rule does **not** apply when the exponent is $-1$; instead,

$$
\int \frac{1}{x}\,dx=\ln|x|+C.
$$

---


27
Similar level to your assigned #24.
Nice capstone combining all previous ideas.






Total for 6/31 (45 mins)
Total for 7/1 (40 mins)
Total for 7/3 (2 hours)
Total Study Cumulative Time (21 hrs 40 mins)