# SESSION 15 - 1 hr 20 mins

Must Do
3 — Sketching shells before integrating. Great conceptual review.
4 — Another geometry/setup problem with a graph.
21 — Solve the same volume both ways (x and y). Excellent conceptual exercise.
22 — Same idea as #21 but different curves.

## Pattern:
Right/left curve confusion after rewriting equations in terms of \(y\).

Mistake:

After deciding to integrate with respect to \(y\), I rewrote the equations in terms of \(y\), but I confused which curve was on the **right** and which curve was on the **left**.

For horizontal slices, the width/height of the slice must be:

$$
\text{right curve} - \text{left curve}.
$$

I need to compare the \(x\)-values of the curves for a typical \(y\)-value before subtracting.

### Type

- [ ] Algebra
- [x] Concept
- [x] Recognition
- [ ] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

When integrating with respect to \(y\), always identify curves as \(x=\text{right}\) and \(x=\text{left}\), then subtract:

$$
\text{right} - \text{left}.
$$

Do not use top minus bottom when working in terms of \(y\).

---

## Pattern:
Forgot to convert the bounds after changing everything to \(y\).

Mistake:

After rewriting all equations in terms of \(y\), I kept the original \(x\)-bounds instead of converting them to \(y\)-bounds.

This caused the integral to mix variables: the integrand was written in terms of \(y\), but the limits still belonged to \(x\).

### Type

- [ ] Algebra
- [x] Concept
- [ ] Recognition
- [x] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

Once the integral is written in terms of \(y\), the bounds must also be \(y\)-values. Convert the intersection points or given boundaries into \(y\)-bounds before evaluating.

Memory cue:

$$
dy \Rightarrow y\text{-bounds}
$$

$$
dx \Rightarrow x\text{-bounds}
$$

23 — Multi-part shell problem with translated axis.


24 — Another graphical shell problem with intersecting curves.

These six problems will strengthen the concepts that matter most.


# SESSION 16 - mins
Good Challenge Problems

If you still have energy afterward:

25 — Shells with an axis shifted to x=−3.

## Pattern:

Used the correct shell method and radius, but wrote the shell height incorrectly by subtracting the curve from the axis value instead of using the top boundary.

Mistake:

I wrote the shell height as $3 - x^3$ instead of $8 - x^3$. The shell height is always the **top function minus the bottom function**, not the distance to the axis of rotation.

### Type

- [ ] Algebra
- [x] Concept
- [x] Recognition
- [ ] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

For the shell method, identify the height from the bounding curves first: $\text{height} = \text{top} - \text{bottom}$. The axis of rotation is used only to find the radius.

---

26 — Another translated-axis shell problem.

## Pattern:

Shell Method

Mistake:

I used the y-intercept of the function as the top of the shell instead of identifying the actual top boundary of the region. I calculated the height as \(4-(4-2x)\) instead of \((4-2x)-0\).

### Type

- [ ] Algebra
- [x] Concept
- [x] Recognition
- [ ] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

The shell height is always **top boundary − bottom boundary** of the region. Determine the height by tracing a vertical slice through the shaded region, not by using the function's y-intercept or the largest y-value shown on the graph.

---

28 — Rotation about x=5. Good practice with shifted radii.

---

29 — More algebra than setup.

## Pattern:

Measured the shell height from the coordinate axis instead of between the two boundary curves when using horizontal shells.

Mistake:

For horizontal shells, I used

$$
h = 2y^2
$$

which is the distance from the **y-axis** to the parabola. The shell actually extends from

$$
x = 2y^2
$$

to

$$
x = 2,
$$

so the correct height is

$$
h = 2 - 2y^2.
$$

### Type

- [ ] Algebra
- [x] Concept
- [x] Recognition
- [ ] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

For shell methods, the shell height is always measured **across the region**:
- Vertical shells: **top curve $-$ bottom curve**
- Horizontal shells: **right curve $-$ left curve**

Never measure the shell height from the coordinate axis unless the axis is actually one of the region's boundaries.


30 — Harder algebra with shells.

## Pattern:

Integrated the last term as if it were $-2y$ instead of $-2y^2$, causing an incorrect antiderivative and final evaluation.

**Mistake:**

The integrand contained $-2y^2$, but I wrote its antiderivative as $-y^2$ instead of correctly applying the power rule:

$$
\int -2y^2\,dy = -\frac{2}{3}y^3.
$$

### Type

- [ ] Algebra
- [ ] Concept
- [ ] Recognition
- [x] Careless

### Fixed?

- [x] Yes
- [ ] Partial
- [ ] No

### Fix Rule

When integrating polynomial terms, verify each exponent before applying the power rule: **increase the exponent by 1 and divide by the new exponent.**

---

Total for 7/3 ( 1 hr 40 mins)
Total for 7/4 (2 hrs)
Total Study Cumulative Time (25 hrs 20 mins)