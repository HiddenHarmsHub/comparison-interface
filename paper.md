---
title: 'Comparison Interface: A Data Collection Interface for Comparative Judgement Studies'
tags:
  - Python
  - Flask
  - Web Interface
  - Comparative Judgement
  - Data Collection
authors:
  - name: Catherine Smith
    orcid: 0000-0002-2530-9229
    corresponding: true 
    affiliation: 1
  - name: Rowland G. Seymour
    orcid: 0000-0002-8739-3921
    affiliation: 1
  - name: Fabián Hernández
    affiliation: 3
  - name: Bertrand Perrat
    affiliation: 3
affiliations:
 - name: University of Birmingham, United Kingdom
   index: 1
 - name: Independent Software Engineer, United Kingdom
   index: 2
date: TODO
bibliography: paper.bib
---

# Summary

Comparative Judgement is a research technique which asks participants to make pairwise judgements of items based on a given criteria, for example which of two areas has the higher rate of deprivation. These pairwise judgements have been shown to be easier for people to make than alternatives such as making a absolute judgement based on a scale or putting a whole series of items in order based on a criteria. These models are gaining popularity in social sciences but the options for data collection remain limited. This Flask app provides a specialist comparative judgement interface which is domain agnostic and highly configurable in terms of its behaviour and the text presented to the user. This means that the same code can be configured to collect comparative judgement data on different topics using different languages making it applicable to a wide range of research projects. The website complies with WCAG 2.2 level AA and works on smaller screens such as phones and tablets as well as larger screens. It can be configured without any programming knowledge and provides an export into CSV files. The system can be configured in JSON or a combination of JSON and a CSV file and any set of images can be used. Example configurations are provided. 

# Statement of Need

This flask application aims to reduce the barriers for researchers who want to use comparative judgement in their research. Comparative judgements can not be collected through traditional research survey software, for example KoboToolbox, or Jisc's Online Surveys, formerly known as BSOS. We are only aware of two packages that do provide data collection software, both of which are for specific contexts. NoMoreMarking[@Jones2015] provide proprietary but free to use software that is designed for schools and other education providers to run studies about student assessment. The open source python package PsychoPy \citep{Peirce_PsychoPy2_Experiments_in_2019} can be used to run comparative judgement studies for experimental psychology studies.  


This software aims to make comparative judgement studies simpler, more efficient and more attractive to run across a wide range of disciplines.

# Features

Upon visiting the website a user is presented with the list of user registration questions specified in the configuration file, this can optionally include a link to the privacy/research ethics document and a select box to confirm that the user agrees to the policies. If multiple groups are included in the study then the user is also presented with the option to select which group/s they have knowledge of on the registration page. Once registration is completed the user is assigned assigned a unique identifier and a session which will be active until they log out or for the length of time specified in the configuration. No passwords are used in the system. All of the data collected is stored in a SQLite3 database.

The configuration file determines how the pairs of images presented to the user for judging are selected; either each pair can have an equal chance or each pair can be weighted with the higher weighted pairs having a greater chance of being presented than the lower weighted pairs. 

If pairs are to be selected with equal weighting then users can be given the option to specify which items they have knowledge of before making any comparisons. This can be done at an item level in which case the user is presented with each item in turn and asked if they know it. In this scenario the pairs are chosen only from those items that the user has selected. If many items are included in the study then this can become a lengthy process, so there is also an option to group the items used for the study and allow a user to specify their knowledge at the group level. In this scenario the pairs of items are selected from those groups that the user has selected. Multiple groups can also be used with weighted item selection but each user must select only one group for the study.

Once a user has registered in the system and any pre-selected of items has been completed the comparison judgement phase begins automatically. The user is presented with two of the images and asked, using text configured in the JSON file to make the judgement between the two images.  The user can select an image by clicking on it, if the judgement is equal and the system is configured to allow ties, then both images are selected. To deselect an image that is currently selected the user can click on the image again. When the user is happy with their decision they click the confirm button to move to the next comparison. Depending on the configuration the user can also have the option to skip a judgement using the skip button. Users are able to see and change judgements they have already made by using the previous button to cycle back through the judgements, again this option is determined by the configuration file. For each judgement they are presented with the images and the previous selection they had made. Changing a judgement works in the same way as making a new judgement. The current counts of comparisons made and comparisons skipped are shown at the top of the screen.

![Figure 1](figures/comparison_interface_screenshot.png)
Fig 1: A screenshot of the ranking page from the comparative judgement interface.

Researchers can optionally set the maximum number of judgements that can be made by a user in a number of configuration settings. The length of a cycle can be set as well as the maximum number of cycles that can be completed in any one user session. At the end of a cycle the user is redirected to a page thanking them for their participation and, if a further cycle is still possible, asking them if they would like to continue, and if not inviting them to logout. If they choose to continue the next cycle will start. This process continues until the maximum cycles are reached. At that point the user will no longer be given the option to continue and will instead be invited to logout. As passwords and unique accounts are not created there is nothing to stop the same person registering again starting the process a further time.


# Acknowledgements and Funding

This work was supported by a UKRI Future Leaders Fellowship [MR/X034992/1].

# References

