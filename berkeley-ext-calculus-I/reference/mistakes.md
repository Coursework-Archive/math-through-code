### Mistake: Overextending the domain of square root functions

I initially wrote domains using unions with infinity for functions involving square roots. For square root expressions, the domain is restricted to where the radicand is greater than or equal to zero, which usually results in a finite interval.

**Correction:**  
Solve the inequality inside the square root first, then write the domain directly from that solution. Do not include values outside the interval.

**Example:**  
For y = 2 + √(4 − x²), the domain is [-2, 2], not a union involving infinity.


### Interval notation for decreasing functions (endpoint inclusion)

**Mistake:**  
I excluded an endpoint when stating where a function is decreasing, even though the function is defined at that endpoint and the decreasing behavior holds up to it.

**Example:**  
In 1.1.4(f), I initially did not include \(0\) when stating where \(g(x)\) is decreasing.

**Correction / Rule:**  
When stating that a function is increasing or decreasing on an interval:
- Use **brackets** if the function is defined at the endpoint and the behavior holds up to that point.
- Use **parentheses** only if the function is not defined at the endpoint or the behavior does not apply there.

**Correct statement:**  
\[
g(x)\ \text{is decreasing on}\ [-4,0]
\]


### Graph interval errors due to endpoint misreading

**Mistake:**  
Incorrect interval endpoints were chosen by extending the graph beyond its actual drawn domain or by reusing endpoints from a previous part of the problem.

**Correction / Rule:**  
When reading intervals from a graph:
- Identify the actual left and right endpoints shown.
- Re-evaluate the graph fresh for each question.
- Do not assume intervals carry over between parts.

**Example:**  
In 1.1.4, the graph ends at x = 3, not 4, so intervals must stop at 3 even if the curve appears to continue.


### Even vs odd functions (symmetry must be exact)

**Mistake:**  
I classified a function as even or odd based on how the graph looked, rather than checking whether it satisfied the formal symmetry definitions.

**Example:**  
In 1.1.78, the graph was neither symmetric about the y-axis nor symmetric about the origin, so the function is neither even nor odd.

**Correction / Rule:**  
To classify a function:
- **Even:** graph must be symmetric about the y-axis \((f(-x) = f(x))\)
- **Odd:** graph must be symmetric about the origin \((f(-x) = -f(x))\)
- If neither symmetry holds exactly, the function is **neither even nor odd**.

**Reminder:**  
Partial or visual symmetry is not sufficient — the symmetry must hold for the entire graph.


### Mistake: Extending a Square Root Graph Outside Its Domain

**Problem Type:** Graphing transformed square root functions  
**Example:** \( y = -\sqrt{x} - 1 \)

**Mistake:**  
I correctly identified the transformation (reflection over the x-axis and a downward shift), but I incorrectly extended the graph to the left of the y-axis. This added points for \( x < 0 \), where the function is not defined.

**Why This Is Incorrect:**  
The square root function \( \sqrt{x} \) is defined only for \( x \ge 0 \).  
Transformations *outside* the square root (such as a leading minus sign or vertical shifts) do **not** change the domain.

**Correct Reasoning:**  
- The expression **inside** the square root determines the domain.
- Since the radicand is \( x \), the domain remains \( x \ge 0 \).
- The graph must start at the endpoint \( (0,-1) \) and extend **only to the right**.

**Correction:**  
The correct graph begins at \( (0,-1) \) and decreases to the right, with **no portion of the graph for \( x < 0 \)**.

**Lesson Learned:**  
> Minus signs outside the square root affect vertical orientation only.  
> To reflect left/right, the negation must be **inside** the square root.


### Composition: placing constants inside vs outside a function

**Mistake:**  
When decomposing a function into a composition, I grouped terms incorrectly (e.g., put “+1” inside the inner function), which changed the original expression.

**Example:**  
\(\cos(\sqrt{\tan t}+1)\) is not the same as \(\cos(\sqrt{\tan t+1})\).  
The “+1” must be applied **after** the square root, not inside it.

**Correction / Rule:**  
When building \(f(g(h(t)))\), match the original parentheses exactly:
- Identify the *outermost* operation first.
- Then work inward, keeping additions inside/outside radicals exactly as written.


### Mistake: Confusing Reflections in Square Root Transformations

**Mistake:**  
I treated `-√x`, `√(-x)`, and `-√x - 1` as if they produced the same type of reflection.  
In particular, I incorrectly reflected `-√x` across the **y-axis**, when it should be a reflection across the **x-axis**.

**Correction:**  
- `√x` starts at `(0, 0)` and increases to the right  
- `-√x` reflects `√x` **over the x-axis** (values become negative, domain unchanged)  
- `√(-x)` reflects `√x` **over the y-axis** (domain becomes `x ≤ 0`)  
- Vertical shifts (e.g. `-√x - 1`) move the graph **after** reflections, not before

**Key Check Before Graphing:**  
1. Identify whether the negative sign is **inside** or **outside** the function  
2. Decide reflection direction (x-axis vs y-axis)  
3. Apply vertical shifts last

**Lesson:**  
Always separate *reflection*, *domain change*, and *vertical shift* into distinct steps instead of combining them mentally.
