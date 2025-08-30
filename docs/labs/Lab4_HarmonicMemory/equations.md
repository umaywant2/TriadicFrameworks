# Lab 4: Harmonic Memory — Equations

## 1. Harmonic Memory State

Define a memory state encoded in harmonic basis:

$$
|M\rangle = \sum_{n=0}^{\infty} c_n |H_n\rangle
$$

Where \( |H_n\rangle \) are harmonic eigenstates and \( c_n \) are memory coefficients.

## 2. Resonant Recall Operator

Introduce a recall operator \( \hat{R} \) that retrieves harmonic memory:

$$
\hat{R} |M\rangle = \sum_{n=0}^{\infty} c_n \hat{R} |H_n\rangle
$$

Assuming \( \hat{R} |H_n\rangle = r_n |H_n\rangle \), we get:

$$
\hat{R} |M\rangle = \sum_{n=0}^{\infty} r_n c_n |H_n\rangle
$$

## 3. Harmonic Overlap Metric

Define a memory fidelity metric \( \mathcal{F}_H \):

$$
\mathcal{F}_H = |\langle M_{\text{stored}} | M_{\text{retrieved}} \rangle|^2
$$

## 4. Triadic Harmonic Tensor

Construct a triadic tensor \( T_{mnk} \) for harmonic memory propagation:

$$
T_{mnk} = \langle H_m | \hat{R}_n | H_k \rangle
$$

Encodes memory transitions across harmonic modes.
