# Calculus I Trigonometry Reference

![Unit Circle](images/unit_circle.jpg)

## Unit Circle: Key Angles

| $\theta$ | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
|---|---:|---:|---:|
| $0$ | $0$ | $1$ | $0$ |
| $\frac{\pi}{6}$ | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{3}}{3}$ |
| $\frac{\pi}{4}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | $1$ |
| $\frac{\pi}{3}$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ | $\sqrt{3}$ |
| $\frac{\pi}{2}$ | $1$ | $0$ | undefined |
| $\pi$ | $0$ | $-1$ | $0$ |

A point on the unit circle has coordinates

```math
(x,y)=(\cos\theta,\sin\theta).
```

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

## Inverse-Trigonometric Derivatives

| Function | Derivative |
|---|---|
| $\arcsin x$ | $\dfrac{1}{\sqrt{1-x^2}}$ |
| $\arccos x$ | $-\dfrac{1}{\sqrt{1-x^2}}$ |
| $\arctan x$ | $\dfrac{1}{1+x^2}$ |

## Chain-Rule Forms

```math
\frac{d}{dx}\left[\arcsin(u)\right]
=\frac{u'}{\sqrt{1-u^2}}
```

```math
\frac{d}{dx}\left[\arccos(u)\right]
=-\frac{u'}{\sqrt{1-u^2}}
```

```math
\frac{d}{dx}\left[\arctan(u)\right]
=\frac{u'}{1+u^2}
```

---

# Antiderivatives

## Trigonometric Antiderivatives

| Integrand | Antiderivative |
|---|---|
| $\sin x$ | $-\cos x+C$ |
| $\cos x$ | $\sin x+C$ |
| $\tan x$ | $\ln\lvert\sec x\rvert+C$ |
| $\cot x$ | $\ln\lvert\sin x\rvert+C$ |
| $\sec^2x$ | $\tan x+C$ |
| $\csc^2x$ | $-\cot x+C$ |
| $\sec x\tan x$ | $\sec x+C$ |
| $\csc x\cot x$ | $-\csc x+C$ |
| $\sec x$ | $\ln\lvert\sec x+\tan x\rvert+C$ |
| $\csc x$ | $\ln\lvert\csc x-\cot x\rvert+C$ |

### Equivalent Forms

```math
\int\tan x\,dx
=-\ln\lvert\cos x\rvert+C
=\ln\lvert\sec x\rvert+C
```

```math
\int\cot x\,dx
=\ln\lvert\sin x\rvert+C
=-\ln\lvert\csc x\rvert+C
```

```math
\int\sec x\,dx
=\ln\lvert\sec x+\tan x\rvert+C
```

```math
\int\csc x\,dx
=\ln\lvert\csc x-\cot x\rvert+C
=-\ln\lvert\csc x+\cot x\rvert+C
```

## Power Rule

| Integrand | Antiderivative |
|---|---|
| $x^n,\;n\ne -1$ | $\dfrac{x^{n+1}}{n+1}+C$ |

## Exponential and Logarithmic Integrals

| Integrand | Antiderivative |
|---|---|
| $e^x$ | $e^x+C$ |
| $a^x$ | $\dfrac{a^x}{\ln a}+C$ |
| $\dfrac{1}{x}$ | $\ln\lvert x\rvert+C$ |

---

# Inverse Trigonometric Functions

## Principal Domains and Ranges

| Function | Domain | Range |
|---|---|---|
| $\arcsin x$ | $[-1,1]$ | $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$ |
| $\arccos x$ | $[-1,1]$ | $[0,\pi]$ |
| $\arctan x$ | $(-\infty,\infty)$ | $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$ |

## Inverse-Trigonometric Process

1. Find the corresponding unit-circle angle.
2. Check the principal range of the inverse function.
3. Select the angle in that range.

---

# Trigonometric Definitions

