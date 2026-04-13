import numpy as np
from scipy.special import kv, gamma

def matern_spectral_density_2d(kappa, nu, l=0.1, sigma2=1.0):
    """
    Evaluate the isotropic 2D Matérn spectral power density.


    This matches the standard Matérn PSD formula for n=2:
    S(kappa) = sigma2 * 4 * pi * Gamma(nu + 1) * (2 * nu)**nu /
               (Gamma(nu) * l**(2 * nu)) *
               ((2 * nu) / l**2 + (2 * pi * kappa)**2)**(-(nu + 1))

    Parameters:
    - kappa : array-like, radial wavenumbers in cycles per unit distance
    - nu : smoothness parameter (nu > 0). At large kappa, the 2D Matérn PSD
           scales as S(kappa) ~ kappa^(-(2 * nu + 2)), so the asymptotic
           spectral slope is -(2 * nu + 2).
    - l : scale parameter (l > 0)
    - sigma2 : variance parameter

    Returns:
    - S(kappa) : 2D spectral density at radial wavenumbers kappa
    """

    kappa = np.asarray(kappa)
    prefactor = sigma2 * 4 * np.pi * gamma(nu + 1) * (2 * nu) ** nu / (gamma(nu) * l ** (2 * nu))
    denominator = ((2 * nu) / l ** 2 + (2 * np.pi * kappa) ** 2) ** (nu + 1)
    return prefactor / denominator