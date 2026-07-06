# Section 5.5 The Substitution Rule
---
## TIER 1
### Algebraic substitutions (10, 11, 21, 23, 24)
### Exponential and logarithmic substitutions (20, 31, 35, 36, 48)
### Trigonometric substitutions (17, 19, 38, 41, 45)
### Definite integrals with u-substitution (59, 60, 63, 64, 68)

---

## TIER 2
### Composition of functions  (22, 26, 29, 32, 42, 43, 44, 46, 49)
### Definite integrals (61, 62, 65, 67, 69, 74, 76, 79, 80)

---

## TIER 3
### Area interpretation (83, 84, 85)
### Symmetry and substitution (97, 98, 99, 100)
### Applications (86, 87, 88, 89, 90, 91, 92)

---

# SESSION 4 (10, 11, 17, 19, 20, 21, 23) - 1 hr

## Pattern:

Mistake:

I correctly recognized the denominator as the substitution

$$
u=1+\sin\theta,
$$

but when differentiating I dropped the differential and wrote

$$
du=\cos\theta
$$

instead of

$$
du=\cos\theta\,d\theta.
$$

As a result, I became confused about how to replace the numerator and differential in the integral.

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

When differentiating a substitution, always carry the differential. The entire quantity involving the derivative and the original differential becomes the new differential.

### Cue

**Never drop the original differential.**

Example:

$$
u=1+\sin\theta
$$

$$
du=\cos\theta\,d\theta
$$

so

$$
\cos\theta\,d\theta=du
$$

and

$$
\int\frac{\cos\theta}{1+\sin\theta}\,d\theta
=
\int\frac{1}{u}\,du.
$$


---

## Pattern:

Mistake:

Substituted correctly with

$$
v = 1-e^u
$$

and

$$
dv=-e^u\,du,
$$

but failed to replace the entire numerator

$$
e^u\,du
$$

with

$$
-dv.
$$

As a result, an extra factor of

$$
e^u
$$

was left in the integral, making the substitution inconsistent.

### Type

- [ ] Algebra
- [x] Concept
- [x] Recognition
- [ ] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

When performing substitution, replace **all occurrences** of the inside function's derivative. If

$$
dv=f'(x)\,dx,
$$

then the entire expression

$$
f'(x)\,dx
$$

must disappear from the integral.

---

### Original Problem

$$
\int \frac{e^u}{(1-e^u)^2}\,du
$$

### Substitution

Let

$$
v=1-e^u
$$

Then

$$
dv=-e^u\,du
$$

so

$$
e^u\,du=-dv.
$$

### Correct Integral

$$
\int \frac{e^u}{(1-e^u)^2}\,du
=
-\int \frac{1}{v^2}\,dv
=
-\int v^{-2}\,dv
$$

### Integration

$$
-\left(\frac{v^{-1}}{-1}\right)+C
=
v^{-1}+C
$$

### Final Answer

$$
\boxed{\frac{1}{1-e^u}+C}
$$

### Recognition Cue

Look for

