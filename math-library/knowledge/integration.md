# Applications of Integration


| Situation | Formula | Memory Phrase |
|------------|---------|---------------|
| Area under curve | $A=\int_a^b f(x)\,dx$ | Height |
| Area between curves | $A=\int_a^b(\text{top}-\text{bottom})\,dx$ | Top − Bottom |
| Area with respect to y | $A=\int_c^d(\text{right}-\text{left})\,dy$ | Right − Left |
| Disc Method | $V=\pi\int_a^bR^2\,dx$ | One circle |
| Washer Method | $V=\pi\int_a^b(R^2-r^2)\,dx$ | Big circle − Small circle |
| Shell Method | $V=2\pi\int_a^b(\text{radius})(\text{height})\,dx$ | Circumference × Height |


If no hole, use the disk method.
If there is a hole, use the washer method.

Decide:
 - Washers = perpendicular slices
 - Shells = parallel slices

Every shell problem, ask yourself:
1. Are my slices vertical or horizontal? r?
2. What direction is the height measured? height is opposite r 
   * Vertical slices → Top − Bottom
   * Horizontal slices → Right − Left
3. What is the radius?
   Distance from the slice to the axis of rotation.
   * if the slice is to the left of the axis: radius = axis - slice 
   * if the slice is to the right of the axis: radius = slice - axis
   * if the slice is below the axis: radius = axis - slice 
   * if the slice is above the axis: radius = slice - axis 

Only then decide whether you're integrating with dx or dy.

This is exactly the decision process you'll want on the final exam. Once you identify the axis orientation first, the rest of the setup becomes much more mechanical.



1. Horizontal axis (like y=1, y=−3, or the x-axis)
Washers/disks: use vertical slices ⇒dx
Shells: use horizontal slices ⇒dy
2. Vertical axis (like x=0, x=2, or the y-axis)
Washers/disks: use horizontal slices ⇒dy
Shells: use vertical slices ⇒dx


---

# Area Under a Curve

If the region is bounded by

- $y=f(x)$
- the x-axis
- $x=a$
- $x=b$

then

$$
A=\int_a^b f(x)\,dx
$$

### Memory

Height × Thickness

where

- height $=f(x)$
- thickness $=dx$

---

# Area Between Two Curves

Suppose

- top curve $=f(x)$
- bottom curve $=g(x)$

Then

$$
A=\int_a^b\left(f(x)-g(x)\right)\,dx
$$

### Memory

**Top − Bottom**

---

# Area Between Curves (with respect to y)

Suppose

- right curve $=x=f(y)$
- left curve $=x=g(y)$

Then

$$
A=\int_c^d\left(f(y)-g(y)\right)\,dy
$$

### Memory

**Right − Left**

---

# Disc Method

Used when rotating a region around an axis and there is no hole.

Volume:

$$
V=\pi\int_a^b R(x)^2\,dx
$$

where

- $R(x)$ = radius

### Memory

Area of a circle × thickness

$$
\pi r^2
$$

Think:

**One circle**

---

# Washer Method

Used when rotating a region around an axis and there is a hole.

Volume:

$$
V=\pi\int_a^b\left(R(x)^2-r(x)^2\right)\,dx
$$

where

- $R(x)$ = outer radius
- $r(x)$ = inner radius

### Memory

Big circle − Small circle

Think:

**Outer radius squared minus inner radius squared**

---

# Shell Method

Volume:

$$
V=
2\pi
\int_a^b
(\text{radius})(\text{height})\,dx
$$

### Memory

Circumference × Height × Thickness

where

- radius = distance from axis
- height = top − bottom

Think:

**Cylinder shells**

---

# Recognition Guide

## No Rotation

Area problem

Use:

$$
A=\int f(x)\,dx
$$

or

$$
A=\int(\text{top}-\text{bottom})\,dx
$$

---

## Rotation About an Axis

Volume problem

---

## Solid All the Way Through

Disc Method

$$
V=\pi\int R^2\,dx
$$

---

## Hole in the Middle

Washer Method

$$
V=\pi\int(R^2-r^2)\,dx
$$

---

## Radius and Height Are Easier

Shell Method

$$
V=2\pi\int(\text{radius})(\text{height})\,dx
$$


---
## Fundamental Patterns

### Area

Top − Bottom

or

Right − Left

---

### Volume

Disc:

$$
\pi R^2
$$

Washer:

$$
\pi(R^2-r^2)
$$

Shell:

$$
2\pi(\text{radius})(\text{height})
$$

---