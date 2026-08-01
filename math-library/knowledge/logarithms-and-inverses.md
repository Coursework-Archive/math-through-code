# Section 1.5 — Inverse Functions and Logarithms

## Power, Exponential, and Logarithmic Integrals

| Integrand | Antiderivative |
|---|---|
| $x^n,\;n\neq -1$ | $\dfrac{x^{n+1}}{n+1}+C$ |
| $e^x$ | $e^x+C$ |
| $a^x$ | $\dfrac{a^x}{\ln a}+C$ |
| $\dfrac{1}{x}$ | $\ln|x|+C$ |

---

## Definition 3 — Inverse Function Relationship

```math
f^{-1}(x)=y
\quad\Longleftrightarrow\quad
f(y)=x
```

## Definition 4 — Cancellation Equations

```math
f^{-1}(f(x))=x
\quad\text{for every }x\text{ in the domain of }f
```

```math
f(f^{-1}(x))=x
\quad\text{for every }x\text{ in the domain of }f^{-1}
```

## Definition 6 — Logarithmic Form

For $b>0$, $b\ne 1$, and $x>0$:

```math
\log_b x=y
\quad\Longleftrightarrow\quad
b^y=x
```

## Definition 7 — Exponential and Logarithmic Cancellation

```math
\log_b(b^x)=x
\quad\text{for every }x\in\mathbb{R}
```

```math
b^{\log_b x}=x
\quad\text{for every }x>0
```

---

## Laws of Logarithms

For $x>0$ and $y>0$:

### Product Rule

```math
\log_b(xy)=\log_b x+\log_b y
```

### Quotient Rule

```math
\log_b\left(\frac{x}{y}\right)=\log_b x-\log_b y
```

### Power Rule

```math
\log_b(x^r)=r\log_b x
```

---

## Definition 8 — Natural Logarithm (Inverse Form)

```math
\ln x=y
\quad\Longleftrightarrow\quad
e^y=x
```

## Definition 9 — Natural Logarithm Cancellation

```math
\ln(e^x)=x
\quad\text{for every }x\in\mathbb{R}
```

```math
e^{\ln x}=x
\quad\text{for every }x>0
```

---

## Definition 10 — Exponential Rewrite Using $\ln$

For $x>0$:

```math
x^r=e^{\ln(x^r)}=e^{r\ln x}
```

---

## Definition 11 — Change-of-Base Formula

```math
\log_b x=\frac{\ln x}{\ln b}
```
