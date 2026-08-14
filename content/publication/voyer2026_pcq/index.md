---
title: "Pre-computed aerosol extinction, scattering and asymmetry grids for scalable atmospheric retrievals"
authors:
- voyer
- admin
#author_notes:
#- "Equal contribution"
#- "Equal contribution"
date: "2026-01-10T00:00:00Z"
doi: "10.1051/0004-6361/202558469"

# Schedule page publish date (NOT publication's date).
publishDate: "2025-03-25T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "A&A 707 A127"
publication_short: ""

abstract: The unprecedented wavelength coverage and sensitivity of the James Webb Space Telescope (JWST) permits to measure the absorption features of a wide range of condensate species from Silicates to Titan tholins. Atmospheric retrievals are uniquely suited to analyse these datasets and characterize the aerosols present in exoplanet atmospheres. However, including the optical properties of condensed particles within retrieval frameworks remains computationally expensive, limiting our ability to fully exploit JWST observations. In this work, we improve the computational efficiency and scaling behavior of aerosol models in atmospheric retrievals, enabling in-depth studies including multiple condensate species within practical time scales. Rather than computing the aerosol Mie coefficients for each sampled model, we pre-compute extinction efficiency (Qext), scattering efficiency (Qscat) and asymmetry parameter (g) grids for seven condensate species relevant in exoplanet atmospheres (Mg2SiO4 amorph sol - gel, MgSiO3 amorph glass, MgSiO3 amorph sol - gel, SiO2 alpha, SiO2 amorph, SiO and Titan tholins). The pre-computed Qext grids significantly reduce computation time between 1.4 and 17 times with negligible differences on the retrieved parameters. They also scale effortlessly with the number of aerosol species while maintaining the accuracy of cloud models. Thereby enabling more complex retrievals as well as broader population studies without increasing the overall error budget. The Qext, Qscat and g grids are freely available on Zenodo as well as a public TauREx plugin -TauREx-PCQ- that utilize them.

# Summary. An optional shortened abstract.
summary: The paper introduces a precomputed grid of aerosol extinction coefficients, and a new module for retrieving clouds in the JWST era.

### TAGS TO USE: 
# JWST, HST, CHEOPS, PLATO, HWO, Ariel
# Transit, Eclipse, Phase-curve, Direct Imaging, 
# Gaseous Planets, Rocky Planets, Sub-Neptunes,
# Data Reduction, Modeling, Atmospheric Retrievals, Ideas
tags:
- JWST
- Gaseous Planets
- Sub-Neptunes
- Atmospheric Retrievals
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'https://arxiv.org/pdf/2607.13793'
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
  caption: 'Synthetic JWST exoplanet spectra with clouds -- Image credit: M. Voyer'
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