$$
\frac{f'(x)}{(f(x))^n}
$$

and let

$$
v=f(x).
$$

Then rewrite the integral entirely in terms of $v$ and $dv$ before integrating.

---

## Pattern:

Forgetting to divide by the derivative factor during $u$-substitution.

Mistake:

I correctly chose

$$
u=3ax+bx^3
$$

and found

$$
du=3(a+bx^2)\,dx
$$

but I treated this like the integral needed a factor of $3$ instead of $\frac{1}{3}$.

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

When $du=k\cdot(\text{matching part})\,dx$, replace the matching part with $\frac{1}{k}du$, not $kdu$.

---

## Pattern:

Forgot the $\ln(a)$ factor when differentiating an exponential function of the form $a^x$.

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

When differentiating $a^x$, always include the $\ln(a)$ factor:

$$
\frac{d}{dx}\left(a^x\right)=a^x\ln(a).
$$

Therefore, for substitution problems,

$$
u=a^x+c
$$

implies

$$
du=a^x\ln(a)\,dx,
$$

so

$$
a^x\,dx=\frac{du}{\ln(a)}.
$$

Example:

$$
\int \frac{2^t}{2^t+3}\,dt
$$

Let

$$
u=2^t+3,
$$

then

$$
du=2^t\ln(2)\,dt,
$$

and

$$
2^t\,dt=\frac{du}{\ln(2)}.
$$

Thus

$$
\int \frac{2^t}{2^t+3}\,dt
=
\frac{1}{\ln(2)}
\int \frac{1}{u}\,du
=
\boxed{
\frac{\ln(2^t+3)}{\ln(2)}+C
}.
$$

---

# SESSION 5 (22, 24, 26, 29, 31, 32, 35) - 1 hr 30 mins 

No errors !!

---

# SESSION 6 (36, 38, 41, 42, 43, 44, 45) - 50 mins

## Pattern:

Forgetting to substitute back the complete power after integrating.

Mistake:

After integrating

$$
-\int u^{1/2}\,du
=
-\frac23u^{3/2}+C
$$

I substituted back only $\cot x$ instead of $(\cot x)^{3/2}$.

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

When substituting back, rewrite the entire expression in terms of the original variable before boxing the answer.

---

## Confidence (1-10): 8

### Reality Check

If tested right now I would score:

8/10

Strength:

Recognizing the correct $u$-substitution and carrying out the integration correctly.

Weakness:

Dropping exponents or pieces of expressions during the final substitution step.

Adjustment for next session:

Pause before boxing the answer and verify that every power and coefficient has been restored.

Focus on:

Careful back-substitution and checking the final answer by differentiating mentally.

Reduce time on:

Finding substitutions; recognition of $u$ and computation are becoming strong.

---

## Pattern

Forgot part of the derivative during $u$-substitution.

### Problem

$$
\int \frac{\sin 2x}{1+\cos^2x}\,dx
$$

with

$$
u=1+\cos^2x
$$

### Mistake

Dropped the derivative of $\cos x$ and missed the negative sign.

Incorrectly treated

$$
du=\sin 2x\,dx
$$

instead of

$$
du=-\sin 2x\,dx.
$$

### Type

- [ ] Algebra
- [x] Concept
- [x] Recognition
- [ ] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

Always differentiate the **entire inside function**, including chain rule factors and signs, before replacing with $du$.

### Reality Check

Since

$$
u=1+\cos^2x,
$$

we have

$$
du=2\cos x(-\sin x)\,dx
=-2\sin x\cos x\,dx
=-\sin 2x\,dx.
$$

### Warning Sign

Whenever $u$ contains

- $\cos(\cdot)$
- $\sin(\cdot)$
- powers such as $(\cos x)^2$
- exponentials such as $e^x$
- logarithms

pause and ask:

> "Did I differentiate the whole inside, including constants and signs?"

### Memory Cue

**Choose $u$ → Differentiate completely → THEN substitute.**

Never replace with $du$ until the chain rule is finished.


---

## Pattern

Missed the exponent on a trigonometric function.

### Mistake

I read $\csc^2(u)$ as $\csc(u)$, so I used the antiderivative for $\csc u$ instead of $\csc^2 u$.

### Type

- [ ] Algebra
- [ ] Concept
- [x] Recognition
- [x] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

Before choosing an antiderivative, check whether the trig function has a power.

$\csc u$ and $\csc^2 u$ are different patterns:

$$
\int \csc u\,du=\ln|\csc u-\cot u|+C
$$

$$
\int \csc^2 u\,du=-\cot u+C
$$

### Cue

Power first, antiderivative second.


# SESSION 7 (46, 48, 49, 59, 60, 61, 62) - 1 hr 30 mins

## Pattern

Mistake:

For a definite integral involving a composite function,

$$
\int_0^1 \cos\left(\frac{\pi t}{2}\right)\,dt,
$$

I correctly chose

$$
u=\frac{\pi t}{2},
$$

but became confused because the derivative

$$
du=\frac{\pi}{2}\,dt
$$

did not appear explicitly in the integrand.

I expected to see a factor of

$$
\frac{\pi}{2}
$$

already present and was unsure how to continue.

### Type

- [ ] Algebra
- [x] Concept
- [x] Recognition
- [ ] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

If the derivative of the inside function is a constant, solve for the differential:

$$
du=k\,dx
\quad\Rightarrow\quad
dx=\frac1k\,du.
$$

The missing constant becomes a coefficient outside the integral.

---

### Original Problem

$$
\int_0^1 \cos\left(\frac{\pi t}{2}\right)\,dt
$$

### Substitution

Let

$$
u=\frac{\pi t}{2}
$$

Then

$$
du=\frac{\pi}{2}\,dt
$$

so

$$
dt=\frac{2}{\pi}\,du.
$$

### Change the Limits

When

$$
t=0,
$$

then

$$
u=0.
$$

When

$$
t=1,
$$

then

$$
u=\frac{\pi}{2}.
$$

---

## Pattern

Uncertainty about handling limits after performing $u$-substitution in a definite integral.

### Problem

$$
\int_0^1 (3t-1)^{50}\,dt
$$

### Mistake

I correctly chose

$$
u=3t-1
$$

and found

$$
du=3\,dt,
\qquad
dt=\frac13\,du,
$$

but became unsure about what to do next.

I was uncertain whether I should

- substitute back to $t$, or
- change the limits of integration and remain in terms of $u$.

This caused confusion after the integration step.

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

For definite integrals, there are two valid approaches:

1. Change the bounds immediately and stay in the new variable.

or

2. Integrate in terms of $u$, substitute back to the original variable, and then evaluate using the original bounds.

Never mix $u$-values with the original variable's limits.

### Correct Method

Let

$$
u=3t-1,
$$

so

$$
du=3\,dt,
\qquad
dt=\frac13\,du.
$$

Change the bounds:

When $t=0$,

$$
u=3(0)-1=-1.
$$

When $t=1$,

$$
u=3(1)-1=2.
$$

Therefore,

### Warning Sign

If I find myself asking

> "Should I plug back in?"

I should first ask:

> "Is this a definite integral?"

If the answer is yes, changing the limits is usually the cleanest approach.

### Memory Cue

**Indefinite integral → substitute back.**

**Definite integral → change the bounds.**


---

## Pattern

Mixed original bounds with a substituted $u$-expression in a definite integral.

### Mistake

I correctly used substitution and rewrote the integral in terms of $u$, but when evaluating the definite integral, I plugged the original bounds back into the $u$ expression instead of using the converted $u$-bounds.

In other words, after changing to $u$, I evaluated something like

$$
F(u)\Big|_0^1
$$

even though the bounds $0$ and $1$ belonged to the original variable, not to $u$.

### Type

- [ ] Algebra
- [x] Concept
- [ ] Recognition
- [x] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

Once the integral is rewritten in terms of $u$, the bounds must also be rewritten in terms of $u$.

Use either:

$$
F(u)\Big|_{u(a)}^{u(b)}
$$

or substitute back first and use

$$
F(x)\Big|_a^b.
$$

Do not mix them.

### Correct Process

If

$$
u=f(x),
$$

then

$$
\int_a^b g(f(x))f'(x)\,dx
=
\int_{f(a)}^{f(b)} g(u)\,du.
$$

So after substituting,

$$
x=a \Rightarrow u=f(a)
$$

and

$$
x=b \Rightarrow u=f(b).
$$

### Warning Sign

If my antiderivative is written in terms of $u$, but my bounds are still the original numbers from $x$ or $t$, pause.

That means I am about to mix variables.

### Memory Cue

**One variable at a time.**

Either:

$$
u\text{-expression with }u\text{-bounds}
$$

or

$$
x\text{-expression with }x\text{-bounds}.
$$

Never:

$$
u\text{-expression with }x\text{-bounds}.
$$

---

## Pattern:

Definite integral with u-substitution and a negative derivative.

Mistake:

Forgot to account for the negative sign from

$$
du=-\frac1{x^2}dx
$$

which caused the answer to have the wrong sign.

### Type

- [ ] Algebra
- [x] Concept
- [x] Recognition
- [ ] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

If $du$ introduces a minus sign, either keep the minus sign outside the integral or reverse the new bounds and remove the minus sign.

---

## Confidence (1-10): 7

### Reality Check

If tested right now I would score:

7/10

Strength:

I recognized the substitution

$$
u=\frac1x
$$

and correctly converted the bounds.

Weakness:

I did not recognize that the negative derivative changes the orientation of the integral.

Adjustment for next session:

Practice several definite integrals where $u$ is a decreasing function.

Focus on:

- Negative $du$
- Reversing bounds
- Converting limits from $x$ to $u$

Reduce time on:

Finding substitutions; the substitution itself was correct.

---

## Recognition Pattern

If

$$
du=-g(x)\,dx
$$

then immediately ask:

"Will I keep the minus sign, or reverse the bounds?"

These two are equivalent:

$$
-\int_a^b f(u)\,du
=
\int_b^a f(u)\,du
$$

---


# SESSION 8 (63, 64, 65, 67, 68, 69, 74) - 1 hr 30 mins

## Pattern:

Moving constants incorrectly when solving for \(dx\) in a substitution.

### Problem

$$
\int_1^4 \frac{\sqrt{2+\sqrt{x}}}{\sqrt{x}}\,dx
$$

with

$$
u=2+\sqrt{x}
$$

### Mistake

I correctly found

$$
du=\frac{1}{2\sqrt{x}}\,dx
$$

but when solving for

$$
\frac{1}{\sqrt{x}}\,dx,
$$

I treated the coefficient incorrectly and effectively lost a factor of \(2\).

As a result, I used

$$
\frac{1}{\sqrt{x}}\,dx=du
$$

instead of

$$
\frac{1}{\sqrt{x}}\,dx=2\,du.
$$

This caused the final answer to be one-half of the correct value.

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

When

$$
du=k\cdot(\text{matching expression}),
$$

solve for the matching expression by dividing by \(k\):

$$
\text{matching expression}
=
\frac{1}{k}du.
$$

If

$$
du=\frac12\left(\frac{1}{\sqrt{x}}dx\right),
$$

then

$$
\frac{1}{\sqrt{x}}dx=2du.
$$

### Reality Check

Starting from

$$
u=2+\sqrt{x},
$$

we have

$$
du=\frac{1}{2\sqrt{x}}dx
=\frac12\left(\frac1{\sqrt{x}}dx\right).
$$

Multiplying both sides by \(2\) gives

$$
\frac1{\sqrt{x}}dx=2du.
$$

Therefore,

$$
\int_1^4\frac{\sqrt{2+\sqrt{x}}}{\sqrt{x}}dx
=
2\int_3^4u^{1/2}du.
$$

### Warning Sign

Whenever the derivative contains fractions, stop and ask:

> "What expression am I trying to isolate?"

Then solve algebraically before substituting.

### Memory Cue

**Isolate the entire matching piece before replacing it with \(du\).**

Never substitute until the quantity multiplying \(du\) has been solved for completely.

---

## Pattern:

Dropped the reciprocal factor from the power rule after integrating \(u^{1/2}\).

Mistake:

For

\[
\frac14\int_1^9\left(u^{1/2}-u^{-1/2}\right)\,du
\]

I wrote

\[
u^{3/2}-2u^{1/2}
\]

instead of

\[
\frac23u^{3/2}-2u^{1/2}.
\]

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

Always divide by the new exponent when using the power rule:

\[
\int u^n\,du=\frac{u^{n+1}}{n+1}+C.
\]

Never drop the reciprocal factor.

---

## Confidence (1-10): 7

### Reality Check

If tested right now I would score:

7/10

Strength:

- Correctly recognized the substitution.
- Correctly converted the bounds.
- Correctly solved for the leftover \(x\).
- Correctly rewrote the integrand in terms of \(u\).

Weakness:

- Forgot to keep the factor

\[
\frac{1}{3/2}=\frac23
\]

when integrating \(u^{1/2}\).

Adjustment for next session:

After every power-rule step, pause and ask:

> "Did I divide by the new exponent?"

Focus on:

- Power rule coefficients.
- Evaluating fractional exponents.

Reduce time on:

- Choosing \(u\), since pattern recognition for substitution is improving.

---

### Memory Cue

**Power Rule = Add 1, THEN Divide.**

Not

> Add 1 and stop.

but

> Add 1 → Divide by the new exponent → Simplify.

---

### SESSION 9 (76, 79, 80, 83, 84, 85) - 40 mins
made it through 84, all problems I had to ask how to solve, this is new material for me. 


---

### SESSION 10 (97, 98, 99, 100) - mins
Will complete after 


---

Total for 6/20 ( 1 hr 30 mins) 
Total for 6/21 (4 hr 20 mins)
Total for 6/22 (1 hr 40 mins)
Total Study Cumulative Time (11 hrs 45 mins)





