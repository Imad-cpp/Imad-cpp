# Imad-cpp Profile v2 — Architecture

Status: Proposed foundation
Owner: Imadeddine Es-sebaiy
Date: 2026-08-12

## Purpose

The `Imad-cpp/Imad-cpp` repository is treated as a maintained personal engineering product, not as a decorative README.

Its job is to help a technical visitor, recruiter, collaborator, student or founder quickly understand:

- who Imadeddine is;
- what he has built;
- how he thinks about engineering;
- what he studies and has learned;
- how he uses Git and GitHub in real project work; and
- where to go for deeper evidence.

The public profile remains concise. Detailed material lives in linked GitHub-native pages inside the repository.

## Product principles

1. **Evidence before claims.** Important claims must be supported by a public project, GitHub evidence, LinkedIn, an official institution/program source, or an explicitly approved first-party statement.
2. **Native content before decoration.** Core information stays as searchable, accessible Markdown. Visual assets support the story; they do not replace it.
3. **Static by design.** No GIFs, typing effects, animated SVG, dynamic stat cards, visitor counters or remote badge walls.
4. **Mobile first.** The main reading flow is a single column and must remain useful on a narrow phone viewport.
5. **Progressive depth.** `README.md` is the executive overview. Detailed pages and case studies carry the long-form content.
6. **Public-safe engineering evidence.** Private repository details, secrets, student data and operational weaknesses are never exposed for the sake of demonstrating skill.
7. **Current facts only.** Education, certification and project status are reviewed against the source register before publication.

## Information architecture

```text
Imad-cpp/
├── README.md
├── profile/
│   ├── about.md
│   ├── work.md
│   ├── education.md
│   ├── certifications.md
│   ├── github-engineering.md
│   └── case-studies/
│       ├── n9raw.md
│       ├── nour-fpn.md
│       ├── n9raw-student-dev-kit.md
│       └── nexar.md
├── assets/
│   ├── brand/
│   ├── hero/
│   ├── sections/
│   └── projects/
├── docs/
│   ├── PROFILE_ARCHITECTURE.md
│   ├── VISUAL_SYSTEM.md
│   └── CONTENT_SOURCES.md
├── .github/
│   ├── workflows/
│   │   └── profile-quality.yml
│   └── pull_request_template.md
└── CHANGELOG.md
```

The final tree may be introduced incrementally. Empty placeholder pages are not published merely to satisfy the tree.

## README contract

`README.md` is the GitHub profile homepage. It should answer the most important questions without becoming an autobiography.

Recommended order:

1. responsive identity hero;
2. compact navigation to deep pages;
3. short positioning statement;
4. what I am building now;
5. selected work;
6. engineering focus and working principles;
7. concise education and certification snapshot;
8. GitHub engineering proof points;
9. contact and canonical links.

The README should not duplicate the full content of the deeper pages.

## Deep-page contracts

### `profile/about.md`

Longer professional story: software engineering, product building, cybersecurity, entrepreneurship, Morocco, current direction and working values.

### `profile/work.md`

A capability-led view of real work rather than a generic skill list. Primary groups:

- product and software engineering;
- backend systems, APIs and integrations;
- infrastructure and delivery;
- security-minded engineering;
- technical product architecture and documentation;
- developer education.

Each capability must point to one or more real examples.

### `profile/education.md`

Education timeline with institution, program, dates/status, what the program covers, and a clear separation between first-party academic history and official institution descriptions.

### `profile/certifications.md`

Credential ledger. Every item includes issuer, issue period when available, what was learned, credential identifier/link when public, and source status.

### `profile/github-engineering.md`

Shows GitHub maturity through practices rather than vanity metrics:

- issue-driven work;
- short-lived branches;
- Conventional Commits;
- pull-request review;
- CI quality gates;
- documentation and ADR discipline;
- changelog/progress records where appropriate;
- release and rollback thinking;
- security and privacy hygiene.

Only public-safe evidence is shown.

