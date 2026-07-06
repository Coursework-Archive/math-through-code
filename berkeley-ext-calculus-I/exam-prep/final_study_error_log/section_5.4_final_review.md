# SESSION 1 (14, 15, 18, 20, 21, 24, 25) - 1 hour 

Core antiderivative patterns
Skills Covered
Power rule
Fraction splitting
Negative exponents
Logarithms
Exponential functions
Trig identities
Simplifying before integrating
Family of antiderivatives

---

## Pattern

Polynomial multiplied by a radical.

Problem:

5.4 #14

Mistake:

Arithmetic error when simplifying the coefficient after applying the power rule.

#### Type:
- [x] Algebra
- [ ] Concept
- [ ] Recognition
- [ ] Careless

#### Fixed?:
- [x] Yes
- [ ] Partial
- [ ] No

#### Fix Rule:

After applying the power rule, simplify coefficients separately before writing the final answer.

---

## Confidence (1–10): 9

### How I Rated It:
- [x] 8–10 → I can solve correctly under test conditions
- [ ] 6–7 → I understand but might make mistakes
- [ ] 4–5 → I need more reps
- [ ] 1–3 → I don't reliably know what to do

---

### Reality Check

If tested right now, I would likely score:

9/10

### Reason for Score:

Strength:
Recognized the radical as a fractional exponent and distributed correctly.

Weakness:
Minor arithmetic simplification error.

---

### Adjustment for Next Session:

Focus on:
Checking coefficients after using the power rule.

Reduce time on:
Expanding products involving radicals.

---

---

## Pattern

Fraction with terms divided by x.

Problem:

5.4 #15

Mistake:

Missed that the term \(1/x\) has natural log as its antiderivative.

#### Type:
- [ ] Algebra
- [ ] Concept
- [x] Recognition
- [ ] Careless

#### Fixed?:
- [ ] Yes
- [x] Partial
- [ ] No

#### Fix Rule:

Whenever the power is \(x^{-1}\), do not use the power rule; use \(\int \frac{1}{x}\,dx=\ln|x|+C\).

---

## Confidence (1–10): 7

### Reality Check

If tested right now, I would likely score:

7/10

### Reason for Score:

Strength:
Correctly split the fraction and integrated the other terms.

Weakness:
Need faster recognition of the special \(x^{-1}\) case.

---

### Adjustment for Next Session:

Focus on:
Spotting \(1/x\), \(x^{-1}\), and split fractions before integrating.

Reduce time on:
Basic power rule terms where \(n \ne -1\).

---

## Pattern

Special antiderivative of \(1/x\).

Problem:

5.4 #20

Mistake:

Integrated \(2r^{-1}\) as \(2/\ln|r|\) instead of \(2\ln|r|\).

#### Type:
- [ ] Algebra
- [x] Concept
- [ ] Recognition
- [ ] Careless

#### Fixed?:
- [x] Yes
- [ ] Partial
- [ ] No

#### Fix Rule:

Whenever the power is \(-1\),

$$
\int x^{-1}\,dx=\ln|x|+C
$$

Do **not** divide by the logarithm.

---

## Confidence (1–10): 8

### Reality Check

Strength:
Correctly rewrote the fraction and expanded the square.

Weakness:
Need to remember that the logarithm is the answer, not the denominator.

---

### Adjustment for Next Session:

Focus on:
Special antiderivative

$$
\int \frac1x\,dx=\ln|x|+C
$$

Reduce time on:
Algebraic expansion, which is already strong.

---

## Pattern

Trig identity before integrating.

Problem:

5.4 #21

Mistake:

Did not know how to integrate \(\tan^2\theta\) directly.

#### Type:
- [ ] Algebra
- [x] Concept
- [x] Recognition
- [ ] Careless

#### Fixed?:
- [ ] Yes
- [x] Partial
- [ ] No

#### Fix Rule:

Rewrite \(\tan^2\theta\) as \(\sec^2\theta-1\) before integrating.

---

## Pattern

Trig identity before integrating.

Problem:

5.4 #24

Mistake:

Did not immediately recognize the double-angle identity \(\sin 2x = 2\sin x\cos x\).

