
<!-- [![DOI](https://zenodo.org/badge/DOI/... .svg)](https://doi.org/...) -->

# Source code and data for 
The impact of two-dimensional filtering on white noise spectra in SWOT along-track observations. Submitted

# Abstract
The Surface Water and Ocean Topography (SWOT) mission provides two-dimensional observations of sea surface height (SSH) at unprecedented spatial resolution, enabling exploration of ocean variability down to scales of $O(10~\mathrm{ km})$. At these scales, however, interpreting SSH variability is challenging because ocean dynamical signals overlap with measurement noise, and their respective spectral signatures are not yet fully understood.
Recent analyses of SWOT 2-km posting observations have shown that along-track spectra are red, with a power-law-like behavior at small scales and spectral slopes around or steeper than $-1$, with their magnitudes and slopes correlated with SWOT measurement noise. 
Here, we investigate the hypothesis that the red along-track spectra can arise from two-dimensional filtering and aliasing of spatially uncorrelated (white) noise. Using synthetic experiments, we show that the resulting one-dimensional along-track spectra exhibit red, power-law-like behavior at small scales, consistent with observations. 
The apparent spectral slope depends on the noise level, its cross-track variability, and the background ocean signal. 
This finding highlights the importance of carefully accounting for measurement noise and processing effects when interpreting SWOT spectra, and suggests that such a noise model should serve as a baseline null hypothesis for small-scale spectral analyses.

# Authors
* 

# Data

# Funding
RSD, LL, MH, and ABVB are supported by NASA award 80NSSC24K1647 through the SWOT Science Team. ABVB received additional support from the ONR MURI program (Grant N00014-24-1-2554). LL received support from NASA award 80NSSC23K0985. 

# How to use this repository
All figures in the manuscript can be reproduced using the Python scripts from this repository. To do so, follow these steps

1. Make a local copy of this repository by either cloning or downloading it.

Your directory tree should look like this:

```
SWOT_noise_1D2D/
├── ***.ipynb
├── data/
├── figs/
├── src/
└── pixi.toml
```
2. If you would like to reproduce the figures from the manuscript using this repository, we recommend that you install [Pixi](https://pixi.sh/latest/). You can then run:

```
$ pixi shell
```
from the project root. This will build the dependencies and activate the Python environment for this project. You can then launch Jupyter Lab as you would normally. In VSCode, the Pixi-managed Python environment will appear in the list of kernels to choose from.

If you follow the steps above, you should be able to reproduce all figures by running the notebooks from the notebooks directory without having to adjust any paths.

# How to cite this code
DOI coming soon.
