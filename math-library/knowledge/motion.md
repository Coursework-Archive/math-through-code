# 🔹 Motion Cheat Sheet (Position → Velocity → Acceleration)

---

## 📌 Position Function
- Represents location over time  
- Notation:  
  $$
  s(t)
  $$

---

## 📌 Average Velocity
- Measures change over an **interval**
- Think: “overall speed from point A to B”

$$
\text{Average Velocity} = \frac{s(b) - s(a)}{b - a}
$$

### 🔍 Recognition:
- “average velocity”
- “average rate of change”
- “over the interval [a, b]”

### ⚠️ Common Mistake:
- Using derivative instead of a fraction

---

## 📌 Instantaneous Velocity
- Velocity at a **single moment**
- Derivative of position

$$
v(t) = s'(t)
$$

### 🔍 Recognition:
- “velocity at time t”
- “instantaneous velocity”
- “find velocity function”

### ⚠️ Common Mistake:
- Forgetting to take derivative first

---

## 📌 Acceleration
- Rate of change of velocity
- Second derivative of position

$$
a(t) = s''(t)
$$

### 🔍 Recognition:
- “acceleration”
- “rate of change of velocity”

### ⚠️ Common Mistake:
- Confusing with velocity (first derivative)

---

## 🔁 Full Relationship (Memorize This)
- Position → $s(t)$  
- Velocity → $s'(t)$  
- Acceleration → $s''(t)$  

---

## 🔥 Quick Decision Rule
- Interval given? → **Average velocity (fraction)**
- Single time? → **Derivative (instantaneous velocity)**
- Asking how velocity changes? → **Second derivative (acceleration)**

---

| Given        | Integrate | Result                |
| ------------ | --------- | --------------------- |
| Acceleration | Once      | Velocity              |
| Velocity     | Once      | Position/Displacement |


Displacement:
∫ v(t) dt

Distance traveled:
1. Solve v(t)=0.
2. Are any roots inside the interval?
3. Split the interval at those roots.
4. Test the sign of v(t) on each piece.
5. If negative, add a minus sign to that integral.
6. Add the positive pieces together.
