# Antiderivatives Cheat Sheet

Whenever $u$ contains trigonometric functions, powers, exponentials, or logarithms, pause and ask:

> Did I differentiate the entire inside expression, including constants and signs?

### Memory Cue

**Choose $u$ → differentiate completely → substitute.**

---

## Basic Antiderivatives

| Function $f(x)$ | Antiderivative $\int f(x)\,dx$ |
|---|---|
| $c$ | $cx+C$ |
| $x^n,\;n\ne -1$ | $\dfrac{x^{n+1}}{n+1}+C$ |
| $\dfrac{1}{x}$ | $\ln\lvert x\rvert+C$ |
| $e^x$ | $e^x+C$ |
| $b^x$ | $\dfrac{b^x}{\ln b}+C$ |

---

## Trigonometric Antiderivatives

| Function $f(x)$ | Antiderivative $\int f(x)\,dx$ |
|---|---|
| $\cos x$ | $\sin x+C$ |
| $\sin x$ | $-\cos x+C$ |
| $\sec^2x$ | $\tan x+C$ |
| $\csc^2x$ | $-\cot x+C$ |
| $\sec x\tan x$ | $\sec x+C$ |
| $\csc x\cot x$ | $-\csc x+C$ |

---

## Inverse-Trigonometric Antiderivatives

| Function $f(x)$ | Antiderivative $\int f(x)\,dx$ |
|---|---|
| $\dfrac{1}{\sqrt{1-x^2}}$ | $\sin^{-1}(x)+C$ |
| $\dfrac{1}{1+x^2}$ | $\tan^{-1}(x)+C$ |

---

## Hyperbolic Antiderivatives

| Function $f(x)$ | Antiderivative $\int f(x)\,dx$ |
|---|---|
| $\cosh x$ | $\sinh x+C$ |
| $\sinh x$ | $\cosh x+C$ |

---

## Linearity Rules

| Rule | Formula |
|---|---|
| Constant Multiple Rule | $\int c f(x)\,dx=c\int f(x)\,dx$ |
| Sum Rule | $\int[f(x)+g(x)]\,dx=\int f(x)\,dx+\int g(x)\,dx$ |
| Difference Rule | $\int[f(x)-g(x)]\,dx=\int f(x)\,dx-\int g(x)\,dx$ |

---

## Important Special Case

```math
\int \frac{1}{x}\,dx=\ln\lvert x\rvert+C
```

The absolute value is required because $1/x$ is defined for positive and negative values of $x$, while $\ln x$ alone is defined only for $x>0$.

### Notes

- Use $\ln\lvert x\rvert+C$ whenever the antiderivative of $1/x$ appears.
- Every indefinite integral includes an arbitrary constant of integration $C$.
- The power rule does **not** apply when the exponent is $-1$.

---

## Recognition Cheat Sheet

| If You See | Think |
|---|---|
| $x^5,\;x^{-2},\;\sqrt{x}$ | Power Rule |
| $\dfrac{1}{x}$ | $\ln\lvert x\rvert+C$ |
| $e^x$ | It remains $e^x$ |
| $\sec^2x$ | $\tan x+C$ |
| $\sec x\tan x$ | $\sec x+C$ |
| $\dfrac{1}{1+x^2}$ | $\tan^{-1}(x)+C$ |
| $\dfrac{1}{\sqrt{1-x^2}}$ | $\sin^{-1}(x)+C$ |

---

## Most Important Formulas to Memorize

```math
\boxed{\int x^n\,dx=\frac{x^{n+1}}{n+1}+C\qquad(n\ne -1)}
```

```math
\boxed{\int \frac{1}{x}\,dx=\ln\lvert x\rvert+C}
```

```math
\boxed{\int e^x\,dx=e^x+C}
```

```math
\boxed{\int \cos x\,dx=\sin x+C}
```

```math
\boxed{\int \sin x\,dx=-\cos x+C}
```

```math
\boxed{\int \sec^2x\,dx=\tan x+C}
```

```math
\boxed{\int \sec x\tan x\,dx=\sec x+C}
```

---

## Common Mistakes

1. Always include the constant of integration:

```math
\boxed{+C}
```

2. Do not use the power rule for $1/x$:

```math
\boxed{\int \frac{1}{x}\,dx=\ln\lvert x\rvert+C}
```

3. For the power rule:

- add $1$ to the exponent;
- divide by the new exponent;
- include $C$.
