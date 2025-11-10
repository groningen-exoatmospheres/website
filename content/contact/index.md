---
title: Contact
date: 2022-10-24

type: landing

sections:
  - block: contact
    content:
      title: Contact
      text: |-
        Whether you are a student, a fellow researcher, or just curious about exoplanet exploration and planetary atmospheres, get in touch with us! Collaboration and curiosity drive our work at the ExoAIM Lab. Please don’t hesitate to reach out if you’d like to learn more about our research, discuss potential partnerships, or engage with our team.
      email: q.changeat@rug.nl
      #phone: 888 888 88 88
      address:
      #Kapteyn Astronomical Institute, Landleven 12, 9747 AD Groningen, The Netherlands
        street: Kapteyn Astronomical Institute, Landleven 12
        city: Groningen
        #region: CA
        postcode: '9747 AD'
        country: The Netherlands
        country_code: NL
      coordinates:
        latitude: '53.24062858985363' 
        longitude: '6.534963208497085'
      #directions: Enter Building 1 and take the stairs to Office 200 on Floor 2
      #office_hours:
      #  - 'Monday 10:00 to 13:00'
      #  - 'Wednesday 09:00 to 10:00'
      #appointment_url: 'https://calendly.com'
      #contact_links:
      #  - icon: comments
      #    icon_pack: fas
      #    name: Discuss on Forum
      #    link: 'https://discourse.gohugo.io'
    
      # Automatically link email and phone or display as text?
      autolink: true
    
      # Email form provider
      form:
        provider: netlify
        formspree:
          id:
        netlify:
          # Enable CAPTCHA challenge to reduce spam?
          captcha: false
    design:
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: contact.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen
---
