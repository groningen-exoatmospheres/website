---
# Leave the homepage title empty to use the site title
title:
date: 2025-10-21
type: landing

sections:
  - block: slider
    content:
      slides:
      - title: ExoAIM Lab
        content: Exo-Atmospheric Interpretation and Modeling Lab
        align: center
        background:
          image:
            filename: ESA_WASP-121_b_artist.jpg
            filters:
              brightness: 0.9
          position: right
          color: '#666'
      - title: Meet our team!
        #content: 'See who is working at ExoAIM Groningen'
        align: left
        background:
          image:
            filename: ESA_Hubble_population.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#555'
        link:
          icon: circle-user
          icon_pack: fas
          text: People
          url: ../people/
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: ''
      is_fullscreen: true
      # Automatically transition through slides?
      loop: false
      # Duration of transition between slides (in ms)
      interval: 2000
---
