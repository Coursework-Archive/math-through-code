# Hyperbolic Functions Cheat Sheet

## Definitions

```math
\sinh x=\frac{e^x-e^{-x}}{2}
```

```math
\cosh x=\frac{e^x+e^{-x}}{2}
```

```math
\tanh x=\frac{\sinh x}{\cosh x}
```

```math
\mathrm{csch}\,x=\frac{1}{\sinh x}
```

```math
\mathrm{sech}\,x=\frac{1}{\cosh x}
```

```math
\coth x=\frac{\cosh x}{\sinh x}
```

---

## Key Identities

```math
\sinh(-x)=-\sinh x
```

```math
\cosh(-x)=\cosh x
```

```math
\cosh^2x-\sinh^2x=1
```

```math
1-\tanh^2x=\mathrm{sech}^2x
```

```math
\sinh(x+y)=\sinh x\cosh y+\cosh x\sinh y
```

```math
\cosh(x+y)=\cosh x\cosh y+\sinh x\sinh y
```

---

## Derivatives

```math
\frac{d}{dx}(\sinh x)=\cosh x
```

```math
\frac{d}{dx}(\cosh x)=\sinh x
```

```math
\frac{d}{dx}(\tanh x)=\mathrm{sech}^2x
```

```math
\frac{d}{dx}(\mathrm{csch}\,x)
=-\mathrm{csch}\,x\coth x
```

```math
\frac{d}{dx}(\mathrm{sech}\,x)
=-\mathrm{sech}\,x\tanh x
```

```math
\frac{d}{dx}(\coth x)=-\mathrm{csch}^2x
```

---

## Inverse Hyperbolic Functions in Logarithmic Form

```math
\sinh^{-1}x=\ln\left(x+\sqrt{x^2+1}\right)
```

```math
\cosh^{-1}x=\ln\left(x+\sqrt{x^2-1}\right),\qquad x\ge 1
```

```math
\tanh^{-1}x=\frac12\ln\left(\frac{1+x}{1-x}\right),
\qquad -1<x<1
```

---

## Derivatives of Inverse Hyperbolic Functions

```math
\frac{d}{dx}(\sinh^{-1}x)=\frac{1}{\sqrt{1+x^2}}
```

```math
\frac{d}{dx}(\cosh^{-1}x)=\frac{1}{\sqrt{x^2-1}}
```

```math
\frac{d}{dx}(\tanh^{-1}x)=\frac{1}{1-x^2}
```

```math
\frac{d}{dx}(\mathrm{csch}^{-1}x)
=-\frac{1}{\lvert x\rvert\sqrt{1+x^2}}
```

```math
\frac{d}{dx}(\mathrm{sech}^{-1}x)
=-\frac{1}{x\sqrt{1-x^2}}
```

```math
\frac{d}{dx}(\coth^{-1}x)=\frac{1}{1-x^2}
```

---

# Recognition and Strategy Guide

## 1. When Hyperbolic Functions Appear

### A. Hidden Hyperbolic Expressions

When you see

```math
\frac{e^x-e^{-x}}{2}
\qquad\text{or}\qquad
\frac{e^x+e^{-x}}{2},
```

recognize $\sinh x$ and $\cosh x$.

**Strategy:** Rewrite the expression in hyperbolic form before differentiating or integrating.

### B. Radicals Involving $x^2\pm 1$

For

```math
\sqrt{x^2+1},
```

try the substitution $x=\sinh t$.

For

```math
\sqrt{x^2-1},
```

try $x=\cosh t$ when the domain supports $x\ge 1$.

The key identity is

```math
\cosh^2t-\sinh^2t=1.
```

### C. Logarithmic Forms

Recognize

```math
\ln\left(x+\sqrt{x^2+1}\right)=\sinh^{-1}x
```

and

```math
\ln\left(x+\sqrt{x^2-1}\right)=\cosh^{-1}x.
```

### D. Inverse-Hyperbolic Derivative Pattern

```math
\frac{1}{\sqrt{1+x^2}}
```

is the derivative of $\sinh^{-1}x$, not an inverse-trigonometric derivative.

---

## 2. Hyperbolic vs. Trigonometric Substitution

| Expression | Typical Choice |
|---|---|
| $\sqrt{1-x^2}$ | Trigonometric: $x=\sin t$ |
| $\sqrt{1+x^2}$ | Hyperbolic: $x=\sinh t$ |
| $\sqrt{x^2-1}$ | Hyperbolic: $x=\cosh t$ |

---

## 3. Fast Derivative Recall

The core pair is

```math
\sinh x\longleftrightarrow\cosh x.
```

Memorize:

```math
\frac{d}{dx}(\sinh x)=\cosh x
```

```math
\frac{d}{dx}(\cosh x)=\sinh x
```

```math
\frac{d}{dx}(\tanh x)=\mathrm{sech}^2x
```

Unlike several trigonometric derivatives, these three do not introduce a negative sign.

---

## 4. Most Useful Identity

```math
\cosh^2x-\sinh^2x=1
```

Compare it with the trigonometric identity

```math
\sin^2x+\cos^2x=1.
```

The structure is similar, but the sign is different.

---

## 5. Common Exam Traps

### Trap 1: Confusing Hyperbolic and Inverse-Trigonometric Patterns

```math
\frac{1}{\sqrt{1+x^2}}
\ne
\frac{d}{dx}(\arcsin x)
```

Instead,

```math
\frac{1}{\sqrt{1+x^2}}
=
\frac{d}{dx}(\sinh^{-1}x).
```

### Trap 2: Ignoring Domain Restrictions

- $\cosh^{-1}x$ requires $x\ge 1$.
- $\tanh^{-1}x$ requires $-1<x<1$.

### Trap 3: Missing a Simplification

Rewrite

```math
\frac{e^x-e^{-x}}{2}
```

as $\sinh x$ when that form makes the problem easier.

---

## 6. Quick Mental Flow

1. Exponentials $e^x$ and $e^{-x}$ appearing symmetrically? Try $\sinh$ or $\cosh$.
2. Radical $\sqrt{x^2\pm1}$? Consider a hyperbolic substitution.
3. Logarithm $\ln\left(x+\sqrt{x^2\pm1}\right)$? Check for an inverse hyperbolic function.
4. Derivative pattern $1/\sqrt{1+x^2}$? Think $\sinh^{-1}x$.

---

## 7. Big Picture

Hyperbolic functions are built from exponentials and often provide the cleanest language for expressions involving:

- $x^2+1$;
- $x^2-1$;
- symmetric combinations of $e^x$ and $e^{-x}$.
