# Calculus I Trigonometry Reference

![Unit Circle](images/unit_circle.jpg)


# Unit Circle (Key Angles)

| $\theta$ | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
|---|---:|---:|---:|
| $0$ | $0$ | $1$ | $0$ |
| $\frac{\pi}{6}$ | $\frac12$ | $\frac{\sqrt3}{2}$ | $\frac{\sqrt3}{3}$ |
| $\frac{\pi}{4}$ | $\frac{\sqrt2}{2}$ | $\frac{\sqrt2}{2}$ | $1$ |
| $\frac{\pi}{3}$ | $\frac{\sqrt3}{2}$ | $\frac12$ | $\sqrt3$ |
| $\frac{\pi}{2}$ | $1$ | $0$ | undefined |
| $\pi$ | $0$ | $-1$ | $0$ |

Point on the unit circle:

$$
(x,y)=(\cos\theta,\sin\theta)
$$

---

# Derivatives

## Trigonometric Derivatives

| Function | Derivative |
|---|---|
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2x$ |
| $\cot x$ | $-\csc^2x$ |
| $\sec x$ | $\sec x\tan x$ |
| $\csc x$ | $-\csc x\cot x$ |

---

## Inverse Trigonometric Derivatives

| Function | Derivative |
|---|---|
| $\arcsin x$ | $\dfrac{1}{\sqrt{1-x^2}}$ |
| $\arccos x$ | $-\dfrac{1}{\sqrt{1-x^2}}$ |
| $\arctan x$ | $\dfrac{1}{1+x^2}$ |

---

## Chain Rule Forms

