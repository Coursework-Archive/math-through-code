# Recognition and Decision Rules

## Algebraic First Steps

### Try Factoring First

When you see:

- a fraction;
- common factors;
- a possible removable discontinuity.

### Try Expanding First

When you see expressions such as:

- $f(x+h)$;
- $(a+1)^n$;
- $(x+h)^2$.

---

## Domain Rules

1. Denominator: exclude values that make it $0$.
2. Even root: require the radicand to be at least $0$.
3. Even root in a denominator: require the radicand to be greater than $0$.
4. Odd root: all real radicands are allowed.
5. Natural logarithm: require the argument to be greater than $0$.
6. Logarithm of any valid base: require the argument to be greater than $0$.
7. Multiple restrictions: take the intersection of all conditions.
8. Products or quotients in inequalities: use a sign chart when needed.

---

# Function Transformations

## Identify the Base Function

- $x^2$: parabola.
- $\sqrt{x}$: square-root function.
- $|x|$: absolute-value function.
- $1/x$: rational function.
- $\sin x$ and $\cos x$: trigonometric functions.

Inside changes affect the input and are horizontal. Outside changes affect the output and are vertical.

## Shifts

### Vertical Shifts

- $f(x)+c$: up $c$ units.
- $f(x)-c$: down $c$ units.

### Horizontal Shifts

- $f(x-c)$: right $c$ units.
- $f(x+c)$: left $c$ units.

### Reflections

- $-f(x)$: reflect across the $x$-axis.
- $f(-x)$: reflect across the $y$-axis.

## Scaling

### Vertical Scaling

- $af(x)$ with $a>1$: vertical stretch.
- $af(x)$ with $0<a<1$: vertical compression.

### Horizontal Scaling

- $f(ax)$ with $a>1$: horizontal compression.
- $f(ax)$ with $0<a<1$: horizontal stretch.

## Order of Transformations

1. Handle inside, horizontal changes.
2. Handle outside, vertical changes.

## Quick Recognition

- $f(x+3)$: left $3$.
- $f(x-3)$: right $3$.
- $f(x)+3$: up $3$.
- $2f(x)$: vertical stretch.
- $f(2x)$: horizontal compression.
- $-f(x)$: reflection across the $x$-axis.

---

## Slope

Average rate of change:

```math
m=\frac{f(b)-f(a)}{b-a}
```

Slope through two points:

```math
m=\frac{y_2-y_1}{x_2-x_1}
```

---

## Removable Discontinuity vs. Vertical Asymptote

- A factor that cancels usually creates a **hole**.
- A denominator factor that remains after simplification usually creates a **vertical asymptote**.

---

## Tangent Line at a Given Point

1. Differentiate to find $f'(x)$, the slope function.
2. Evaluate $m=f'(a)$ to find the slope at $x=a$.
3. Evaluate $f(a)$ to find the point $(a,f(a))$.
4. Use point-slope form:

```math
y-f(a)=f'(a)(x-a)
```

5. Simplify only if requested.

### What Each Step Produces

- $f'(x)$: slope formula.
- $f'(a)$: slope at the point.
- $f(a)$: vertical coordinate of the point.
- Point-slope form: tangent-line equation.

---

## Polynomial and Exponential Comparison

When a polynomial and an exponential function intersect, compare them on each side of the intersection. For large positive $x$, a positive-base exponential with base greater than $1$ eventually dominates every polynomial.

---

## Quotient Rule

```math
\left(\frac{f}{g}\right)'
=\frac{gf'-fg'}{g^2}
```

Memory phrase: **low times derivative of high minus high times derivative of low, over low squared**.

---

## Implicit Differentiation: Starting Steps

1. Differentiate both sides with respect to $x$.
2. Treat $y$ as a function of $x$.
3. Attach $y'$ whenever a term involving $y$ is differentiated.
4. Apply the product and chain rules as needed.
5. Move all $y'$ terms to one side.
6. Factor out $y'$ and solve.

Examples:

```math
\frac{d}{dx}(y)=y'
```

```math
\frac{d}{dx}(y^2)=2yy'
```

```math
\frac{d}{dx}(\sin y)=\cos(y)y'
```

---

## Symmetry in Definite Integrals

| Pattern | Immediate Thought |
|---|---|
| $\int_{-a}^{a}f(x)\,dx$ | Check whether $f$ is odd or even before integrating. |
| $f$ is odd | $\int_{-a}^{a}f(x)\,dx=0$ |
| $f$ is even | $\int_{-a}^{a}f(x)\,dx=2\int_0^a f(x)\,dx$ |
