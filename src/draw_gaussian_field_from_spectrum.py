import numpy as np

def draw_gaussian_field_from_spectrum(spec,repeat_num=1):
    spec_realization = spec.copy()
    spec_realization[0, 0] = 0
    field_hat = np.repeat(np.array([spec_realization**0.5]), repeats=repeat_num, axis=0)
    field_hat = field_hat * (
        np.random.normal(0, 1, field_hat.shape)
        + 1j * np.random.normal(0, 1, field_hat.shape)
    ) / np.sqrt(2)
    field = np.real(np.fft.ifft2(field_hat, norm='forward', axes=(1, 2))) * np.sqrt(2)
    return field_hat, field