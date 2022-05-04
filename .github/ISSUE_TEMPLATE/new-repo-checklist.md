---
name: New Repository Checklist
about: Ensure all new MapLibre repositories confirm to our standards
title: "Onboarding repository [repo]"

---

# Procedural
- [ ] Any two board members must agree to accept a new repository. Names: [name1], [name2]

# Licensing
- [ ] The repo license is BSD-3 or MIT.  Repos may allow dual-licensing under other open source licenses like Apache.
- [ ] The repo contains Copyright (c) <year> MapLibre contributors.
- [ ] The repo has a `/LICENSE` file (could also have additional `LICENSE-MIT` / `LICENSE-APACHE` files as needed).

# Other Files
- [ ] The repo has `/CONTRIBUTING.md`
- [ ] The repo has `/README.md`
- [ ] The repo has `/CODE_OF_CONDUCT.md`

# Organizational
- [ ] The repo has at least one admin who is ideally not part of the Governing Board.
- [ ] The repo has the GitHub sponsors button.
- [ ] The primary branch is named `main`
- [ ] There are no personal branches - all work should be done on forks and submitted via PRs.
- [ ] Community is encouraged to use `squash merge` (disable other merge types if possible)
- [ ] Disable unused features like wiki
- [ ] Set up branch rules to require CI pass and an approval before merge<br>For smaller projects it might be OK to ignore this rule.
- [ ] All Pull Requests are tested before merging using GitHub actions
  
# Community
- [ ] The new repo has been announced in the `#maplibre` OSMUS slack channel.
- [ ] The new repo has been announced in the next monthly meeting of the Technical Steering Committee.
- [ ] The new repo has been announced in the `@maplibre` twitter.
