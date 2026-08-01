# Riemann Sum Recognition Checklist

1. A limit combined with sigma notation usually represents a **Riemann sum**.
2. The factor outside the sum often represents $\Delta x$.
3. The repeated expression containing $i$ often represents the sample point $x_i$.
4. Rewrite the repeated expression as $f(x_i)$.
5. Recover the interval using

```math
\Delta x=\frac{b-a}{n}.
```

A standard Riemann sum has the form

```math
\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i^*)\,\Delta x
=\int_a^b f(x)\,dx.
```