#### Type:
- [ ] Algebra
- [ ] Concept
- [x] Recognition
- [ ] Careless

#### Fixed?:
- [x] Yes
- [ ] Partial
- [ ] No

#### Fix Rule:

When \(\sin 2x\) appears, rewrite it as \(2\sin x\cos x\) before integrating.

---

# SESSION 2 (31, 33, 35, 36, 37, 38, 44, 45) - 1 hr 15 mins
Skills Covered
Definite integrals
Rational functions
Logarithms
Radicals
Arctangent
Secant squared
Exponentials
Trigonometric identities

## Error Template – Problem 31

### Error Type
Transcription error.

### Work Correct Through

Expand:

$$
(2x-3)(4x^2+1)
=8x^3-12x^2+2x-3
$$

Integrate:

$$
\int_0^2(8x^3-12x^2+2x-3)\,dx
=
\left[
2x^4-4x^3+x^2-3x
\right]_0^2
$$

### Error

While evaluating at \(x=2\), I accidentally transcribed

$$
2(2)^4
$$

as

$$
2(2)^2,
$$

which produced an incorrect intermediate value.

### Correction

Use the correct exponent:

$$
2(2)^4
=
2(16)
=
32.
$$

Therefore,

$$
\begin{aligned}
F(2)-F(0)
&=
2(2)^4-4(2)^3+(2)^2-3(2)\\
&=
32-32+4-6\\
&=
-2.
\end{aligned}
$$

### Correct Answer

$$
\boxed{-2}
$$

---

## Error Template – Problem 33

### Error Type
Arithmetic error during evaluation of the definite integral.

### Work Correct Through

Simplify the integrand:

$$
\frac{3x^2+4x+1}{x}
=
3x+4+\frac1x
$$

Integrate:

$$
F(x)
=
\frac{3x^2}{2}+4x+\ln|x|.
$$

Evaluate:

$$
F(3)
=
\frac{51}{2}+\ln3
$$

and

$$
F(1)
=
\frac{11}{2}.
$$

### Error

While subtracting the endpoint values, I computed

$$
\frac{51}{2}-\frac{12}{2}
=
\frac{39}{2},
$$

using an incorrect value for $F(1)$.

### Correction

Since

$$
F(1)
=
\frac32+4+\ln1
=
\frac{11}{2},
$$

the difference is

$$
\left(\frac{51}{2}+\ln3\right)
-
\frac{11}{2}
=
\frac{40}{2}+\ln3
=
20+\ln3.
$$

### Correct Answer

$$
\boxed{20+\ln3}
$$

---  

## Error Template – Problem 35

### Error Type
Arithmetic error during evaluation.

### Work Correct Through

Rewrite the integrand:

$$
\frac{4+6u}{\sqrt{u}}
=
4u^{-1/2}+6u^{1/2}
$$

Integrate:

$$
F(u)
=
8u^{1/2}+4u^{3/2}
$$

Evaluate at the endpoints:

$$
F(4)
=
8(4)^{1/2}+4(4)^{3/2}
$$

and

$$
F(1)
=
8(1)^{1/2}+4(1)^{3/2}.
$$

### Error

While evaluating at $u=4$, I computed

$$
4(4)^{3/2}
$$

as

$$
8
$$

instead of multiplying by the coefficient 4.

### Correction

Since

$$
(4)^{3/2}=8,
$$

we have

$$
4(4)^{3/2}=4(8)=32.
$$

Therefore,

$$
F(4)=8(2)+32=48
$$

and

$$
F(1)=8+4=12.
$$

Hence,

$$
48-12=36.
$$

### Correct Answer

$$
\boxed{36}
$$

---

---

## Pattern

Arctangent antiderivative.

Problem:

5.4 #36

Mistake:

Did not immediately recognize the form \(\frac{1}{1+x^2}\).

#### Type:
- [ ] Algebra
- [ ] Concept
- [x] Recognition
- [ ] Careless

#### Fixed?:
- [ ] Yes
- [x] Partial
- [ ] No

#### Fix Rule:

Whenever the denominator is \(1+x^2\), check for the arctangent pattern: \(\int \frac{1}{1+x^2}\,dx=\arctan x+C\).

---

