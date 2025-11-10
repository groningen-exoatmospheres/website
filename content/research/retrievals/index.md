---
title: Atmospheric Retrieval Development
weight: 4
#date: 2020-12-01

image:
  caption: 'Created with ChatGPT'
  focal_point: "Center"
  placement: 2
  preview_only: false

show_author: false
show_social: false
share: false
profile: false
show_date: false
---

<p style="text-align: justify;">
Atmospheric retrievals refer to a set of computational and statistical techniques used to infer the physical and chemical properties of a planet’s atmosphere from observed spectra. We observe exoplanets with powerful spectrographs oboard space and ground-based telescopes to measure their spectra. These spectra encode the properties of the atmosphere, but they are not directly interpretable; they must be inverted (i.e., retrieved) to extract information such as temperature, chemistry, aerosols, and other atmospheric properties. 
</p>

<!--more-->

<p style="text-align: justify;">
In atmospheric retrievals, millions of forward model---predicting what a planet’s spectrum should look like for a given set of atmospheric conditions---are tested to evaluate which sets of the free parameters best match the observed spectrum. At ExoAIM, we test for the effects of molecular absorption, scattering from clouds, and the temperature distributions. We use modern Bayesian statistical frameworks, such as Nested Sampling, to optimize our exploration: the model parameters are iteratively adjusted to find the best-fitting atmospheric state and provides probability distributions (posterior estimates). We have sucessfully applied these techniques on 100s of exoplanets, constraining quantities such as the abundances of water vapor, methane, carbon dioxide, and the planet’s temperature-pressure profile.

In collaboration with UCL and KCL, we are the architects of the open-source project TauREx. TauREx is the most advanced exoplanet atmosphere simulation and retrieval platform. It is trusted by 100s of scientists and it is available for all: [Check out TauREx here](https://taurex.space/). TauREx is used for high-impact research and discoveries. In Groningen, we develop the main core code and maintain a number of plugins allowing advanced modeling and retrievals of exoplanet data.

Atmospheric retrievals are crucial for understanding exo-atmospheres, which in turn can be used to constrain planetary formation, evolution, and potential habitability. By comparing the atmospheric compositions of many exoplanets across different sizes, temperatures, and host star types, we can test models of planet formation and migration. For example, detecting certain molecular ratios like carbon-to-oxygen can reveal where in a protoplanetary disk a planet formed. We utilize retrievals to explore the performances of next-generation observatories such as Ariel and inform their design to answer foundamental questions about the universe.
</p>

Check out our atmospheric retrieval code TauREx v3.2: [Official Website](https://taurex.space/)
