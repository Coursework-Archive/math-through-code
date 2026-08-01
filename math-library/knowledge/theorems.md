# Calculus Theorems and Decision Rules

## Continuity Comes First

If a function is undefined or discontinuous at a point inside the interval, then the continuity hypotheses for the Extreme Value Theorem, Mean Value Theorem, and Rolle's Theorem are not satisfied on that interval.

For example, when a function is undefined at $x=0$ and the interval contains $0$:

- the function is not continuous on the whole interval;
- the Extreme Value Theorem cannot be invoked;
- the Mean Value Theorem cannot be invoked;
- Rolle's Theorem cannot be invoked.

---

## Extreme Value Theorem (EVT)

### Conditions

The function $f$ must be continuous on the closed interval $[a,b]$.

### Conclusion

The function attains both an absolute maximum and an absolute minimum somewhere on $[a,b]$.

### Recognition Cue

Closed interval plus continuity suggests the **Extreme Value Theorem**.

---

## Mean Value Theorem (MVT)

### Conditions

1. $f$ is continuous on $[a,b]$.
2. $f$ is differentiable on $(a,b)$.

### Conclusion

There is at least one number $c\in(a,b)$ such that

```math
f'(c)=\frac{f(b)-f(a)}{b-a}
```

The instantaneous rate of change at $c$ equals the average rate of change over $[a,b]$.

---

## Rolle's Theorem

### Conditions

1. $f$ is continuous on $[a,b]$.
2. $f$ is differentiable on $(a,b)$.
3. $f(a)=f(b)$.

### Conclusion

There is at least one number $c\in(a,b)$ such that

```math
f'(c)=0
```

Rolle's Theorem is a special case of the Mean Value Theorem.

---

## Finding Absolute Maximum and Minimum Values

For a continuous function on a closed interval $[a,b]$:

1. Compute $f'(x)$.
2. Find all critical numbers inside $(a,b)$.
3. Evaluate the original function at every critical number and both endpoints.
4. Compare the resulting function values.

The largest value is the absolute maximum, and the smallest value is the absolute minimum.

---

## Optimization Problems

Optimization problems usually contain two equations or relationships.

### Objective Function

The quantity being maximized or minimized, such as:

- area;
- volume;
- profit;
- cost;
- surface area.

### Constraint Equation

The fixed limitation in the problem, such as:

- a fixed perimeter;
- a fixed volume;
- a fixed budget;
- a fixed amount of material.

| Problem Statement | Objective | Constraint |
|---|---|---|
| Greatest area with 600 ft of fencing | Area | Perimeter $=600$ |
| Least metal for a $500\text{ cm}^3$ can | Surface area | Volume $=500$ |
| Maximum profit with a fixed budget | Profit | Budget |

### Optimization Workflow

1. Identify the objective.
2. Identify the constraint.
3. Solve the constraint for one variable.
4. Substitute into the objective function.
5. Differentiate the one-variable objective.
6. Find and test critical numbers.
7. Confirm whether the result is a maximum or minimum.
8. State the answer with units.

---

## Fundamental Theorem of Calculus (FTC)

### Variable Upper Limit

```math
\frac{d}{dx}\int_a^x f(t)\,dt=f(x)
```

### Upper Limit Is a Function

```math
\frac{d}{dx}\int_a^{g(x)} f(t)\,dt=f(g(x))g'(x)
```

### Variable Lower Limit

```math
\frac{d}{dx}\int_{g(x)}^a f(t)\,dt=-f(g(x))g'(x)
```

### Both Limits Are Functions

```math
\frac{d}{dx}\int_{g(x)}^{h(x)} f(t)\,dt
=f(h(x))h'(x)-f(g(x))g'(x)
```

Recognition clues include “differentiate an integral” and “an integral with variable limits.”

---

## L'Hôpital's Rule

L'Hôpital's Rule applies only after direct substitution produces an indeterminate form such as $0/0$ or $\infty/\infty$.

When its hypotheses are satisfied:

```math
\lim_{x\to a}\frac{f(x)}{g(x)}
=
\lim_{x\to a}\frac{f'(x)}{g'(x)}
```

Differentiate the numerator and denominator separately. Do not use the quotient rule.

### Checklist

1. Substitute first.
2. Confirm the form is $0/0$ or $\infty/\infty$.
3. Differentiate numerator and denominator separately.
4. Evaluate the new limit.
5. Repeat only if the new expression is still indeterminate.

---

## Newton's Method

Newton's method approximates a root of $f(x)=0$ using

```math
\boxed{x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}}
```

### Workflow

1. Choose or use the given initial estimate $x_0$.
2. Compute $f(x)$ and $f'(x)$.
3. Substitute $x_0$ into the iteration formula:

```math
x_1=x_0-\frac{f(x_0)}{f'(x_0)}
```

4. For another iteration, use $x_1$:

```math
x_2=x_1-\frac{f(x_1)}{f'(x_1)}
```

Continue until the requested accuracy or number of iterations is reached.
