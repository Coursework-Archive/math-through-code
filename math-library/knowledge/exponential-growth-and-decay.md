# Exponential Growth & Decay 

## Pattern: Find exponential function from two points

Given:
An exponential function of the form  
\( f(x) = C b^x \)  
and two points on the graph.

---

### Step 1: Plug both points into the equation

For point \((x_1, y_1)\):
\( C b^{x_1} = y_1 \)

For point \((x_2, y_2)\):
\( C b^{x_2} = y_2 \)

---

### Step 2: Divide the equations (eliminates C)

\[
\frac{C b^{x_2}}{C b^{x_1}} = \frac{y_2}{y_1}
\]

\[
b^{x_2 - x_1} = \frac{y_2}{y_1}
\]

---

### Step 3: Solve for \(b\)

\[
b = \left(\frac{y_2}{y_1}\right)^{\frac{1}{x_2 - x_1}}
\]

(Usually this simplifies nicely — often no logs needed)

---

### Step 4: Plug back to solve for \(C\)

Use either original equation:

\[
C b^{x_1} = y_1
\]

Solve for \(C\)

---

### Step 5: Write final answer

\[
\boxed{f(x) = C b^x}
\]

---

## Example (from your problem)

Points: \((1,6)\), \((3,24)\)

Step 1:
\( Cb = 6 \)  
\( Cb^3 = 24 \)

Step 2:
\[
\frac{Cb^3}{Cb} = \frac{24}{6}
\Rightarrow b^2 = 4
\]

Step 3:
\( b = 2 \)

Step 4:
\( 2C = 6 \Rightarrow C = 3 \)

Step 5:
\[
\boxed{f(x) = 3 \cdot 2^x}
\]

## 1. General Exponential Form
y = a · b^t
- a = initial value
- b = growth/decay factor
- t = time

Rules:
- Growth: b > 1
- Decay: 0 < b < 1


## 2. Growth & Decay (Rate Form – Discrete)
Growth:
y = a(1 + r)^t

Decay:
y = a(1 - r)^t

- r = rate (decimal form)

Examples:
- 5% growth → r = 0.05 → b = 1.05
- 8% decay → r = 0.08 → b = 0.92


## 3. Continuous Growth / Decay (IMPORTANT)
y = a e^(kt)

- a = initial value
- k = continuous growth/decay rate
- t = time
- e ≈ 2.718

Rules:
- k > 0 → growth
- k < 0 → decay

Example:
- 3% continuous growth → k = 0.03
- 7% continuous decay → k = -0.07


## 4. Compounded n Times Per Year
y = a(1 + r/n)^(nt)

- n = number of compounding periods per year

Examples:
- Monthly → n = 12
- Daily → n = 365


## 5. Annual / Yearly Growth
y = a(1 + r)^t

- t is in years
- compounding once per year


## 6. Key Conversions

Percent → Decimal:
r = percent ÷ 100

Discrete factor:
- Growth: 1 + r
- Decay: 1 - r

Continuous model:
- Use k directly in e^(kt)


## 7. Graph Behavior
- y-intercept = a
- Growth → increasing curve
- Decay → decreasing curve
- Horizontal asymptote: y = 0


## 8. When to Use Which Model

Use:
- y = a(1 ± r)^t → when rate is applied in steps (yearly, monthly, etc.)
- y = a e^(kt) → when growth is continuous