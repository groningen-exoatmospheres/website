---
# Homepage. Each entry under `sections` is one block; the exo-* blocks live in
# layouts/partials/blocks/. Edit text here; order = order on the page.
title:
date: 2025-10-21
type: landing

sections:
  - block: exo-hero
    content:
      kicker: Kapteyn Astronomical Institute · University of Groningen
      title: Decoding the <span class="grad">atmospheres</span> of distant planets
      text: We read the light of exoplanets observed with JWST, Hubble and soon ESA's Ariel, and build the models and scientific codes to interpret it.
      image: ESA_WASP-121_b_artist.jpg
      primary: {label: Our research, url: research/}
      secondary: {label: Publications, url: publication/}
      stats:
        - {value: "auto:publications", label: publications}
        - {value: "auto:team", label: team members}
        - {value: "auto:codes", label: scientific codes}   # = number of items under "Software we build"
    design:
      style: photo        # photo | minimal (starfield, no image)

  - block: exo-research
    content:
      title: What we study
      more: {label: All topics, url: research/}
    design:
      style: tiles        # tiles | cards

  - block: exo-updates
    content:
      news:   {title: Latest news, count: 3, more: {label: All news, url: post/}}
      papers: {title: Selected papers, count: 3, more: {label: All publications, url: publication/}}
      # papers shown = publications with `featured: true` in their front matter

  - block: exo-software
    content:
      title: Software we build
      more: {label: On GitHub, url: "https://github.com/groningen-exoatmospheres"}
      items:
        - name: TauREx 3
          icon: layer-group
          short: Bayesian retrieval framework
          text: Fast, modular Bayesian retrieval framework for exoplanet atmospheres. TauREx4 is in development with the Netherlands eScience Center.
          url: https://github.com/ucl-exoplanets/taurex3
          docs: https://taurex.space/
          paper: publication/alrefaie2022_taurex/
        - name: FRECKLL
          icon: flask
          short: Disequilibrium chemistry
          text: Chemical kinetics solver bringing disequilibrium chemistry into retrievals.
          docs: https://ahmed-f-alrefaie.github.io/freckll/
          paper: publication/alrefaie2024_freckll/
        - name: TauREx-PCQ
          icon: cloud
          short: Fast cloud retrievals
          text: Pre-computed aerosol extinction grids for fast cloud retrievals.
          url: https://github.com/groningen-exoatmospheres/taurex-PCQ
          paper: publication/voyer2026_pcq/
        - name: MELTYQ
          icon: volcano
          short: Magma-ocean retrievals
          text: Couples magma-ocean chemistry to spectral retrievals of sub-Neptunes.
          paper: publication/ito2026_meltyq/
        - name: Alfnoor
          icon: satellite
          short: Ariel population retrievals
          text: Simulates and retrieves the atmospheres of Ariel's planet population with TauREx.
          paper: publication/changeat2020_alfnoor/
        - name: ExPLOR
          icon: wave-square
          short: Light-curve retrievals
          text: Retrievals performed directly on panchromatic light curves.
          paper: publication/changeat2024_retrievals/
    design:
      style: compact      # compact | cards

  - block: exo-cta
    content:
      title: Want to work with us?
      text: We welcome BSc, MSc and PhD students, postdocs and collaborators.
      primary: {label: Get in touch, url: contact/}
      partners: [JWST, Hubble, Ariel, ESA, NWO, NOVA, Netherlands eScience Center, SRON, CEA Paris-Saclay]
---
