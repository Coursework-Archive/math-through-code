# Motion Cheat Sheet: Position, Velocity, and Acceleration

## Position Function

- Represents location over time.
- Notation: $s(t)$.

---

## Average Velocity

- Measures change over an **interval**.
- Think: overall change in position divided by elapsed time.

```math
\text{Average velocity}=\frac{s(b)-s(a)}{b-a}
```

### Recognition Clues

- “average velocity”
- “average rate of change”
- “over the interval $[a,b]$”

### Common Mistake

Do not use a derivative when the question asks for average velocity over an interval.

---

## Instantaneous Velocity

- Velocity at a **single moment**.
- The derivative of position.

```math
v(t)=s'(t)
```

### Recognition Clues

- “velocity at time $t$”
- “instantaneous velocity”
- “find the velocity function”

### Common Mistake

Differentiate the position function before substituting a specific time.

---

## Acceleration

- The rate of change of velocity.
- The second derivative of position.

```math
a(t)=v'(t)=s''(t)
```

### Recognition Clues

- “acceleration”
- “rate of change of velocity”

### Common Mistake

Acceleration is the second derivative of position, not the first derivative.

---

## Full Relationship

```math
s(t)\xrightarrow{\text{differentiate}}v(t)=s'(t)
\xrightarrow{\text{differentiate}}a(t)=s''(t)
```

Moving in the reverse direction requires integration.

| Given | Operation | Result |
|---|---|---|
| Acceleration | Integrate once | Velocity |
| Velocity | Integrate once | Position plus a constant |

---

## Quick Decision Rule

- Interval given? Use **average velocity**.
- Single time given? Use the **derivative** for instantaneous velocity.
- Asking how velocity changes? Use the **second derivative** for acceleration.

---

## Displacement

Displacement over $[a,b]$ is the signed integral of velocity:

```math
\text{Displacement}=\int_a^b v(t)\,dt=s(b)-s(a)
```

## Total Distance Traveled

Total distance uses the absolute value of velocity:

```math
\text{Distance}=\int_a^b |v(t)|\,dt
```

Practical method:

1. Solve $v(t)=0$.
2. Keep only roots inside the interval.
3. Split the interval at those roots.
4. Determine the sign of $v(t)$ on each subinterval.
5. Reverse the sign of any negative velocity integral.
6. Add all positive distances.