## Case-study contract

Each project case study follows the same structure so that the reader can compare work easily:

1. **Context** — what the project is and who it serves.
2. **Problem** — the concrete problem being solved.
3. **My role** — founder, product, engineering, infrastructure, or other verified role.
4. **Constraints** — important product, security, data, performance or delivery constraints.
5. **System approach** — architecture and key technical decisions at a public-safe level.
6. **What I built** — implemented work, not aspirations presented as completed work.
7. **GitHub engineering** — branch/PR/CI/documentation practices that can be safely shown.
8. **Security and privacy** — relevant engineering choices without operational exposure.
9. **Stack** — only technologies actually used or approved for the project.
10. **Status and evidence** — current state and public links where available.

Private repositories are never linked as if they were publicly inspectable.

## Visual/content separation

Visual assets may provide:

- identity hero;
- section headers;
- project covers;
- small engineering diagrams that add meaning.

Visual assets must not contain paragraphs of important content. Native Markdown remains the canonical copy.

## Responsive contract

GitHub is the renderer, so the design must work inside GitHub rather than pretending the README is a normal website.

- Default to one content column.
- Avoid fixed two-column tables for primary content.
- Use relative links for repository pages and assets.
- Render major SVG assets at `width="100%"`.
- Provide mobile-specific hero assets if desktop artwork becomes unreadable when scaled down.
- Use `<picture>` only for meaningful theme/viewport variants.
- Keep essential labels large enough to remain readable after mobile scaling.
- Never rely on hover to reveal information.

## Content integrity

`docs/CONTENT_SOURCES.md` is the source register for externally verifiable facts.

Before changing education, certification, employment or project-status copy:

1. identify the source;
2. record the verification date;
3. distinguish personal claims from institution/program descriptions;
4. remove or qualify stale information;
5. do not infer missing dates, titles or outcomes.

## GitHub quality gates

The profile will add a lightweight CI workflow that can run without a web application runtime. The target checks are:

- required-file validation;
- Markdown linting or equivalent structural validation;
- internal relative-link validation;
- SVG XML parsing;
- accessible SVG metadata checks for major visual assets;
- rejection of GIF and animated SVG patterns;
- accidental secret-pattern scan;
- whitespace/basic repository hygiene.

Third-party GitHub Actions must be pinned before use.

## Change workflow

Meaningful changes use:

1. a short-lived `feat/`, `fix/`, `docs/`, `refactor/`, `test/` or `chore/` branch;
2. coherent Conventional Commits;
3. a pull request into `main`;
4. quality checks;
5. review of visual and factual changes;
6. squash or other intentionally selected merge method;
7. a changelog entry for visible profile releases.

Direct profile experimentation on `main` is avoided.

## Delivery phases

### Phase A — Foundation

- architecture;
- visual system;
- source register;
- clean GitHub workflow.

### Phase B — Verified content model

- LinkedIn extraction;
- official education/program research;
- certification ledger;
- project evidence inventory;
- public/private evidence classification.

### Phase C — Deep pages

- About;
- Work;
- Education;
- Certifications;
- GitHub Engineering;
- project case studies.

### Phase D — Visual profile v2

- responsive hero system;
- deep-page headers;
- project visual language;
- light/dark consistency;
- mobile readability review.

### Phase E — README rebuild

- concise homepage;
- navigation into deep pages;
- selected proof rather than duplicated detail.

### Phase F — Quality and release

- CI;
- link and accessibility checks;
- mobile/desktop review;
- factual review against source register;
- pull request evidence;
- release changelog.

## Definition of done

Profile v2 is complete only when:

- the README is concise and works on mobile and desktop;
- light and dark visuals are coherent;
- every deep-page link resolves;
- education and certifications match current sources;
- every material project claim is evidence-backed or clearly presented as first-party context;
- private information is not leaked;
- visuals remain static and accessible;
- CI passes;
- the change is reviewed through a pull request;
- the merged commit is recorded in the changelog.
