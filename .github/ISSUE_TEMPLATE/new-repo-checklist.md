---
name: New Repository Checklist
about: Ensure all new MapLibre repositories confirm to our standards
title: "Onboarding repository [repo]"
labels: onboarding

---

https://github.com/maplibre/[repo]

## Overview
Thank you for your interest in onboarding a new repository to the MapLibre organization! To onboard your repository, you'll need to do the following:
- Create an issue with this template, explain your motivation and follow the checklists contained within.
- Get approval from two MapLibre board members.
- Transfer your repository to the MapLibre organization.
  - Located under Settings -> Transfer ownership, visible to repository owners.
- Address any remaining change requests listed in your issue and close it out.

## Motivation
**<...Explain why this repo is good for MapLibre project, its goals, and any other relevant info...>**

## Acceptance
- [ ] Any two board members must agree to accept a new repository.
  **Approved by:** <@user1> <@user2>

## Licensing
- [ ] The repo license is BSD-3 or MIT.
  *Repos may allow dual-licensing under other open source licenses, e.g. MIT OR Apache.*
- [ ] The repo contains `Copyright (c) <year> MapLibre contributors` in license file(s) and in the readme.

## Special files
- [ ] `/README.md`
  - [ ] Description
  - [ ] link to the main maplibre.org page
  - [ ] name of the OSM-US Slack channel for discussions and an [invite link](https://slack.openstreetmap.us)
- [ ] `/LICENSE`
  *Dual-licensed repos may have additional files like `LICENSE-MIT` and `LICENSE-APACHE`*
- [ ] `/SECURITY.md`
  Add the text:
  ```
  For an up-to-date policy refer to
  https://github.com/maplibre/maplibre/blob/main/SECURITY.md
  ```
- [ ] `/CONTRIBUTING.md`
- [ ] The repo has Pull Request and Issue Templates in `/.github` dir.
- [ ] The repo has `/.github/FUNDING.yml` file copied from [maplibre-gl-js/funding](https://github.com/maplibre/maplibre-gl-js/blob/main/.github/FUNDING.yml)
- [ ] `/CODE_OF_CONDUCT.md`
  *This file should only link to our [primary code of conduct](https://github.com/maplibre/maplibre/blob/main/CODE_OF_CONDUCT.md). Use this markup for consistency:*
  ```md
  # Contributor Covenant
  [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/maplibre/maplibre/blob/main/CODE_OF_CONDUCT.md)
  ```

## Repo Settings
#### General page
- [ ] **[Features]** Disable unused features like wiki.
- [ ] **[Features]** Enable `Sponsorships` checkbox (see also FUNDING.yaml above).
- [ ] **[Features]** Enable `Preserve this repository`.
- [ ] **[Pull Requests]** Community is encouraged to use `squash merge`. Disable other merge types if possible.
- [ ] **[Pull Requests]** Enable `Automatically delete head branches`.

#### Access
- [ ] The repo has at least one admin who is ideally not part of the Governing Board: <@user>

#### Branches
- [ ] The primary branch is named `main`.
- [ ] Set up branch ruleset to require CI pass before merge.  Non-trivial projects should also require an approval before merging.
- [ ] Set up branch ruleset to prevent branch creation - this will prevent accidental pushes directly to the repo, and force all developers to use their own forks.

## Miscelaneous
- [ ] Repo has a proper GitHub description and an optional web site
  *Use the gear icon in the upper right corner of the repo page.*
- [ ] CI automatically runs on all pull requests before merging using GitHub actions
- [ ] Grant admin rights to the board members and automation accounts for packages <list-of-packages>
    - [npmjs.com](https://www.npmjs.com/): package settings / invite:  `maplibreorg nyurik klokan lseelenbinder birkskyum`
    - [crates.io](https://crates.io/): package settings / add owner: `nyurik klokan lseelenbinder`

## Community
- [ ] The new repo has been announced in the `#maplibre` OSMUS slack channel.
- [ ] The new repo has been announced in the next monthly meeting of the Technical Steering Committee.
- [ ] The new repo has been announced on social media.
- [ ] The new repo has been announced in the newsletter.
