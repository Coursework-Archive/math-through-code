# LIMIT RECOGNITION CHEAT SHEET


## DECISION TREE

Before doing ANY work, ask:

---

### Step 1: direct substitution?
### Step 2: indeterminate form? $0/0$ or $\infty/\infty$, or none
    0/0 → indeterminate → must simplify  
    0/nonzero → answer is 0  
    nonzero/0 → ±∞ or DNE
### Step 3: method?
    method → factor (difference of squares)
    method → conjugate
    method → combine fractions
    method → derivative definition
      - $(e^{kt} - 1)/t$ → Answer = $k$  
      - $\frac{f(a+h) - f(a)}{h}$ → Derivative  
      - Square roots → Conjugate  
      - Polynomial ratio at infinity → Leading terms
### Step 4: simplify or substitute



## Vertical Asymptote

**Pattern:**
- Denominator $\to 0$  
- No cancellation  

👉 Limit = **DNE (diverges to $\pm \infty$)**  

---

## Infinity Limits (Leading Terms)

DECISION RULE: LIMITS AT INFINITY

1. Identify the structure:
   - Polynomial / rational → go to step 2
   - Square root / radical → factor highest power inside root
   - Mixed (logs, exponentials) → use dominant growth rates

2. Ask: Is dominant behavior obvious?
   - YES → use leading-term shortcut
   - NO → divide numerator and denominator by highest power

3. Apply rules:
   - top degree < bottom → 0
   - top degree = bottom → ratio of leading coefficients
   - top degree > bottom → ±∞ (check sign)

4. For square roots:
   - sqrt(ax^2 + ...) ≈ x√a (as x → ∞)

Always decide method BEFORE doing algebra

### Recognition Note: Sign Behavior at Infinity

When evaluating limits as x → ±∞:

- Focus on the leading term
- Determine sign using power type:

#### Even Powers (x², x⁴, x⁶, ...)
- Always positive → ignore direction of x
- Only the coefficient determines the sign

- Example:
  - x² → +∞ (both x → ∞ and x → −∞)
  - −2x² → −∞ (both x → ∞ and x → −∞)


#### Odd Powers (x³, x⁵, x⁷, ...)
- Follow the sign of x
- Then apply the leading coefficient (this may flip the sign)

- Example:
  - x³ → +∞ as x → ∞
  - x³ → −∞ as x → −∞
  - −2x³ → −∞ as x → ∞
  - −2x³ → +∞ as x → −∞

#### Key Rule:
Leading term controls BOTH magnitude and sign of the limit


---

## Special Exponential Limit

$\lim_{t \to 0} \frac{e^{kt} - 1}{t} = k$

👉 Instant answer = $k$

---

## Derivative Definition

**Pattern:**
$\frac{f(a+h) - f(a)}{h}$

👉 This equals $f'(a)$  

---

### Example:
$\frac{(2+h)^5 - 32}{h} \rightarrow f(x)=x^5$

👉 $f'(x)=5x^4$  
👉 Answer = $80$

---

## Conjugate Trick (Roots)

**Pattern:**
$\sqrt{x} - \sqrt{a}$

👉 Multiply by conjugate  

Example: Conjugate (Square Roots)

**Problem:**
$\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4}$

Recognize pattern

$\sqrt{x} - \sqrt{a}$ → multiply by conjugate

$\frac{\sqrt{x} - 2}{x - 4} \cdot \frac{\sqrt{x} + 2}{\sqrt{x} + 2}$

Simplify

$\frac{x - 4}{(x - 4)(\sqrt{x} + 2)} = \frac{1}{\sqrt{x} + 2}$

Plug in

$\frac{1}{\sqrt{4} + 2} = \frac{1}{4}$

**Final Answer:**
$\boxed{\frac{1}{4}}$

---
