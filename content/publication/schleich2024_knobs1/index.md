---
title: "Knobs and dials of retrieving JWST transmission spectra: I. The importance of p–T profile complexity"
authors:
- schleich
- Sudeshna Boro Saikia
- admin
- Manuel Güdel
- Aiko Voigt
- Ingo Waldmann
#author_notes:
#- "Equal contribution"
#- "Equal contribution"
date: "2024-10-01T00:00:00Z"
doi: "10.1051/0004-6361/202451845"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-10-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "A&A 690, A336"
publication_short: ""

abstract: Context. When retrieving exoplanet atmospheric characteristics from spectroscopic observations, parameter estimation results strongly depend on the chosen forward model. In the era of the James Webb Space Telescope (JWST) and other next-generation facilities, the increased signal-to-noise ratio (S/N), wavelength coverage, and spectral resolution of observations warrant closer investigations into factors that could inadvertently bias the results of these retrievals. Aims. We aim to investigate the impact of utilising multi-point pressure–temperature (p–T) profiles of varying complexity on the retrieval of synthetically generated hot-Jupiter transmission spectra modelled after state-of-the-art observations of the hot Jupiter WASP-39 b with JWST. Methods. We performed homogenised atmospheric retrievals with the TauREx retrieval framework on a sample of synthetically generated transmission spectra, accounting for varying cases of underlying p–T profiles, cloud-top pressures, and expected noise levels. These retrievals are performed using a fixed-pressure multi-point p–T prescription with increasing complexity, ranging from isothermal to an eleven-point profile. We evaluated the performance of the retrievals based on the Bayesian model evidence, and the accuracy of the retrievals was compared to the known input parameters. Results. We find that performing atmospheric retrievals using an isothermal prescription for the pressure–temperature profile consistently results in wrongly retrieved atmospheric parameters when compared to the known input parameters. For an underlying p–T profile with a fully positive lapse rate, we find that a two-point profile is sufficient to retrieve the known atmospheric parameters, while under the presence of an atmospheric temperature inversion, we find that a more complex profile is necessary. Conclusions. Our investigation shows that, for a data quality scenario mirroring state-of-the-art observations of a hot Jupiter with JWST, an isothermal p–T prescription is insufficient to correctly retrieve the known atmospheric parameters. We find a model complexity preference dependent on the underlying pressure–temperature structure, but we argue that a p–T prescription on the complexity level of a four-point profile should be preferred. This represents the overlap between the lowest number of free parameters and the highest model preference in the cases investigated in this work.

# Summary. An optional shortened abstract.
summary: The study investigates the impact of utilising multi-point pressure–temperature (p–T) profiles in atmospheric retrievals.


### TAGS TO USE: 
# JWST, HST, CHEOPS, PLATO, HWO, Ariel
# Transit, Eclipse, Phase-curve, Direct Imaging, 
# Gaseous Planets, Rocky Planets, Sub-Neptunes,
# Data Reduction, Modeling, Atmospheric Retrievals, Ideas
tags:
- JWST
- Transit
- Gaseous Planets
- Atmospheric Retrievals
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'https://arxiv.org/pdf/2409.09127'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Impact of the number of T-p nodes in atmospheric retrievals -- Image credit: S. Schleich'
  focal_point: "Center"
  placement: 2
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---
