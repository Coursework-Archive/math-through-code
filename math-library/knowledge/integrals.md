# Integral Recognition Strategy

## 1. Simplify the Integrand

Before choosing a method:

- expand powers when useful;
- rewrite radicals as fractional exponents;
- factor constants out of the integral;
- simplify algebraic fractions when possible.

## 2. Look for a Basic Antiderivative

Ask whether the integrand matches a familiar pattern.

### Polynomial

```math
\int x^n\,dx
```

### Exponential

```math
\int e^x\,dx
```

```math
\int a^x\,dx
```

### Logarithmic Pattern

```math
\int \frac{1}{x}\,dx
```

### Trigonometric

```math
\int \sin x\,dx
```

```math
\int \cos x\,dx
```

```math
\int \sec^2x\,dx
```

## 3. Look for a Composition

A composition often suggests substitution. Look for an inside function together with its derivative.

### Example

```math
\int \frac{2z}{z^2+1}\,dz
```

Choose

```math
u=z^2+1.
```

Then

```math
du=2z\,dz,
```

so the integral becomes

```math
\int\frac{1}{u}\,du=\ln|u|+C.
```

Substitute back:

```math
\boxed{\ln(z^2+1)+C}
```

Because $z^2+1>0$ for every real $z$, absolute-value bars are optional in the final expression.
