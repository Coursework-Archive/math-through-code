# Hyperbolic Functions Cheat Sheet

## Definitions

$$
\sinh x = \frac{e^x - e^{-x}}{2}
$$

$$
\cosh x = \frac{e^x + e^{-x}}{2}
$$

$$
\tanh x = \frac{\sinh x}{\cosh x}
$$

$$
\csch x = \frac{1}{\sinh x}
$$

$$
\sech x = \frac{1}{\cosh x}
$$

$$
\coth x = \frac{\cosh x}{\sinh x}
$$


---

## Key Identities

$$
\sinh(-x) = -\sinh x
$$

$$
\cosh(-x) = \cosh x
$$

$$
\cosh^2 x - \sinh^2 x = 1
$$

$$
1 - \tanh^2 x = \sech^2 x
$$

$$
\sinh(x + y) = \sinh x \cosh y + \cosh x \sinh y
$$

$$
\cosh(x + y) = \cosh x \cosh y + \sinh x \sinh y
$$


---

## Derivatives

$$
\frac{d}{dx}(\sinh x) = \cosh x
$$

$$
\frac{d}{dx}(\cosh x) = \sinh x
$$

$$
\frac{d}{dx}(\tanh x) = \sech^2 x
$$

$$
\frac{d}{dx}(\csch x) = -\csch x \coth x
$$

$$
\frac{d}{dx}(\sech x) = -\sech x \tanh x
$$

$$
\frac{d}{dx}(\coth x) = -\csch^2 x
$$


---

## Inverse Hyperbolic Functions (Log Forms)

$$
\sinh^{-1} x = \ln\left(x + \sqrt{x^2 + 1}\right)
$$

$$
\cosh^{-1} x = \ln\left(x + \sqrt{x^2 - 1}\right), \quad x \ge 1
$$

$$
\tanh^{-1} x = \frac{1}{2} \ln\left(\frac{1 + x}{1 - x}\right), \quad -1 < x < 1
$$


---

## Derivatives of Inverse Hyperbolic Functions

$$
\frac{d}{dx}(\sinh^{-1} x) = \frac{1}{\sqrt{1 + x^2}}
$$

$$
\frac{d}{dx}(\cosh^{-1} x) = \frac{1}{\sqrt{x^2 - 1}}
$$

$$
\frac{d}{dx}(\tanh^{-1} x) = \frac{1}{1 - x^2}
$$

$$
\frac{d}{dx}(\csch^{-1} x) = -\frac{1}{|x|\sqrt{1 + x^2}}
$$

$$
\frac{d}{dx}(\sech^{-1} x) = -\frac{1}{x\sqrt{1 - x^2}}
$$

$$
\frac{d}{dx}(\coth^{-1} x) = \frac{1}{1 - x^2}
$$

# Hyperbolic Functions – Recognition & Strategy Guide

---

# 1. WHEN DO HYPERBOLIC FUNCTIONS SHOW UP?

## A. Expressions involving exponentials (hidden hyperbolics)

If you see:
$$
\frac{e^x - e^{-x}}{2}, \quad \frac{e^x + e^{-x}}{2}
$$

Think immediately:
$$
\sinh x, \quad \cosh x
$$

👉 Strategy:
Rewrite in hyperbolic form to simplify derivatives/integrals

---

## B. Integrals with $\sqrt{x^2 + 1}$ or $\sqrt{x^2 - 1}$

If you see:
$$
\sqrt{x^2 + 1}
$$
Use:
$$
x = \sinh t
$$

If you see:
$$
\sqrt{x^2 - 1}
$$
Use:
$$
x = \cosh t
$$

👉 Why:
Because:
$$
\cosh^2 t - \sinh^2 t = 1
$$

This simplifies radicals cleanly.

---

## C. Log expressions of this form

If you see:
$$
\ln\left(x + \sqrt{x^2 + 1}\right)
$$

Recognize immediately:
$$
= \sinh^{-1} x
$$

If:
$$
\ln\left(x + \sqrt{x^2 - 1}\right)
$$

Then:
$$
= \cosh^{-1} x
$$

👉 Strategy:
Convert logs → inverse hyperbolic (cleaner derivatives)

---

## D. Derivatives that look like inverse trig (but aren’t)

If you see:
$$
\frac{1}{\sqrt{1 + x^2}}
$$

This is:
$$
\frac{d}{dx}(\sinh^{-1} x)
$$

NOT arctan, NOT arcsin

---

# 2. HYPERBOLIC vs TRIG – QUICK DECISION TABLE

| Expression | Use |
|----------|-----|
| $\sqrt{1 - x^2}$ | trig (sin) |
| $\sqrt{1 + x^2}$ | hyperbolic (sinh) |
| $\sqrt{x^2 - 1}$ | hyperbolic (cosh) |

👉 This is one of the most tested patterns

---

# 3. DERIVATIVE PATTERNS (FAST RECALL)

## Core swaps
$$
\sinh x \leftrightarrow \cosh x
$$

## Key ones to memorize
$$
\frac{d}{dx}(\sinh x) = \cosh x
$$

$$
\frac{d}{dx}(\cosh x) = \sinh x
$$

$$
\frac{d}{dx}(\tanh x) = \sech^2 x
$$

👉 Notice:
No negative signs (unlike trig)

---

# 4. IDENTITIES YOU ACTUALLY USE

## Most important:
$$
\cosh^2 x - \sinh^2 x = 1
$$

Compare:
$$
\sin^2 x + \cos^2 x = 1
$$

👉 Same idea, different sign

---

# 5. COMMON EXAM TRAPS

## Trap 1: Mixing trig + hyperbolic
$$
\frac{1}{\sqrt{1 + x^2}} \neq \text{arcsin}
$$

Correct:
$$
= \sinh^{-1} x
$$

---

## Trap 2: Forgetting domain restrictions

$$
\cosh^{-1} x \quad \text{requires} \quad x \ge 1
$$

$$
\tanh^{-1} x \quad \text{requires} \quad -1 < x < 1
$$

---

## Trap 3: Missing simplification opportunity

$$
\frac{e^x - e^{-x}}{2}
$$

Don’t leave it like this → write:
$$
\sinh x
$$

---

# 6. QUICK MENTAL FLOW (USE THIS DURING PROBLEMS)

1. Do I see exponentials like $e^x$ and $e^{-x}$?
   → rewrite as $\sinh, \cosh$

2. Do I see $\sqrt{x^2 \pm 1}$?
   → use hyperbolic substitution

3. Do I see $\ln(x + \sqrt{x^2 \pm 1})$?
   → convert to inverse hyperbolic

4. Does derivative look like:
   $$
   \frac{1}{\sqrt{1 + x^2}}
   $$
   → inverse hyperbolic, not trig

---

# 7. BIG PICTURE

Hyperbolic functions are:

- Built from exponentials
- Cleaner than trig for certain integrals
- The “natural language” of expressions involving:
  - $x^2 + 1$
  - $x^2 - 1$
  - exponential symmetry

👉 If trig feels forced, hyperbolic is probably the right tool