$$
\frac{d}{dx}\left[\arcsin(u)\right]
=
\frac{u'}{\sqrt{1-u^2}}
$$

$$
\frac{d}{dx}\left[\arccos(u)\right]
=
-\frac{u'}{\sqrt{1-u^2}}
$$

$$
\frac{d}{dx}\left[\arctan(u)\right]
=
\frac{u'}{1+u^2}
$$

---

# Antiderivatives

## Trigonometric Antiderivatives


| Integrand | Antiderivative |
|---|---|
| $\sin x$ | $-\cos x+C$ |
| $\cos x$ | $\sin x+C$ |
| $\tan x$ | $\ln\left(\sec x\right)+C$ |
| $\cot x$ | $\ln\left(\sin x\right)+C$ |
| $\sec^2x$ | $\tan x+C$ |
| $\csc^2x$ | $-\cot x+C$ |
| $\sec x\tan x$ | $\sec x+C$ |
| $\csc x\cot x$ | $-\csc x+C$ |
| $\sec x$ | $\ln\left(\sec x+\tan x\right)+C$ |
| $\csc x$ | $\ln\left(\csc x-\cot x\right)+C$ |

### Equivalent Forms

$$
\int\tan x\,dx
=
-\ln\left(\cos x\right)+C
=
\ln\left(\sec x\right)+C
$$

$$
\int\cot x\,dx
=
\ln\left(\sin x\right)+C
=
-\ln\left(\csc x\right)+C
$$

$$
\int\sec x\,dx
=
\ln\left|\sec x+\tan x\right|+C
$$

$$
\int\csc x\,dx
=
\ln\left|\csc x-\cot x\right|+C
=
-\ln\left|\csc x+\cot x\right|+C
$$

---

## Power Rule

| Integrand | Antiderivative |
|---|---|
| $x^n,\;n\neq -1$ | $\dfrac{x^{n+1}}{n+1}+C$ |

---

## Exponential and Logarithmic Integrals

| Integrand | Antiderivative |
|---|--|
| $e^x$ | $e^x+C$ |
| $a^x$ | $\dfrac{a^x}{\ln a}+C$ |
| $\dfrac1x$ | $\ln\lvert x\rvert+C$ |

---

# Inverse Trigonometric Functions

## Principal Domains and Ranges

| Function | Domain | Range |
|---|---|---|
| $\arcsin x$ | $[-1,1]$ | $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$ |
| $\arccos x$ | $[-1,1]$ | $[0,\pi]$ |
| $\arctan x$ | $(-\infty,\infty)$ | $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$ |

---

## Inverse Trig Process

1. Find the unit circle angle.
2. Check the principal range.
3. That angle is the answer.

---




# Trigonometric Definitions

| Function | Ratio | Unit Circle |
|---|---|---|
| $\sin\theta$ | opposite/hypotenuse | $y$ |
| $\cos\theta$ | adjacent/hypotenuse | $x$ |
| $\tan\theta$ | $\dfrac{\sin\theta}{\cos\theta}$ | $\dfrac{y}{x}$ |
| $\cot\theta$ | $\dfrac{\cos\theta}{\sin\theta}$ | $\dfrac{x}{y}$ |
| $\sec\theta$ | $\dfrac1{\cos\theta}$ | $\dfrac1x$ |
| $\csc\theta$ | $\dfrac1{\sin\theta}$ | $\dfrac1y$ |

---

# Trigonometric Identities

## Reciprocal Identities

$$
\sec x=\frac1{\cos x}
$$

$$
\csc x=\frac1{\sin x}
$$

$$
\cot x=\frac1{\tan x}
$$

### Squared Reciprocal Identity

$$
\boxed{\sec^2x=\frac1{\cos^2x}}
$$

---

## Quotient Identities

$$
\tan x=\frac{\sin x}{\cos x}
$$

$$
\cot x=\frac{\cos x}{\sin x}
$$

---

## Pythagorean Identities

$$
\sin^2x+\cos^2x=1
$$

$$
1+\tan^2x=\sec^2x
$$

$$
1+\cot^2x=\csc^2x
$$

### Rearrangements

$$
\tan^2x=\sec^2x-1
$$

$$
\cot^2x=\csc^2x-1
$$

$$
\sec^2x-\tan^2x=1
$$

$$
\csc^2x-\cot^2x=1
$$

---

## Double-Angle Identities

$$
\boxed{\sin(2x)=2\sin x\cos x}
$$

$$
\cos(2x)=\cos^2x-\sin^2x
$$

$$
\cos(2x)=2\cos^2x-1
$$

$$
\cos(2x)=1-2\sin^2x
$$

---

# Recognition Rules

| If You See | Think |
|---|---|
| $\dfrac1{\cos^2x}$ | $\sec^2x$ |
| $\sec^2x\,dx$ | $d(\tan x)$ |
| $\csc^2x\,dx$ | $-d(\cot x)$ |
| $\sec x\tan x\,dx$ | $d(\sec x)$ |
| $\csc x\cot x\,dx$ | $-d(\csc x)$ |
| $\sin(2x)$ | $2\sin x\cos x$ |
| $\sin x\cos x\,dx$ | Double-angle or $u=\cos x$ |
| $\dfrac{\sin x}{\cos x}$ | $\tan x$ |
| $\dfrac{\cos x}{\sin x}$ | $\cot x$ |
| $1+\tan^2x$ | $\sec^2x$ |
| $1+\cot^2x$ | $\csc^2x$ |
| $\sqrt{1+\tan x}$ | $u=1+\tan x$ |
| $1+\cos^2x$ | $u=1+\cos^2x$ |
| $1+x^2$ | arctan derivative |
| $\sqrt{1-x^2}$ | arcsin or arccos derivative |
| $\dfrac1x$ | $\ln\lvert x\rvert+C$ |

---

# Three Most Important Identities

$$
\boxed{\sin^2x+\cos^2x=1}
$$

$$
\boxed{1+\tan^2x=\sec^2x}
$$

$$
\boxed{1+\cot^2x=\csc^2x}
$$

---

# Three Most Important Derivative–Antiderivative Pairs

$$
\boxed{
\frac{d}{dx}(\tan x)=\sec^2x
\qquad\Longleftrightarrow\qquad
\int\sec^2x\,dx=\tan x+C
}
$$

$$
\boxed{
\frac{d}{dx}(\sec x)=\sec x\tan x
\qquad\Longleftrightarrow\qquad
\int\sec x\tan x\,dx=\sec x+C
}
$$

$$
\boxed{
\frac{d}{dx}(\sin x)=\cos x
\qquad\Longleftrightarrow\qquad
\int\cos x\,dx=\sin x+C
}
$$
