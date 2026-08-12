# Changelog

All meaningful public-profile changes are recorded here.

## 2026-08-12 — Profile v1.1.0 / Engineering Signal Refinement

### Release scope

Profile v1.1.0 refines the maintained Engineering Signal profile after the v1.0.0 baseline. It improves scanability, extends the visual language into compact local cues, strengthens deeper-page and case-study hierarchy, tightens evidence boundaries, and aligns the public GitHub account metadata with the profile contract.

### Added

- Compact **Engineering Signal icon family** for Product Engineering, Backend Systems, Cybersecurity, Infrastructure, GitHub Practice and Verified Learning.
- Additional local signal icons for the personal website and professional network.
- Scan-first **Signal areas** on the root README.
- Compact visual workflow cues for **How I engineer**.
- Structured visual grouping for Education, Technology and Connect sections.
- Capability-map treatment on the Work page.
- Learning-path treatment on the Education page.
- Verified-learning timeline treatment on the Certifications page.
- Engineering-record map on the GitHub Engineering page.
- Case-study maps for N9raw, Nour FPN, N9raw Student Dev Kit and Nexar.

### Changed

- Refined the root README for faster scanning while keeping the visual density restrained and GitHub-native.
- Added compact project cues to Selected Systems without introducing a card wall.
- Improved About page hierarchy with Engineering Signal cues while preserving the existing page header and factual content.
- Reworked Work into a clearer capability hierarchy across product, backend, security, infrastructure, documentation and developer education.
- Made the education path easier to scan as degree → cybersecurity program → applied learning.
- Reframed certifications as a verified-learning timeline rather than a badge collection.
- Reworked GitHub Engineering as an engineering system of record covering scope, commits, CI, ADRs, documentation, traceability and safety.
- Reorganized N9raw case-study hierarchy around problem, role, system approach, decisions, evidence and current state.
- Reorganized Nour FPN around student flow, backend/integrations, administration, multilingual design, privacy and operations.
- Reorganized N9raw Student Dev Kit around learning outcomes, Git/GitHub workflow, bilingual parity, repository discipline, privacy and rights.
- Reorganized Nexar as founder/product evidence while making the software-evidence boundary explicit.
- Extended the Engineering Signal system from large section/project visuals into small recognition and navigation cues across deeper pages.
- Aligned the public GitHub account metadata with the approved profile contract: display name, founder/engineering bio, company, location and website.

### Fixed

- Clarified the N9raw stack label on the root README as **Approved architecture** so approved/future architecture is not implied to be fully implemented.
- Normalized the Nexar case-study map and current-state heading hierarchy with the other project case studies.

### Visual-system rules added

- Engineering Signal icons are recognition/navigation cues, not decoration.
- Local static SVG is preferred; no remote badge/stat dependencies are introduced.
- Green remains the structural/signal color and gold remains a restrained milestone accent.
- Inline icons are generally used around `18–24px` and must be paired with explicit adjacent text.
- Capability maps and case-study maps remain short, text-led and mobile-first.
- Root README visual density should not keep growing once the first-read hierarchy is clear; deeper pages are the preferred place for additional detail.
- Founder/product claims, private implementation evidence and public software claims remain explicitly separated.

### Validation

Each logical refinement was committed to `main` and validated by the repository's **Profile Quality** workflow, including internal link checks, SVG parsing/accessibility checks, static-only visual rules and basic secret hygiene.

## 2026-08-12 — Profile v1.0.0 / Engineering Signal

### Release scope

Profile v1.0.0 establishes the first maintained public baseline for the personal GitHub profile: a concise root profile, verified deeper pages, public-safe project case studies, the IMAD-CPP / Engineering Signal visual system and automated profile-quality validation.

### Added

- **IMAD-CPP / Engineering Signal System** as the approved personal visual language.
- Responsive desktop/mobile light/dark identity hero family.
- Theme-aware Engineering Signal headers for About, Work, Education, Certifications and GitHub Engineering.
- Theme-aware case-study covers for N9raw, Nour FPN, N9raw Student Dev Kit and Nexar.
- Detailed GitHub-native pages for About, Work, Education, Certifications and GitHub Engineering.
- Public-safe case studies for N9raw, Nour FPN, N9raw Student Dev Kit and Nexar.
- Verified content/source register for LinkedIn, education, certifications and GitHub evidence.
- Project-grade profile architecture and visual-system documentation.
- Automated Profile Quality checks for internal links, SVG validity/accessibility, static-only visuals and basic secret hygiene.
- Public account-metadata contract for display name, bio, company, location and website.

### Changed

- Rebuilt the root profile README as a concise homepage with progressive links into deeper pages.
- Sharpened the first-read experience so the root profile moves directly from identity to current focus, selected systems, engineering proof, education and contact.
- Kept N9raw as the only featured project visual on the root profile while moving the remaining project covers to their deeper case studies.
- Reduced duplicated engineering and technology copy on the root profile; detailed evidence now lives in Work and GitHub Engineering.
- Replaced the stale generic `Licence SMI` profile label with the verified `Informatique et Intelligence Artificielle` degree wording.
- Separated personal academic history from official institution/program descriptions.
- Reframed technology and GitHub claims around evidence and real project work rather than badge/stat walls.
- Kept private repositories as internal verification sources without presenting them as publicly inspectable evidence.
- Extended the Engineering Signal language from the root hero into the complete Profile v1 page and project system.
- Removed legacy hero/project visuals after the Engineering Signal replacements became canonical.

### Visual rules

- Static only: no GIFs, typing effects, animated SVG, visitor counters or remote stat cards.
- Native Markdown carries important content; SVG supports identity and recognition.
- Mobile and desktop readability are treated separately rather than shrinking one fixed desktop composition.
- Light and dark assets carry the same information hierarchy.
- Project covers remain personal-profile visuals and do not replace or redraw each project's own brand identity.

### Repository policy

- The intended steady state is a single `main` branch for this owner-only profile repository.
- Historical development branches are removed after their work is incorporated.
- The one-time branch-cleanup workflow was removed after successfully restoring the repository to `main` only.

## Earlier 2026-08-12 iterations

### Added

- Initial static GitHub profile README.
- Theme-aware identity hero.
- Static N9raw, Nour and N9raw Student Developer Kit project visuals.
- Native Markdown sections for engineering focus, technology, education and contact links.

### Fixed

- Reworked the initial visual profile into a more mobile-first GitHub-native reading flow.
- Restored a hybrid visual/native Markdown presentation without GIFs or animated effects.
