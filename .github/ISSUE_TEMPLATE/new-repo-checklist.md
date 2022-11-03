---
name: New Repository Checklist
about: Ensure all new MapLibre repositories confirm to our standards
title: "Onboarding repository [repo]"
labels: onboarding

---

https://github.com/maplibre/[repo]

## Motivation
**<...Explain why this repo is good for MapLibre project, its goals, and any other relevant info...>**

## Acceptance
- [ ] Any two board members must agree to accept a new repository, once the checklist is complete. _Movement to the `maplibre` organization may happen before or after the checklist is complete, but the two "sponsoring" board members is required._
  **Approved by:** <@user1> <@user2>
- [ ] Denote what tier of project it will be (`Core`, `Supported`, `Hosted`): <...tier...> (See discussion: https://github.com/maplibre/maplibre/discussions/132)

## Licensing
- [ ] The repo license is BSD-3 or MIT.
  *Repos may allow dual-licensing under other open source licenses, e.g. MIT OR Apache.*
- [ ] The repo contains `Copyright (c) <year> MapLibre contributors` in license file(s) and in the readme.

## Special files
- [ ] `/README.md`
  *Description, link to the main maplibre.org page, name of the OSM-US Slack channel for discussions and an [invite link](https://osmus-slack.herokuapp.com/), etc*
- [ ] `/LICENSE`
   *Dual-licensed repos may have additional files like `LICENSE-MIT` and `LICENSE-APACHE`*
- [ ] `/CONTRIBUTING.md`
- [ ] The repo has Pull Request and Issue Templates in `/.github` dir.
- [ ] The repo has `/.github/FUNDING.yml` file copied from [maplibre-gl-js/funding](https://github.com/maplibre/maplibre-gl-js/blob/main/.github/FUNDING.yml)
- [ ] `/CODE_OF_CONDUCT.md`
  *This file should only link to our [primary code of conduct](https://github.com/maplibre/maplibre/blob/main/CODE_OF_CONDUCT.md). Use this markup for consistency:*
 `# Contributor Covenant`
 `[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/maplibre/maplibre/blob/main/CODE_OF_CONDUCT.md)`

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
- [ ] Set up branch rules to require CI pass and an approval before merge.
  *For smaller projects it might be OK to ignore this rule.*

## Miscelaneous
- [ ] The repo must not have any personal branches.
  *All work should be done on forks and submitted via PRs, including by the admins.*
- [ ] Repo has a proper GitHub description and an optional web site
  *Use the gear icon in the upper right corner of the repo page.*
- [ ] CI automatically runs on all pull requests before merging using GitHub actions
- [ ] Grant admin rights to the board members and automation accounts for packages <list-of-packages>
  - [npmjs.com](https://www.npmjs.com/): package settings / invite:  `maplibreorg nyurik klokan lseelenbinder wipfli`
  - [crates.io](https://crates.io/): package settings / add owner: `nyurik klokan lseelenbinder wipfli`

## Community
- [ ] The new repo has been announced in the `#maplibre` OSMUS slack channel.
- [ ] The new repo has been announced in the next monthly meeting of the Technical Steering Committee.
- [ ] The new repo has been announced in the `@maplibre` twitter.
