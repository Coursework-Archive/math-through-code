# Exponential Growth and Decay

## Pattern: Find an Exponential Function from Two Points

Suppose an exponential function has the form $f(x)=Cb^x$ and passes through the points $(x_1,y_1)$ and $(x_2,y_2)$.

---

### Step 1: Substitute Both Points

For $(x_1,y_1)$:

```math
Cb^{x_1}=y_1
```

For $(x_2,y_2)$:

```math
Cb^{x_2}=y_2
```

---

### Step 2: Divide the Equations

Dividing eliminates $C$:

```math
\frac{Cb^{x_2}}{Cb^{x_1}}=\frac{y_2}{y_1}
```

Therefore,

```math
b^{x_2-x_1}=\frac{y_2}{y_1}
```

---

### Step 3: Solve for $b$

```math
b=\left(\frac{y_2}{y_1}\right)^{\frac{1}{x_2-x_1}}
```

This often simplifies without logarithms.

---

### Step 4: Solve for $C$

Substitute $b$ into either original equation:

```math
Cb^{x_1}=y_1
```

---

### Step 5: Write the Final Function

```math
\boxed{f(x)=Cb^x}
```

---

## Example

Find the exponential function through $(1,6)$ and $(3,24)$.

From the two points:

```math
Cb=6
```

```math
Cb^3=24
```

Divide the equations:

```math
\frac{Cb^3}{Cb}=\frac{24}{6}
\quad\Longrightarrow\quad
b^2=4
```

For a positive exponential base, $b=2$. Then:

```math
2C=6
\quad\Longrightarrow\quad
C=3
```

Therefore,

```math
\boxed{f(x)=3\cdot 2^x}
```

---

## 1. General Exponential Form

```math
y=ab^t
```

- $a$ is the initial value.
- $b$ is the growth or decay factor.
- $t$ is time.
- Growth: $b>1$.
- Decay: $0<b<1$.

## 2. Discrete Growth and Decay

Growth:

```math
y=a(1+r)^t
```

Decay:

```math
y=a(1-r)^t
```

Here, $r$ is the rate written as a decimal.

Examples:

- $5\%$ growth: $r=0.05$ and $b=1.05$.
- $8\%$ decay: $r=0.08$ and $b=0.92$.

## 3. Continuous Growth and Decay

```math
y=ae^{kt}
```

- $a$ is the initial value.
- $k$ is the continuous growth or decay rate.
- $t$ is time.
- $k>0$ indicates growth.
- $k<0$ indicates decay.

Examples:

- $3\%$ continuous growth: $k=0.03$.
- $7\%$ continuous decay: $k=-0.07$.

## 4. Compounding $n$ Times per Year

```math
y=a\left(1+\frac{r}{n}\right)^{nt}
```

Here, $n$ is the number of compounding periods per year.

- Monthly: $n=12$.
- Daily: $n=365$.

## 5. Annual Growth

```math
y=a(1+r)^t
```

Use this model when compounding occurs once per year and $t$ is measured in years.

## 6. Key Conversions

- Percent to decimal: $r=\dfrac{\text{percent}}{100}$.
- Discrete growth factor: $1+r$.
- Discrete decay factor: $1-r$.
- Continuous models use $k$ directly in $e^{kt}$.

## 7. Graph Behavior

- The $y$-intercept is $a$.
- Growth produces an increasing curve.
- Decay produces a decreasing curve.
- The horizontal asymptote is $y=0$.

## 8. Choosing a Model

- Use $y=a(1\pm r)^t$ when the rate is applied in steps, such as yearly or monthly.
- Use $y=ae^{kt}$ when growth or decay is continuous.
