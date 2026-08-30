# LaTeX Math Cheat Sheet

A simple reference: **what the math looks like** and **the LaTeX used to write it**.

Add to this file as new notation comes up.

---

## Basic Math

| Looks like | LaTeX |
|---|---|
| $\frac{a}{b}$ | `\frac{a}{b}` |
| $x^2$ | `x^2` |
| $e^{2x}$ | `e^{2x}` |
| $a_1$ | `a_1` |
| $a_{n+1}$ | `a_{n+1}` |
| $\sqrt{x}$ | `\sqrt{x}` |
| $\sqrt{1-x^2}$ | `\sqrt{1-x^2}` |
| $(x+1)$ | `(x+1)` |
| $\left(x+1\right)$ | `\left(x+1\right)` |
| $\lvert x\rvert$ | `\lvert x\rvert` |
| $a\cdot b$ | `a\cdot b` |

---

## Integrals

| Looks like | LaTeX |
|---|---|
| $\int x^2\,dx$ | `\int x^2\,dx` |
| $\int_a^b f(x)\,dx$ | `\int_a^b f(x)\,dx` |
| $\int_0^{\pi/2}\sin(x)\,dx$ | `\int_0^{\pi/2}\sin(x)\,dx` |
| $dx$ | `dx` |
| $du$ | `du` |
| $d\theta$ | `d\theta` |
| $\int u\,dv=uv-\int v\,du$ | `\int u\,dv=uv-\int v\,du` |

---

## Integration by Parts Setup

| Looks like | LaTeX |
|---|---|
| $u=x$ | `u=x` |
| $dv=\cos(x)\,dx$ | `dv=\cos(x)\,dx` |
| $du=dx$ | `du=dx` |
| $v=\sin(x)$ | `v=\sin(x)` |

### LIPET

Use this order when choosing $u$:

1. **L**ogarithmic
2. **I**nverse trig
3. **P**ower / polynomial
4. **E**xponential
5. **T**rig

---

## Substitution

| Looks like | LaTeX |
|---|---|
| $u=\ln(x)$ | `u=\ln(x)` |
| $du=\frac{1}{x}\,dx$ | `du=\frac{1}{x}\,dx` |
| $z=1-x^2$ | `z=1-x^2` |
| $dz=-2x\,dx$ | `dz=-2x\,dx` |
| $u=x^2+1\Rightarrow du=2x\,dx$ | `u=x^2+1\Rightarrow du=2x\,dx` |

---

## Trigonometric Functions

| Looks like | LaTeX |
|---|---|
| $\sin(x)$ | `\sin(x)` |
| $\cos(x)$ | `\cos(x)` |
| $\tan(x)$ | `\tan(x)` |
| $\sec(x)$ | `\sec(x)` |
| $\csc(x)$ | `\csc(x)` |
| $\cot(x)$ | `\cot(x)` |
| $\sin^2(x)$ | `\sin^2(x)` |
| $\cos^3(\theta)$ | `\cos^3(\theta)` |

---

## Inverse Trigonometric Functions

| Looks like | LaTeX |
|---|---|
| $\arcsin(x)$ | `\arcsin(x)` |
| $\arccos(x)$ | `\arccos(x)` |
| $\arctan(x)$ | `\arctan(x)` |
| $\sin^{-1}(x)$ | `\sin^{-1}(x)` |
| $\tan^{-1}(x)$ | `\tan^{-1}(x)` |

---

## Logarithms and Exponentials

| Looks like | LaTeX |
|---|---|
| $\ln(x)$ | `\ln(x)` |
| $\log(x)$ | `\log(x)` |
| $e^x$ | `e^x` |
| $e^{-x}$ | `e^{-x}` |
| $e^{2x}$ | `e^{2x}` |
| $e^{2\theta}$ | `e^{2\theta}` |

### Exponent reminder

If the exponent has more than one character, use braces:

| Looks like | LaTeX |
|---|---|
| $e^{2x}$ | `e^{2x}` |
| $x^{2n+1}$ | `x^{2n+1}` |

---

## Greek Letters

| Looks like | LaTeX |
|---|---|
| $\theta$ | `\theta` |
| $\pi$ | `\pi` |
| $\alpha$ | `\alpha` |
| $\beta$ | `\beta` |
| $\Delta$ | `\Delta` |
| $\Sigma$ | `\Sigma` |

---

## Common Calculus II Expressions

| Looks like | LaTeX |
|---|---|
| $\frac{x^2}{1+x^2}$ | `\frac{x^2}{1+x^2}` |
| $\frac{1}{\sqrt{1-x^2}}$ | `\frac{1}{\sqrt{1-x^2}}` |
| $\frac{\arccos(\ln x)}{x^2}$ | `\frac{\arccos(\ln x)}{x^2}` |
| $e^{2\theta}\cos(3\theta)$ | `e^{2\theta}\cos(3\theta)` |
| $\int e^{2\theta}\cos(3\theta)\,d\theta$ | `\int e^{2\theta}\cos(3\theta)\,d\theta` |
| $\frac{\frac{2}{3}}{\frac{13}{9}}$ | `\frac{\frac{2}{3}}{\frac{13}{9}}` |
| $\frac{\arccos(\ln x)}{x^2}$ | `\frac{\arccos(\ln x)}{x^2}` |

---

## Comparison Symbols

| Looks like | LaTeX |
|---|---|
| $=$ | `=` |
| $\neq$ | `\neq` |
| $<$ | `<` |
| $>$ | `>` |
| $\leq$ | `\leq` |
| $\geq$ | `\geq` |
| $\approx$ | `\approx` |

---

## Arrows

| Looks like | LaTeX |
|---|---|
| $\rightarrow$ | `\rightarrow` |
| $\Rightarrow$ | `\Rightarrow` |

---

## Constant of Integration

| Looks like | LaTeX |
|---|---|
| $+C$ | `+C` |

---

# Common Syntax Problems

| Problem | Correct LaTeX |
|---|---|
| Missing closing brace in an exponent | `e^{2\theta}` |
| Extra closing brace | `\sin(3\theta)` |
| Fraction needs numerator and denominator groups | `\frac{a}{b}` |
| Multi-character exponent needs braces | `x^{2x+1}` |
| Multi-character subscript needs braces | `a_{n+1}` |
| Trig function needs a backslash | `\sin(x)` |
| Greek letter needs a backslash | `\theta` |

---

## Quick Debugging Order

If LaTeX is highlighted or does not render correctly, check:

1. `{ }` braces
2. `( )` parentheses
3. Missing backslashes
4. `^{...}` exponents
5. `_{...}` subscripts
6. `\frac{...}{...}` groups

---

## Memory Aid

**Backslash = command. Braces = grouping.**

Examples:

| Looks like | LaTeX |
|---|---|
| $\frac{2}{3}$ | `\frac{2}{3}` |
| $e^{2\theta}$ | `e^{2\theta}` |
