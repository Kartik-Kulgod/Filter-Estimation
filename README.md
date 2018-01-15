# Filter-Estimation
The following MATLAB code estimates the impulse response of a FIR Filter.
The filter is assumed to be sinc(x)
**x** is white
**y** is the output
**Rxx** is the auto correlation Toeplitz Matrix
**Ryx** is the cross correlation matrix
**h** is the filter data
**hest** is the estimated filter data

It can be shown that **Rxx h** = **r**, implying that **h** = **inv(R)r**
Since **x** is white, **Rxx** is Toeplitz.
Also both **x** and **y** are ergodic processes.
