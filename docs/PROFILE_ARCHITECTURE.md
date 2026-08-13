# Imad-cpp Profile v1 — Architecture

Status: Approved
Owner: Imadeddine Es-sebaiy
Approved: 2026-08-12
Last reviewed: 2026-08-13

## Purpose

`Imad-cpp/Imad-cpp` is maintained as a **personal engineering product**, not as a decorative README.

Its job is to help a technical visitor, recruiter, collaborator, student or founder quickly understand:

- who Imadeddine is;
- what he has built;
- how he approaches engineering;
- what he has studied and learned;
- how he uses Git and GitHub in real project work; and
- where deeper evidence exists.

The root README stays concise. Detailed material lives in linked GitHub-native Markdown pages.

## Approved product principles

1. **Evidence before claims.** Important claims are backed by a public project, GitHub evidence, LinkedIn, an official institution/program source or an explicitly approved first-party statement.
2. **Native content before decoration.** Core information stays searchable and accessible in Markdown. Visual assets support the story; they do not replace it.
3. **Static by design.** No GIFs, typing effects, animated SVGs, visitor counters, remote stat cards or badge walls.
4. **Mobile first.** The main reading flow is single-column and useful on a narrow phone viewport.
5. **Progressive depth.** `README.md` is the homepage; deeper pages carry long-form content.
6. **Public-safe evidence.** Private repositories may verify claims internally but secrets, student data and operational weaknesses are never exposed for portfolio value.
7. **Current facts only.** Education, certifications and project status are checked against `docs/CONTENT_SOURCES.md`.

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
│       ├── secure-file-gateway.md
│       ├── nour-fpn.md
│       ├── n9raw-student-dev-kit.md
│       └── nexar.md
├── assets/
│   ├── hero/
│   └── projects/ + icons/ + sections/
├── docs/
│   ├── PROFILE_ARCHITECTURE.md
│   ├── VISUAL_SYSTEM.md
│   └── CONTENT_SOURCES.md
└── CHANGELOG.md
```

## README contract

The root README answers the most important questions without becoming an autobiography.

Order:

1. responsive Engineering Signal hero;
2. canonical links;
3. navigation to deep pages;
4. concise positioning;
5. current flagship project;
6. selected systems;
7. engineering focus;
8. education/certification snapshot;
9. technology; and
10. contact links.

The README must not duplicate the full content of deeper pages.

Selected Systems may include a public repository/release link when it materially improves the evidence hierarchy. Secure File Gateway is the current reference example because its repository and V1 release are intentionally public and inspectable.

## Deep-page contracts

### `profile/about.md`

Professional story, current direction and working values.

### `profile/work.md`

Capabilities backed by real project evidence:

- product/software engineering;
- backend systems and integrations;
- infrastructure and delivery;
- security-minded engineering;
- technical architecture/documentation; and
- developer education.

### `profile/education.md`

Personal academic chronology separated clearly from official institution/program descriptions.

### `profile/certifications.md`

Credential ledger with issuer, period, practical relevance and verification source.

### `profile/github-engineering.md`

Shows GitHub maturity through practices rather than vanity metrics: scoped work, commits, review, CI, documentation, security hygiene, release evidence and project history.

## Case-study contract

Each project case study uses the same general shape so visitors can compare work:

1. context;
2. problem;
3. role;
4. product/system approach;
5. implemented work or approved architecture clearly labelled;
6. constraints;
7. GitHub/engineering process where relevant;
8. security/privacy where relevant;
9. current status/evidence boundary; and
10. public evidence.

Private repositories are never linked as if they were publicly inspectable.

A deliberately public engineering repository may be used as direct evidence. In that case the case study should link to inspectable repository/release artifacts and preserve the project's own evidence limits instead of inflating CI or portfolio evidence into production claims.

## Visual/content separation

Visual assets may provide identity, project recognition and small engineering motifs.

They must not contain paragraphs of important information. Native Markdown remains canonical.

A new case study does not automatically require a new large project cover. Existing Engineering Signal icons may carry recognition when a text-led case study is clearer and avoids unnecessary root-profile visual density.

## Responsive contract

GitHub is the renderer, so the design works with GitHub rather than pretending the README is a normal web application.

- One primary content column.
- No fixed two-column layout for essential information.
- Major SVG assets render at `width="100%"`.
- Desktop and mobile hero variants are separate.
- Important labels remain readable around 320–390 px viewport widths.
- No information depends on hover.
- Links may wrap naturally.

## Content integrity

Before changing education, certification, role or project-status copy:

1. identify the source;
2. record/review the verification date;
3. distinguish personal facts from institution/program descriptions;
4. qualify implementation status accurately;
5. preserve explicit evidence boundaries from public engineering artifacts; and
6. do not infer missing dates, titles or outcomes.

## Repository policy — single-branch steady state

The owner's current decision is to keep this personal profile repository in a **single-branch steady state**:

```text
main
```

For this repository:

- `main` is both the source and published GitHub profile state;
- changes are made as small coherent Conventional Commits;
- historical feature branches should be removed after their work is incorporated;
- stale branches are not part of the intended repository structure;
- the changelog records visible releases and material profile changes.

This is a deliberate exception for the owner-only profile repository and does not redefine the stricter branch/PR workflows used by production-sensitive projects such as N9raw or security-focused public projects such as Secure File Gateway.

## Quality gates

Profile V1 changes should be checked for:

- internal relative links;
- missing referenced files;
- SVG XML validity;
- accessible `<title>` / `<desc>` metadata on major SVGs;
- accidental animated SVG/GIF introduction;
- obvious secret/token patterns;
- mobile readability;
- light/dark consistency; and
- factual alignment with `docs/CONTENT_SOURCES.md`.

## Definition of done for V1

V1 is complete only when:

- the root README is concise and useful on mobile and desktop;
- Engineering Signal visuals work in light/dark mode;
- every deep-page link resolves;
- About, Work, Education, Certifications and GitHub Engineering are populated;
- core project case studies are populated;
- education and credentials match current sources;
- material project claims are evidence-backed or clearly first-party context;
- private information is not leaked;
- visuals remain static and accessible;
- repository checks pass; and
- the changelog reflects the release state.
