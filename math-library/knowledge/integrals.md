1. Simplify the integrand if possible
    - Expand powers if necessary.
    - Rewrite radicals as fractional exponents.
    - Factor constants out.

2. Look for a basic antiderivative

Ask:

- Is it a polynomial?

$$
\int x^n\,dx
$$

- Is it exponential?

$$
\int e^x\,dx
$$

$$
\int a^x\,dx
$$

- Is it logarithmic?

$$
\int \frac{1}{x}\,dx
$$

- Is it trigonometric?

$$
\int \sin x\,dx
$$

$$
\int \cos x\,dx
$$

$$
\int \sec^2 x\,dx
$$

3. Look for a composition (inside function)

Example:

$$
\int \frac{2z}{z^2+1}\,dz
$$

Choose

$$
u=z^2+1
$$

Then

$$
du=2z\,dz
$$

so the integral becomes

$$
\int \frac{1}{u}\,du
=\ln|u|+C
$$

Substitute back:

$$
\boxed{\ln(z^2+1)+C}
$$

Because $z^2+1>0$ for every real $z$, the absolute value is optional in the final expression.
