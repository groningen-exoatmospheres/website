---
title: "FRECKLL: Full and Reduced Exoplanet Chemical Kinetics DistiLLed"
authors:
- Ahmed F. Al-Refaie
- Olivia Venot
- admin
- Billy Edwards
#author_notes:
#- "Equal contribution"
#- "Equal contribution"
date: "2024-06-01T00:00:00Z"
doi: "10.3847/1538-4357/ad3dee"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-06-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "ApJ 967 132"
publication_short: ""

abstract: 'We introduce a new Python 1D chemical kinetic code, Full and Reduced Exoplanet Chemical Kinetics distiLLed (FRECKLL), to evolve large chemical networks efficiently. FRECKLL employs "distillation" in computing the reaction rates, which minimizes the error bounds to the minimum allowed by double precision values (ϵ ≤ 10−15). Compared to summation of rates with traditional algorithms like pairwise summation, distillation provides a tenfold reduction in solver time for both full and reduced networks. Both the full and reduced Venot2020 networks are packaged in FRECKLL as well as a TAUREX 3.1 plug-in for usage in forward modeling and retrievals of exoplanet atmospheres. We present TAUREX retrievals performed on a simulated HD 189733b JWST spectra using the full and reduced Venot2020 chemical networks and demonstrate the viability of total disequilibrium chemistry retrievals and the ability for JWST to detect disequilibrium processes.'

# Summary. An optional shortened abstract.
# AUTO-GENERATED (first sentence of the abstract) -- please rewrite.
summary: 'We introduce a new Python 1D chemical kinetic code, Full and Reduced Exoplanet Chemical Kinetics distiLLed (FRECKLL), to evolve large chemical networks efficiently.'


### TAGS TO USE:
# JWST, HST, CHEOPS, PLATO, HWO, Ariel
# Transit, Eclipse, Phase-curve, Direct Imaging,
# Gaseous Planets, Rocky Planets, Sub-Neptunes,
# Data Reduction, Modeling, Atmospheric Retrievals, Ideas
# AUTO-GENERATED from keywords -- please check.
tags:
- JWST
- Modeling
- Atmospheric Retrievals
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'https://arxiv.org/pdf/2209.11203'
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
  caption: 'Chemical abundances for a benchmark HD 209458 b atmosphere using temperature and vertical mixing profiles as well as… -- Image credit: A. Al-Refaie'
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
