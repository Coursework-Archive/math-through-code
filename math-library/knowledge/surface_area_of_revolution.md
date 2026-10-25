# Surface Area of Revolution

A surface of revolution is formed when a curve is rotated about an axis.

The basic idea is:

```math
\boxed{
dS=(\text{circumference})(\text{arc length element})
}
```

Since the circumference of a circle is $2\pi r$,

```math
\boxed{
dS=2\pi r\,ds
}
```

Therefore,

```math
\boxed{
S=\int 2\pi r\,ds
}
```

The radius $r$ is the distance from the curve to the axis of rotation.

---

## Arc Length Element

Surface area uses the same $ds$ from arc length.

If the curve is written as $y=f(x)$,

```math
ds=
\sqrt{1+\left(\frac{dy}{dx}\right)^2}\,dx
```

If the curve is written as $x=g(y)$,

```math
ds=
\sqrt{1+\left(\frac{dx}{dy}\right)^2}\,dy
```

---

# Rotation About the $x$-Axis

When a curve is rotated about the $x$-axis, the radius is the vertical distance to the axis.

For a curve above the $x$-axis,

```math
r=y
```

so

```math
\boxed{
S=\int 2\pi y\,ds
}
```

---

## About the $x$-Axis: Integrating with Respect to $x$

If

```math
y=f(x),
\qquad
a\leq x\leq b
```

then

```math
\boxed{
S=
\int_a^b
2\pi y
\sqrt{1+\left(\frac{dy}{dx}\right)^2}\,dx
}
```

or

```math
S=
\int_a^b
2\pi f(x)
\sqrt{1+\left[f'(x)\right]^2}\,dx
```

---

## About the $x$-Axis: Integrating with Respect to $y$

If

```math
x=g(y),
\qquad
c\leq y\leq d
```

then

```math
\boxed{
S=
\int_c^d
2\pi y
\sqrt{1+\left(\frac{dx}{dy}\right)^2}\,dy
}
```

---

# Rotation About the $y$-Axis

When a curve is rotated about the $y$-axis, the radius is the horizontal distance to the axis.

For a curve to the right of the $y$-axis,

```math
r=x
```

so

```math
\boxed{
S=\int 2\pi x\,ds
}
```

---

## About the $y$-Axis: Integrating with Respect to $x$

If

```math
y=f(x),
\qquad
a\leq x\leq b
```

then

```math
\boxed{
S=
\int_a^b
2\pi x
\sqrt{1+\left(\frac{dy}{dx}\right)^2}\,dx
}
```

---

## About the $y$-Axis: Integrating with Respect to $y$

If

```math
x=g(y),
\qquad
c\leq y\leq d
```

then

```math
\boxed{
S=
\int_c^d
2\pi x
\sqrt{1+\left(\frac{dx}{dy}\right)^2}\,dy
}
```

or

```math
S=
\int_c^d
2\pi g(y)
\sqrt{1+\left[g'(y)\right]^2}\,dy
```

---

## Radius Recognition Rule

The radius is always the distance from the curve to the axis of rotation.

| Axis of Rotation | Radius |
|---|---|
| $x$-axis | $y$ |
| $y$-axis | $x$ |

```math
\boxed{
\text{Rotate about the }x\text{-axis}
\Longrightarrow
r=y
}
```

```math
\boxed{
\text{Rotate about the }y\text{-axis}
\Longrightarrow
r=x
}
```

---

## Surface Area Formula Table

| Rotation | Integrate With Respect To | Formula |
|---|---|---|
| About $x$-axis | $x$ | $S=\displaystyle\int_a^b2\pi y\sqrt{1+\left(\dfrac{dy}{dx}\right)^2}\,dx$ |
| About $x$-axis | $y$ | $S=\displaystyle\int_c^d2\pi y\sqrt{1+\left(\dfrac{dx}{dy}\right)^2}\,dy$ |
| About $y$-axis | $x$ | $S=\displaystyle\int_a^b2\pi x\sqrt{1+\left(\dfrac{dy}{dx}\right)^2}\,dx$ |
| About $y$-axis | $y$ | $S=\displaystyle\int_c^d2\pi x\sqrt{1+\left(\dfrac{dx}{dy}\right)^2}\,dy$ |

---

## Surface Area Setup Process

1. Identify the axis of rotation.
2. Determine the radius.
3. Decide whether to integrate with respect to $x$ or $y$.
4. Rewrite the curve if necessary.
5. Find the appropriate derivative.
6. Build the arc length element $ds$.
7. Multiply by $2\pi r$.
8. Apply the bounds.
9. Evaluate the resulting integral if required.

---

## Recognition Pattern

Start with

```math
\boxed{
S=\int 2\pi r\,ds
}
```

Then determine the two pieces separately.

### Radius

```math
r=
\begin{cases}
y, & \text{rotation about the }x\text{-axis} \\
x, & \text{rotation about the }y\text{-axis}
\end{cases}
```

### Arc Length Element

```math
ds=
\begin{cases}
\sqrt{1+\left(\dfrac{dy}{dx}\right)^2}\,dx,
& \text{integrating with respect to }x \\[6pt]
\sqrt{1+\left(\dfrac{dx}{dy}\right)^2}\,dy,
& \text{integrating with respect to }y
\end{cases}
```

---

## Arc Length vs. Surface Area

Arc length:

```math
L=\int ds
```

Surface area:

```math
S=\int 2\pi r\,ds
```

The difference is the circumference factor $2\pi r$.

```math
\boxed{
\text{Surface area}
=
(\text{circumference})
\times
(\text{arc length})
}
```

---

## Common Mistakes

- Using $y$ as the radius when rotating about the $y$-axis.
- Using $x$ as the radius when rotating about the $x$-axis.
- Using $\dfrac{dy}{dx}$ while integrating with respect to $y$.
- Using $\dfrac{dx}{dy}$ while integrating with respect to $x$.
- Forgetting to square the derivative.
- Forgetting the factor $2\pi r$.
- Changing from $dx$ to $dy$ without also changing the bounds.
- Solving for the wrong variable before differentiating.

---

## Memory Rule

```math
\boxed{
S=\int 2\pi r\,ds
}
```

Think:

```math
\boxed{
\text{radius}
\times
\text{arc length factor}
}
```

About the $x$-axis:

```math
r=y
```

About the $y$-axis:

```math
r=x
```