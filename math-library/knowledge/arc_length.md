# Arc Length

Arc length measures the distance along a smooth curve between two points.

---

## Arc Length for $y=f(x)$

If the curve is written as

```math
y=f(x),
\qquad
a\leq x\leq b
```

then the arc length is

```math
\boxed{
L=\int_a^b
\sqrt{1+\left(\frac{dy}{dx}\right)^2}\,dx
}
```

Equivalently,

```math
L=\int_a^b
\sqrt{1+\left[f'(x)\right]^2}\,dx
```

### Recognition Rule

If the bounds are in terms of $x$ and the curve is naturally written as $y=f(x)$, use

```math
\boxed{
\sqrt{1+\left(\frac{dy}{dx}\right)^2}\,dx
}
```

---

## Arc Length for $x=g(y)$

If the curve is written as

```math
x=g(y),
\qquad
c\leq y\leq d
```

then the arc length is

```math
\boxed{
L=\int_c^d
\sqrt{1+\left(\frac{dx}{dy}\right)^2}\,dy
}
```

### Recognition Rule

If the bounds are in terms of $y$ and the curve is naturally written as $x=g(y)$, use

```math
\boxed{
\sqrt{1+\left(\frac{dx}{dy}\right)^2}\,dy
}
```

---

## Differential of Arc Length

The differential of arc length is denoted by $ds$.

When integrating with respect to $x$,

```math
\boxed{
ds=
\sqrt{1+\left(\frac{dy}{dx}\right)^2}\,dx
}
```

When integrating with respect to $y$,

```math
\boxed{
ds=
\sqrt{1+\left(\frac{dx}{dy}\right)^2}\,dy
}
```

The symmetric relationship is

```math
\boxed{
(ds)^2=(dx)^2+(dy)^2
}
```

This is the Pythagorean relationship behind the arc length formula.

---

## Why the Formula Works

Over a very small interval, a smooth curve behaves approximately like a straight line segment.

For a small change in $x$ and $y$,

```math
(\Delta s)^2
\approx
(\Delta x)^2+(\Delta y)^2
```

so

```math
\Delta s
\approx
\sqrt{(\Delta x)^2+(\Delta y)^2}
```

Factoring out $\Delta x$ gives the $x$-form of the arc length formula.

As the interval widths approach $0$, the sum of the small line-segment lengths becomes an integral.

---

## Arc Length Setup Process

1. Identify whether the curve is easier to use as $y=f(x)$ or $x=g(y)$.
2. Identify whether the bounds are $x$-values or $y$-values.
3. Differentiate the curve.
4. Square the derivative.
5. Add $1$.
6. Take the square root.
7. Integrate over the given interval.

### Using $x$

```math
y=f(x)
\Longrightarrow
\frac{dy}{dx}
\Longrightarrow
L=
\int_a^b
\sqrt{1+\left(\frac{dy}{dx}\right)^2}\,dx
```

### Using $y$

```math
x=g(y)
\Longrightarrow
\frac{dx}{dy}
\Longrightarrow
L=
\int_c^d
\sqrt{1+\left(\frac{dx}{dy}\right)^2}\,dy
```

---

## Choosing $dx$ or $dy$

| Curve Form | Derivative | Arc Length Element |
|---|---|---|
| $y=f(x)$ | $\dfrac{dy}{dx}$ | $\sqrt{1+\left(\dfrac{dy}{dx}\right)^2}\,dx$ |
| $x=g(y)$ | $\dfrac{dx}{dy}$ | $\sqrt{1+\left(\dfrac{dx}{dy}\right)^2}\,dy$ |

Use the form that makes the curve and bounds simplest.

---

## Arc Length Function

If $s(x)$ measures the distance along a curve from $x=a$ to a variable point $x$, then

```math
s(x)=
\int_a^x
\sqrt{1+\left[f'(t)\right]^2}\,dt
```

The variable $t$ is used inside the integral so that $x$ can remain the upper limit.

By the Fundamental Theorem of Calculus,

```math
\boxed{
\frac{ds}{dx}
=
\sqrt{1+\left[f'(x)\right]^2}
}
```

---

## Memory Rule

```math
\boxed{
\text{Arc length}
=
\int \sqrt{1+(\text{derivative})^2}
}
```

Match the derivative and differential:

```math
\frac{dy}{dx}
\Longleftrightarrow
dx
```

```math
\frac{dx}{dy}
\Longleftrightarrow
dy
```