| Function | Right-Triangle Ratio | Unit-Circle Form |
|---|---|---|
| $\sin\theta$ | opposite/hypotenuse | $y$ |
| $\cos\theta$ | adjacent/hypotenuse | $x$ |
| $\tan\theta$ | $\dfrac{\sin\theta}{\cos\theta}$ | $\dfrac{y}{x}$ |
| $\cot\theta$ | $\dfrac{\cos\theta}{\sin\theta}$ | $\dfrac{x}{y}$ |
| $\sec\theta$ | $\dfrac{1}{\cos\theta}$ | $\dfrac{1}{x}$ |
| $\csc\theta$ | $\dfrac{1}{\sin\theta}$ | $\dfrac{1}{y}$ |

---

# Trigonometric Identities

## Reciprocal Identities

```math
\sec x=\frac{1}{\cos x}
```

```math
\csc x=\frac{1}{\sin x}
```

```math
\cot x=\frac{1}{\tan x}
```

```math
\boxed{\sec^2x=\frac{1}{\cos^2x}}
```

## Quotient Identities

```math
\tan x=\frac{\sin x}{\cos x}
```

```math
\cot x=\frac{\cos x}{\sin x}
```

## Pythagorean Identities

```math
\sin^2x+\cos^2x=1
```

```math
1+\tan^2x=\sec^2x
```

```math
1+\cot^2x=\csc^2x
```

### Rearrangements

```math
\tan^2x=\sec^2x-1
```

```math
\cot^2x=\csc^2x-1
```

```math
\sec^2x-\tan^2x=1
```

```math
\csc^2x-\cot^2x=1
```

## Double-Angle Identities

```math
\boxed{\sin(2x)=2\sin x\cos x}
```

```math
\cos(2x)=\cos^2x-\sin^2x
```

```math
\cos(2x)=2\cos^2x-1
```

```math
\cos(2x)=1-2\sin^2x
```

---

# Recognition Rules

| If You See | Think |
|---|---|
| $\dfrac{1}{\cos^2x}$ | $\sec^2x$ |
| $\sec^2x\,dx$ | $d(\tan x)$ |
| $\csc^2x\,dx$ | $-d(\cot x)$ |
| $\sec x\tan x\,dx$ | $d(\sec x)$ |
| $\csc x\cot x\,dx$ | $-d(\csc x)$ |
| $\sin(2x)$ | $2\sin x\cos x$ |
| $\sin x\cos x\,dx$ | Double-angle identity or $u=\cos x$ |
| $\dfrac{\sin x}{\cos x}$ | $\tan x$ |
| $\dfrac{\cos x}{\sin x}$ | $\cot x$ |
| $1+\tan^2x$ | $\sec^2x$ |
| $1+\cot^2x$ | $\csc^2x$ |
| $\sqrt{1+\tan x}$ | Consider $u=1+\tan x$ |
| $1+\cos^2x$ | Consider $u=1+\cos^2x$ |
| $1+x^2$ | Arctangent derivative pattern |
| $\sqrt{1-x^2}$ | Arcsine or arccosine derivative pattern |
| $\dfrac{1}{x}$ | $\ln\lvert x\rvert+C$ |

---

# Three Most Important Identities

```math
\boxed{\sin^2x+\cos^2x=1}
```

```math
\boxed{1+\tan^2x=\sec^2x}
```

```math
\boxed{1+\cot^2x=\csc^2x}
```

---

# Three Important Derivative–Antiderivative Pairs

```math
\boxed{\frac{d}{dx}(\tan x)=\sec^2x
\quad\Longleftrightarrow\quad
\int\sec^2x\,dx=\tan x+C}
```

```math
\boxed{\frac{d}{dx}(\sec x)=\sec x\tan x
\quad\Longleftrightarrow\quad
\int\sec x\tan x\,dx=\sec x+C}
```

```math
\boxed{\frac{d}{dx}(\sin x)=\cos x
\quad\Longleftrightarrow\quad
\int\cos x\,dx=\sin x+C}
```
