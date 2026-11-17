---
title: "To Sample or Not to Sample: Retrieving Exoplanetary Spectra with Variational Inference and Normalizing Flows"
authors:
- Kai Hou Yip
- admin
- Ahmed F. Al-Refaie
- Ingo P. Waldmann
#author_notes:
#- "Equal contribution"
#- "Equal contribution"
date: "2024-01-01T00:00:00Z"
doi: "10.3847/1538-4357/ad063f"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-01-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "ApJ 961 30"
publication_short: ""

abstract: 'Current endeavours in exoplanet characterization rely on atmospheric retrieval to quantify crucial physical properties of remote exoplanets from observations. However, the scalability and efficiency of said technique are under strain with increasing spectroscopic resolution and forward model complexity. The situation has become more acute with the recent launch of the James Webb Space Telescope and other upcoming missions. Recent advances in machine learning provide optimization-based variational inference as an alternative approach to perform approximate Bayesian posterior inference. In this investigation we developed a normalizing-flow-based neural network, combined with our newly developed differentiable forward model, Diff-τ, to perform Bayesian inference in the context of atmospheric retrievals. Using examples from real and simulated spectroscopic data, we demonstrate the advantages of our proposed framework: (1) training our neural network does not require a large precomputed training set and can be trained with only a single observation; (2) it produces high-fidelity posterior distributions in excellent agreement with sampling-based retrievals; (3) it requires up to 75% fewer forward model calls to converge to the same result; and (4) this approach allows formal Bayesian model selection. We discuss the computational efficiencies of Diff-τ in relation to TauREx3''s nominal forward model and provide a "lessons learned" account of developing radiative transfer models in differentiable languages. Our proposed framework contributes toward the latest development of neural network-powered atmospheric retrieval. Its flexibility and significant reduction in forward model calls required for convergence holds the potential to be an important addition to the retrieval tool box for large and complex data sets along with sampling-based approaches.'

# Summary. An optional shortened abstract.
# AUTO-GENERATED (first sentence of the abstract) -- please rewrite.
summary: 'Current endeavours in exoplanet characterization rely on atmospheric retrieval to quantify crucial physical properties of remote exoplanets from observations.'


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
url_pdf: ''
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
  caption: ''
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
