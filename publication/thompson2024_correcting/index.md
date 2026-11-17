---
title: "Correcting Exoplanet Transmission Spectra for Stellar Activity with an Optimized Retrieval Framework"
authors:
- Alexandra Thompson
- Alfredo Biagini
- Gianluca Cracchiolo
- Antonino Petralia
- admin
- et al.
#author_notes:
#- "Equal contribution"
#- "Equal contribution"
date: "2024-01-01T00:00:00Z"
doi: "10.3847/1538-4357/ad0369"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-01-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "ApJ 960 107"
publication_short: ""

abstract: 'The chromatic contamination that arises from photospheric heterogeneities, e.g., spots and faculae on the host star presents a significant noise source for exoplanet transmission spectra. If this contamination is not corrected for, it can introduce substantial bias in our analysis of the planetary atmosphere. We utilize two stellar models of differing complexity, StARPA (Stellar Activity Removal for Planetary Atmospheres) and ASteRA (Active Stellar Retrieval Algorithm), to explore the biases introduced by stellar contamination in retrieval under differing degrees of stellar activity. We use the retrieval framework TauREx3 and a grid of 27 synthetic, spot-contaminated transmission spectra to investigate potential biases and to determine how complex our stellar models must be in order to accurately extract the planetary parameters from transmission spectra. The input observation is generated using the more complex model (StARPA), in which the spot latitude is an additional, fixable parameter. This observation is then fed into a combined stellar-planetary retrieval, which contains a simplified stellar model (ASteRA). Our results confirm that the inclusion of stellar activity parameters in retrieval minimizes bias under all activity regimes considered. ASteRA performs very well under low-to-moderate activity conditions, retrieving the planetary parameters with a high degree of accuracy. For the most active cases, characterized by larger, higher-temperature contrast spots, some minor residual bias remains due to ASteRA neglecting the interplay between the spot and the limb-darkening effect. As a result of this, we find larger errors in retrieved planetary parameters for central spots (0°) and those found close to the limb (60°) than those at intermediate latitudes (30°).'

# Summary. An optional shortened abstract.
# AUTO-GENERATED (first sentence of the abstract) -- please rewrite.
summary: 'The chromatic contamination that arises from photospheric heterogeneities, e.g., spots and faculae on the host star presents a significant noise source for exoplanet transmission spectra.'


### TAGS TO USE:
# JWST, HST, CHEOPS, PLATO, HWO, Ariel
# Transit, Eclipse, Phase-curve, Direct Imaging,
# Gaseous Planets, Rocky Planets, Sub-Neptunes,
# Data Reduction, Modeling, Atmospheric Retrievals, Ideas
# AUTO-GENERATED from keywords -- please check.
tags:
- Transit
- Atmospheric Retrievals
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'https://arxiv.org/pdf/2302.04574'
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
  caption: 'Figure from the paper -- Image credit: A. Thompson'
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
