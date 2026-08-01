# Applications of Integration

## Quick Reference

| Situation | Formula | Memory Phrase |
|---|---|---|
| Area under a curve | $A=\int_a^b f(x)\,dx$ | Height |
| Area between curves | $A=\int_a^b(\text{top}-\text{bottom})\,dx$ | Top minus bottom |
| Area with respect to $y$ | $A=\int_c^d(\text{right}-\text{left})\,dy$ | Right minus left |
| Disk method | $V=\pi\int_a^b R^2\,dx$ | One circle |
| Washer method | $V=\pi\int_a^b(R^2-r^2)\,dx$ | Big circle minus small circle |
| Shell method | $V=2\pi\int_a^b(\text{radius})(\text{height})\,dx$ | Circumference times height |

- No hole: use the **disk method**.
- Hole in the middle: use the **washer method**.
- Washers use slices perpendicular to the axis of rotation.
- Shells use slices parallel to the axis of rotation.

---

## Choosing Slices and Variables

### Horizontal Axis of Rotation

Examples: the $x$-axis, $y=1$, or $y=-3$.

- Disks or washers: vertical slices, integrate with respect to $x$.
- Shells: horizontal slices, integrate with respect to $y$.

### Vertical Axis of Rotation

Examples: the $y$-axis, $x=0$, or $x=2$.

- Disks or washers: horizontal slices, integrate with respect to $y$.
- Shells: vertical slices, integrate with respect to $x$.

### Shell-Method Checklist

1. Are the slices vertical or horizontal?
2. In which direction is the shell height measured?
   - Vertical slices: top minus bottom.
   - Horizontal slices: right minus left.
3. What is the radius?
   - Radius is the distance from the slice to the axis of rotation.
4. Only then choose $dx$ or $dy$.

---

## Area Under a Curve

If the region is bounded by $y=f(x)$, the $x$-axis, $x=a$, and $x=b$, then

```math
A=\int_a^b f(x)\,dx.
```

Memory phrase: **height times thickness**.

- Height: $f(x)$.
- Thickness: $dx$.

---

## Area Between Two Curves

If the top curve is $f(x)$ and the bottom curve is $g(x)$, then

```math
A=\int_a^b\left[f(x)-g(x)\right]dx.
```

Memory phrase: **top minus bottom**.

---

## Area Between Curves with Respect to $y$

If the right curve is $x=f(y)$ and the left curve is $x=g(y)$, then

```math
A=\int_c^d\left[f(y)-g(y)\right]dy.
```

Memory phrase: **right minus left**.

---

## Disk Method

Use the disk method when rotating a region that has no hole.

```math
V=\pi\int_a^b R(x)^2\,dx.
```

Here, $R(x)$ is the radius from the axis of rotation to the outer edge of the region.

The cross-sectional area is

```math
A(x)=\pi R(x)^2.
```

---

## Washer Method

Use the washer method when the rotated region has a hole.

```math
V=\pi\int_a^b\left[R(x)^2-r(x)^2\right]dx.
```

- $R(x)$ is the outer radius.
- $r(x)$ is the inner radius.

Memory phrase: **outer radius squared minus inner radius squared**.

---

## Shell Method

```math
V=2\pi\int_a^b
(\text{radius})(\text{height})\,dx.
```

A shell's volume comes from

```math
(\text{circumference})(\text{height})(\text{thickness}).
```

- Radius: distance from the slice to the axis of rotation.
- Height: top minus bottom for vertical slices, or right minus left for horizontal slices.

---

## Recognition Guide

### No Rotation

Use an area integral:

```math
A=\int f(x)\,dx
```

or

```math
A=\int(\text{top}-\text{bottom})\,dx.
```

### Rotation with No Hole

Use the disk method:

```math
V=\pi\int R^2\,dx.
```

### Rotation with a Hole

Use the washer method:

```math
V=\pi\int(R^2-r^2)\,dx.
```

### Radius and Height Are Easier to Describe

Use the shell method:

```math
V=2\pi\int(\text{radius})(\text{height})\,dx.
```

---

## Fundamental Patterns

### Area

- Vertical slices: top minus bottom.
- Horizontal slices: right minus left.

### Volume

Disk cross section:

```math
\pi R^2
```

Washer cross section:

```math
\pi(R^2-r^2)
```

Shell factor:

```math
2\pi(\text{radius})(\text{height})
```
