# Antiderivatives Cheat Sheet

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

## Basic Antiderivatives

| Function $f(x)$ | Antiderivative $\int f(x)\,dx$ |
|---|---|
| $c$ | $$cx + C$$ |
| $x^n,\; n\neq -1$ | $$\frac{x^{n+1}}{n+1}+C$$ |
| $\frac{1}{x}$ | $\ln \lvert x \rvert + C$ |
| $e^x$ | $$e^x+C$$ |
| $b^x$ | $$\frac{b^x}{\ln b}+C$$ |

---

## Trigonometric Antiderivatives

| Function $f(x)$ | Antiderivative $\int f(x)\,dx$ |
|---|---|
| $\cos x$ | $$\sin x + C$$ |
| $\sin x$ | $$-\cos x + C$$ |
| $\sec^2 x$ | $$\tan x + C$$ |
| $\sec x \tan x$ | $$\sec x + C$$ |

---

## Inverse Trig Antiderivatives

| Function $f(x)$ | Antiderivative $\int f(x)\,dx$ |
|---|---|
| $\dfrac{1}{\sqrt{1-x^2}}$ | $$\sin^{-1}(x)+C$$ |
| $\dfrac{1}{1+x^2}$ | $$\tan^{-1}(x)+C$$ |

---

## Hyperbolic Antiderivatives

| Function $f(x)$ | Antiderivative $\int f(x)\,dx$ |
|---|---|
| $\cosh x$ | $$\sinh x + C$$ |
| $\sinh x$ | $$\cosh x + C$$ |

---

## Table of Indefinite Integrals
## Table of Indefinite Integrals

| Integral | Antiderivative |
|----------|----------------|
| $\int c\,f(x)\,dx$ | $c\int f(x)\,dx$ |
| $\int [f(x)+g(x)]\,dx$ | $\int f(x)\,dx+\int g(x)\,dx$ |
| $\int k\,dx$ | $kx+C$ |
| $\int x^n\,dx,\; n\neq -1$ | $\dfrac{x^{n+1}}{n+1}+C$ |
| $\int \frac{1}{x}\,dx$ | $\ln \vert x \vert + C$ |
| $\int e^x\,dx$ | $e^x+C$ |
| $\int b^x\,dx$ | $\dfrac{b^x}{\ln b}+C$ |
| $\int \sin x\,dx$ | $-\cos x+C$ |
| $\int \cos x\,dx$ | $\sin x+C$ |
| $\int \sec^2 x\,dx$ | $\tan x+C$ |
| $\int \csc^2 x\,dx$ | $-\cot x+C$ |
| $\int \sec x\tan x\,dx$ | $\sec x+C$ |
| $\int \csc x\cot x\,dx$ | $-\csc x+C$ |
| $\int \dfrac{1}{x^2+1}\,dx$ | $\tan^{-1}(x)+C$ |
| $\int \dfrac{1}{\sqrt{1-x^2}}\,dx$ | $\sin^{-1}(x)+C$ |
| $\int \sinh x\,dx$ | $\cosh x+C$ |
| $\int \cosh x\,dx$ | $\sinh x+C$ |

### Important Note

For

$$
\int \frac{1}{x}\,dx
$$

the antiderivative is

$$
\ln|x|+C
$$

not $\ln(x)+C$, because the logarithm must be defined for both positive and negative values of $x$.

### Notes

- Use $$\ln \left|x\right|+C$$ whenever the antiderivative of $$\frac{1}{x}$$ appears.
- The absolute value bars $$\left|x\right|$$ are required because $$x$$ may be positive or negative.
- Every indefinite integral includes an arbitrary constant of integration $$C$$.

## Rules

| Rule | Formula |
|---|---|
| Constant Multiple Rule | $$\int c f(x)\,dx = c\int f(x)\,dx$$ |
| Sum Rule | $$\int [f(x)+g(x)]\,dx = \int f(x)\,dx + \int g(x)\,dx$$ |
| Difference Rule | $$\int [f(x)-g(x)]\,dx = \int f(x)\,dx - \int g(x)\,dx$$ |

---

## Recognition Cheat Sheet

| If You See | Think |
|---|---|
| $x^5,\;x^{-2},\;\sqrt{x}$ | Power Rule |
| $\dfrac{1}{x}$ | $\boxed{\ln \lvert x \rvert + C}$ (special case) |
| $e^x$ | stays $e^x$ |
| $\sec^2x$ | $$\boxed{\tan x + C}$$ |
| $\sec x\tan x$ | $$\boxed{\sec x + C}$$ |
| $\dfrac{1}{1+x^2}$ | $$\boxed{\tan^{-1}(x)+C}$$ |
| $\dfrac{1}{\sqrt{1-x^2}}$ | $$\boxed{\sin^{-1}(x)+C}$$ |

---

## Most Important Formulas to Memorize

$$
\boxed{
\int x^n\,dx
=
\frac{x^{n+1}}{n+1}+C
\qquad (n\neq -1)
}
$$

$$
\boxed{
\int \frac{1}{x}\,dx
=
\ln|x|+C
}
$$

$$
\boxed{
\int e^x\,dx
=
e^x+C
}
$$

$$
\boxed{
\int \cos x\,dx
=
\sin x+C
}
$$

$$
\boxed{
\int \sin x\,dx
=
-\cos x+C
}
$$

$$
\boxed{
\int \sec^2x\,dx
=
\tan x+C
}
$$

$$
\boxed{
\int \sec x\tan x\,dx
=
\sec x+C
}
$$

## Common Mistakes

1. Always include:

$$
\boxed{+C}
$$

2. Do **not** use the power rule for:

$$
\boxed{
\int \frac{1}{x}\,dx
=
\ln|x|+C
}
$$

3. For the power rule:
- **Add 1 to the exponent**
- **Then divide by the new exponent**