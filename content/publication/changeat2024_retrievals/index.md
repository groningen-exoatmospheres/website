---
title: "Toward Atmospheric Retrievals of Panchromatic Light Curves: EXPLOR-ing Generalized Inversion Techniques for Transiting Exoplanets with JWST and Ariel"
authors:
- admin
- Yuichi Ito
- Ahmed F. Al-Refaie
- Kai Hou Yip
- Theresa Lueftinger
#author_notes:
#- "Equal contribution"
#- "Equal contribution"
date: "2024-05-01T00:00:00Z"
doi: "10.3847/1538-3881/ad3032"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-05-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "AJ 167 195"
publication_short: ""

abstract: 'Conventional atmospheric retrieval codes are designed to extract information, such as chemical abundances, thermal structures, and cloud properties, from fully "reduced" spectra obtained during transit or eclipse. Reduced spectra, however, are assembled by fitting a series of simplified light curves to time-series observations, wavelength by wavelength. Thus, spectra are postprocessed summary statistics of the original data, which by definition do not encode all the available information (i.e., astrophysical signal, model covariance, and instrumental noise). Here, we explore an alternative inversion strategy where the atmospheric retrieval is performed on the light curve directly, i.e., closer to the data. This method is implemented in EXoplanet Panchromatic Light curve Observation and Retrieval (EXPLOR), a novel atmospheric retrieval code inheriting from the TAUREX project. By explicitly considering time in the model, EXPLOR naturally handles transits, eclipses, phase curves, and other complex geometries for transiting exoplanets. In this paper, we have validated this new technique by inverting simulated panchromatic light curves. The model was tested on realistic simulations of a WASP-43 b-like exoplanet as observed with the James Webb Space Telescope (JWST) and Ariel telescope. By comparing our panchromatic light-curve approach against conventional spectral retrievals on mock scenarios, we have identified key breaking points in information and noise propagation when employing past literature techniques. Throughout the paper, we discuss the importance of developing "closer-to-data" approaches such as the method presented in this work, and highlight the inevitable increase in model complexity and computing requirements associated with the recent JWST revolution.'

# Summary. An optional shortened abstract.
# AUTO-GENERATED (first sentence of the abstract) -- please rewrite.
summary: 'Conventional atmospheric retrieval codes are designed to extract information, such as chemical abundances, thermal structures, and cloud properties, from fully "reduced" spectra obtained during transit or eclipse.'


### TAGS TO USE:
# JWST, HST, CHEOPS, PLATO, HWO, Ariel
# Transit, Eclipse, Phase-curve, Direct Imaging,
# Gaseous Planets, Rocky Planets, Sub-Neptunes,
# Data Reduction, Modeling, Atmospheric Retrievals, Ideas
# AUTO-GENERATED from keywords -- please check.
tags:
- JWST
- Ariel
- Transit
- Eclipse
- Phase-curve
- Modeling
- Atmospheric Retrievals
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'https://arxiv.org/pdf/2403.02244'
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
  caption: 'Figure from the paper -- Image credit: Q. Changeat'
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