## Simplifying Fractional Powers

Given

\[
\frac{2}{3}\left(\frac{\pi}{2}\right)^{3/2}
\]

### Step 1: Use the meaning of the exponent

Recall

\[
a^{3/2}=(\sqrt{a})^3
\]

so

\[
\left(\frac{\pi}{2}\right)^{3/2}
=
\left(\sqrt{\frac{\pi}{2}}\right)^3
\]

### Step 2: Rewrite the square root

\[
\sqrt{\frac{\pi}{2}}
=
\frac{\sqrt{\pi}}{\sqrt{2}}
\]

Therefore

\[
\left(\frac{\pi}{2}\right)^{3/2}
=
\left(\frac{\sqrt{\pi}}{\sqrt{2}}\right)^3
=
\frac{\pi\sqrt{\pi}}{2\sqrt{2}}
\]

### Step 3: Multiply by \(\frac{2}{3}\)

\[
\frac{2}{3}\left(\frac{\pi}{2}\right)^{3/2}
=
\frac{2}{3}\cdot\frac{\pi\sqrt{\pi}}{2\sqrt{2}}
=
\frac{\pi\sqrt{\pi}}{3\sqrt{2}}
\]

### Step 4 (Optional): Rationalize the denominator

Multiply by

\[
\frac{\sqrt{2}}{\sqrt{2}}
\]

to obtain

\[
\frac{\pi\sqrt{\pi}}{3\sqrt{2}}
=
\frac{\pi\sqrt{2\pi}}{6}
\]

Thus

\[
\boxed{
\frac{2}{3}\left(\frac{\pi}{2}\right)^{3/2}
=
\frac{\pi\sqrt{\pi}}{3\sqrt{2}}
=
\frac{\pi\sqrt{2\pi}}{6}
}
\]

### Fix Rule

Whenever an expression contains

\[
(a/b)^{3/2},
\]

think

\[
(a/b)^{3/2}
=
\left(\sqrt{\frac{a}{b}}\right)^3
\]

and simplify before boxing the final answer.

---

## Pattern:

Forgot to evaluate and subtract the lower limit when applying the Fundamental Theorem of Calculus.

Mistake:

I correctly found the antiderivative and evaluated the upper limit, but I stopped before subtracting the value at $x=0$. This caused me to miss that

$$
3e^0-4\sec(0)=3-4=-1,
$$

and subtracting this lower value adds $+1$ to the answer.

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

Always evaluate the antiderivative at both bounds and compute upper value minus lower value.

---

## Pattern:

Mistake:

Did not subtract the negative value correctly when evaluating \(F(3)-F(5/3)\).

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

When subtracting a negative lower-bound value, rewrite it as addition before combining fractions.

---

# SESSION 3 (57, 58, 59, 61, 63, 68, 69, 70, 71, 72, 73)

## Pattern:

Mistake:

Forgot to evaluate the antiderivative correctly at the upper bound after integrating with respect to \(y\). I treated

$$
\left[\frac{y^5}{5}\right]_0^1
$$

as \(1-0\) instead of

$$
\frac{1^5}{5}-\frac{0^5}{5}.
$$

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

When evaluating a definite integral, substitute the bounds into the entire antiderivative, including coefficients and exponents, before simplifying.

### Example

Incorrect:

$$
\left[\frac{y^5}{5}\right]_0^1
=1-0
=1
$$

Correct:

$$
\left[\frac{y^5}{5}\right]_0^1
=
\frac{1^5}{5}-\frac{0^5}{5}
=
\frac15.
$$

---

## Pattern:

Mistake:

Used the rod length incorrectly and attached the wrong units to the final answer.

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

For density problems, integrate over the physical length of the object and remember that integrating kg/m over meters produces kilograms.

---

Conceptual understanding
Skills Covered
Areas with respect to y
Interpretation of integrals
Velocity and displacement
Distance traveled
Acceleration → velocity
Density and mass
Marginal revenue
Rate problems

covers sessions 1 through 3 
Total for 6/14 (1 hr 30 mins)
Total for 6/19 (1 hr 15 mins)
Total for 6/20 (2 hr)
Total Study Cumulative Time (4 hrs 45 mins)