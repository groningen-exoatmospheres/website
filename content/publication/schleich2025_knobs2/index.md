---
title: "Knobs and dials of retrieving JWST transmission spectra. II. Impacts of pipeline-level differences on retrieval posteriors"
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
date: "2025-11-05T00:00:00Z"
doi: "10.48550/arXiv.2511.05652"

# Schedule page publish date (NOT publication's date).
publishDate: "2025-11-05T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "A&A (Accepted)"
publication_short: ""

abstract: Since the launch of JWST, observations of exoplanetary atmospheres have seen a revolution in data quality. Given that atmospheric parameter inferences depend heavily on the underlying data, a re-evaluation of current methodologies is warranted to assess the reliability of these results. We investigate the impact of variations in input spectra on atmospheric retrievals for the hot Jupiter WASP-39 b using JWST transit data. Specifically, we analyse the reliability of parameter estimations from random perturbations of the underlying spectrum and their sensitivity to three transmission spectra derived from the same observational data. Using the NIRSpec PRISM observation from a single transit of WASP-39 b, we perform retrievals with the TauREx framework. As a baseline, we use a spectrum derived with the Eureka! data reduction pipeline. To evaluate retrieval reliability, we analyse posterior distributions under deviations from this spectrum. We simulate random noise by performing retrievals on scattered instances of this spectrum and compare them with retrievals based on existing spectra reduced from the same raw observation. Our analysis identifies three types of posterior distributions. (1) Stable, Gaussian distributions for species constrained across the entire spectrum (e.g., H2O, CO2); (2) Uniform posteriors with upper bounds for weakly constrained species (e.g., CO, CH4); and (3) Unstable, heavy-tailed posteriors for species constrained by minor spectrum features (e.g., SO2, C2H2). We find that other parameters, such as the planetary radius and p-T profile, are stable under spectral perturbations. Posterior distributions differ for retrievals on independently reduced transmission spectra from the same raw data, complicating interpretation, particularly for skewed distributions. Based on this, we advocate for careful assessment and selection of credible interval sizes to reflect this.

# Summary. An optional shortened abstract.
summary: The study investigates the impacts of pipeline-level differences on retrieval posteriors using three different Eureka! data reductions of the WASP-39b PRISM observations.


### TAGS TO USE: 
# JWST, HST, CHEOPS, PLATO, HWO, Ariel
# Transit, Eclipse, Phase-curve, Direct Imaging, 
# Gaseous Planets, Rocky Planets, Sub-Neptunes,
# Data Reduction, Modeling, Atmospheric Retrievals, Ideas
tags:
- JWST
- Transit
- Gaseous Planets
- Data Reduction
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'https://arxiv.org/pdf/2511.05652'
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
  caption: 'Retrieved atmospheric properties of WASP-39b -- Image credit: S. Schleich'
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
