# Filter-Estimation
Contains code which estimates the impulse response of a filter for input White noise. The response **h** = **inverse(Rxx) * Ryx**.
Since X is White, **Rxx** is Toeplitz. A linear system involving a Toeplitz Matrix can be solved faster using the Levinson Algorithm which has O(n^2) complexity as compared to Gauss-Jordan which has O(n^3) complexity. The MATLAB code uses the function *inv*. The python code implements the Levinson algorithm.

Attached is a figure of the results. 'o' is actual. 'x' is the estimate.
