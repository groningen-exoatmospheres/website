---
title: People
date: 2022-10-24
type: landing

# Team page. People come from content/authors/<id>/_index.md, selected by their
# `user_groups`. Current team: PI first, then alphabetical by last name.
sections:
  - block: exo-page-head
    content:
      eyebrow: Team
      title: Meet the team
      text: Astronomers, research software engineers and students working together on exoplanet atmospheres, in Groningen and with partners across Europe.
      photo: group.jpg                 # file in this folder (content/people/)
      photo_caption: The ExoAIM group on the ice in Groningen.
      photo_focus: "50% 62%"           # which part of the photo to keep when cropped
  - block: exo-team
    content:
      groups:
        - {title: Members, user_groups: [Members], pin_first: admin}
        # to list someone here, give them `user_groups: [Guest and Visiting Researchers]`
        # or `[Honorary Members]` in content/authors/<id>/_index.md
        - {title: Guests & honorary members, user_groups: [Guest and Visiting Researchers, Honorary Members]}
        - {title: Former members, user_groups: [Former Members], style: compact}
---
