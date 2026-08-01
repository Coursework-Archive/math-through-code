# Section 1.5 — Inverse Functions and Logarithms

## Power, Exponential, and Logarithmic Integrals

| Integrand | Antiderivative |
|---|---|
| $x^n,\;n\neq -1$ | $\dfrac{x^{n+1}}{n+1}+C$ |
| $e^x$ | $e^x+C$ |
| $a^x$ | $\dfrac{a^x}{\ln a}+C$ |
| $\dfrac1x$ | $\ln|x|+C$ |

---

## Definition 3 — Inverse Function Relationship
$$
f^{-1}(x) = y \;\Longleftrightarrow\; f(y) = x
$$

## Definition 4 — Cancellation Equations
$$
f^{-1}(f(x)) = x \quad \text{for every } x \in A
$$
$$
f(f^{-1}(x)) = x \quad \text{for every } x \in B
$$

## Definition 6 — Logarithmic Form
$$
\log_b x = y \;\Longleftrightarrow\; b^y = x
$$

## Definition 7 — Exponential/Log Cancellation
$$
\log_b(b^x) = x \quad \text{for every } x \in \mathbb{R}
$$
$$
b^{\log_b x} = x \quad \text{for every } x > 0
$$

---

## Laws of Logarithms
For $x > 0$, $y > 0$:

1. Product Rule
$$
\log_b(xy) = \log_b x + \log_b y
$$

2. Quotient Rule
$$
\log_b\!\left(\frac{x}{y}\right) = \log_b x - \log_b y
$$

3. Power Rule
$$
\log_b(x^r) = r \log_b x
$$

---

## Definition 8 — Natural Logarithm (Inverse Form)
$$
\ln x = y \;\Longleftrightarrow\; e^y = x
$$

## Definition 9 — Natural Log Cancellation
$$
\ln(e^x) = x \quad \text{for every } x \in \mathbb{R}
$$
$$
e^{\ln x} = x \quad \text{for every } x > 0
$$

---

## Definition 10 — Exponential Rewrite Using $\ln$
$$
x^r = e^{\ln(x^r)} = e^{r \ln x} \quad \text{for } x > 0
$$

---

## Definition 11 — Change of Base Formula
$$
\log_b x = \frac{\ln x}{\ln b}
$$