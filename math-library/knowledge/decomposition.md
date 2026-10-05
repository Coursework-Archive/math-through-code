## Partial Fraction Decomposition: Degree Rule

Before decomposing, compare the degree of the numerator and denominator.

$$
\deg(\text{numerator}) < \deg(\text{denominator})
\quad\Longrightarrow\quad
\text{Decompose directly.}
$$

$$
\deg(\text{numerator}) \geq \deg(\text{denominator})
\quad\Longrightarrow\quad
\text{Perform polynomial long division first.}
$$


## Integration Rule After Partial Fraction Decomposition


### Recognition Rule

```math
\boxed{
(x-a)^{-1}
\Longrightarrow
\ln\lvert x-a\rvert
}
```

```math
\boxed{
(x-a)^n,\ n\neq -1
\Longrightarrow
\text{Use the power rule.}
}
```

After decomposing, look at the power of each linear factor.

```math
\boxed{
\int \frac{1}{x-a}\,dx
=
\ln\lvert x-a\rvert+C
}
```


For other powers, use the power rule:

```math
\boxed{
\int (x-a)^n\,dx
=
\frac{(x-a)^{n+1}}{n+1}+C,
\qquad n\neq -1
}
```

Example:

```math
\int \frac{1}{(x-a)^2}\,dx
=
\int (x-a)^{-2}\,dx
=
-\frac{1}{x-a}+C
```

## Quadratic Denominators: Natural Log vs. Arctangent

When the denominator begins with $x^2$, look at the **numerator** to decide whether to think natural log or arctangent.

### Natural Log Pattern

If the numerator matches the derivative of the denominator, think:

```math
\boxed{
\int \frac{f'(x)}{f(x)}\,dx
=
\ln\lvert f(x)\rvert+C
}
```

For example:

```math
\int \frac{2x}{x^2+4}\,dx
=
\ln(x^2+4)+C
```

If the numerator is only $x$:

```math
\int \frac{x}{x^2+4}\,dx
=
\frac12\ln(x^2+4)+C
```

### Arctangent Pattern

If the denominator has the form

```math
x^2+a^2
```

and there is **no $x$ in the numerator**, think arctangent:

```math
\boxed{
\int \frac{1}{x^2+a^2}\,dx
=
\frac{1}{a}
\arctan\left(\frac{x}{a}\right)+C
}
```

With a constant numerator:

```math
\boxed{
\int \frac{K}{x^2+a^2}\,dx
=
\frac{K}{a}
\arctan\left(\frac{x}{a}\right)+C
}
```

Example:

```math
\int \frac{2}{x^2+4}\,dx
=
2\left(
\frac12\arctan\left(\frac{x}{2}\right)
\right)
=
\arctan\left(\frac{x}{2}\right)+C
```

### Recognition Rule

```math
\boxed{
\frac{x}{x^2+a^2}
\Longrightarrow
\text{Think }u=x^2+a^2
}
```

```math
\boxed{
\frac{1}{x^2+a^2}
\Longrightarrow
\text{Think arctangent}
}
```

The key question is:

```math
\boxed{
\text{Is there an }x\text{ in the numerator that matches the derivative of }x^2?
}
```

- Yes $\Longrightarrow$ think $u$-substitution.
- No $\Longrightarrow$ check for the arctangent form.


# Logarithmic Integrals: Choosing Between \(u\)-Substitution and Integration by Parts

## Recognition Rule

When an integral contains a logarithm, first ask:

1. Is the derivative of the expression inside the logarithm already present?
2. Is the logarithm standing alone or multiplied by an algebraic function?

---

## Case 1: Use \(u\)-Substitution

If the derivative of the logarithm is already present, use \(u\)-substitution.

Example:

```math
\int \frac{\ln(4x)}{x}\,dx
```

Choose

```math
u=\ln(4x)
```

Differentiate:

```math
du=\frac{1}{4x}(4)\,dx
=\frac{1}{x}\,dx
```

Then

```math
\int \frac{\ln(4x)}{x}\,dx
=
\int u\,du
```

```math
=
\frac{u^2}{2}+C
```

Substitute back:

```math
\boxed{
\frac{(\ln(4x))^2}{2}+C
}
```

### Recognition Cue

```math
\boxed{
\ln(f(x))\,\frac{f'(x)}{f(x)}
\Longrightarrow
u=\ln(f(x))
}
```

---

## Case 2: Logarithm by Itself

If the logarithm appears by itself, use integration by parts.

Example:

```math
\int \ln(3x)\,dx
```

Choose

```math
u=\ln(3x)
```

```math
dv=dx
```

Then

```math
du=\frac{1}{x}\,dx
```

```math
v=x
```

Apply integration by parts:

```math
\int u\,dv
=
uv-\int v\,du
```

```math
\int \ln(3x)\,dx
=
x\ln(3x)
-
\int x\left(\frac{1}{x}\right)\,dx
```

Simplify:

```math
=
x\ln(3x)-\int 1\,dx
```

```math
\boxed{
x\ln(3x)-x+C
}
```

---

## Case 3: Logarithm Multiplied by a Power of \(x\)

If a logarithm is multiplied by an algebraic function such as \(x^n\), use integration by parts.

Example:

```math
\int x^2\ln x\,dx
```

Using LIATE, choose the logarithm for \(u\):

```math
u=\ln x
```

```math
dv=x^2\,dx
```

Then

```math
du=\frac{1}{x}\,dx
```

```math
v=\frac{x^3}{3}
```

Apply integration by parts:

```math
\int x^2\ln x\,dx
=
\frac{x^3}{3}\ln x
-
\int
\frac{x^3}{3}
\left(\frac{1}{x}\right)\,dx
```

Simplify:

```math
=
\frac{x^3}{3}\ln x
-
\int \frac{x^2}{3}\,dx
```

```math
\boxed{
\frac{x^3}{3}\ln x
-
\frac{x^3}{9}
+C
}
```

---

## Quick Recognition Guide

| If You See | Think |
|---|---|
| $\dfrac{\ln(f(x))f'(x)}{f(x)}$ | \(u\)-substitution |
| $\ln(f(x))$ by itself | Integration by parts |
| $x^n\ln x$ | Integration by parts |
| Polynomial $\times$ logarithm | Integration by parts |

```math
\boxed{
\text{Derivative pattern present}
\Longrightarrow
u\text{-substitution}
}
```

```math
\boxed{
\text{Logarithm alone or multiplied by an algebraic function}
\Longrightarrow
\text{Integration by parts}
}
```
