# Imad-cpp Profile v2 — Visual System

Status: Proposed foundation
Owner: Imadeddine Es-sebaiy
Date: 2026-08-12

## Direction

The approved direction is **Premium Minimal Engineer**.

The profile should feel engineered, calm and intentional: more like a technical portfolio system than a social-media banner collection.

Working visual name: **IMAD-CPP / Engineering Signal System**.

The visual language grows from the current profile's strongest idea — connected engineering nodes and disciplined green/gold accents — while reducing tiny decorative text and repeated project banners.

## Personality

- precise;
- technical;
- premium without looking corporate-heavy;
- security-aware;
- modern but not trend-dependent;
- confident without inflated claims;
- recognisable without visual noise.

## Core motif — Engineering Signal

The recurring motif is a restrained network/path system:

- nodes represent decisions, systems and milestones;
- connecting lines represent architecture and delivery paths;
- one warm gold node may mark a meaningful milestone;
- labels use terse engineering language such as `BUILD`, `SECURE`, `SHIP`, `LEARN` only when they add meaning.

The motif must never become code rain, a circuit-board wallpaper, a tiled logo pattern or a decorative grid covering every asset.

## Color system

The existing profile already establishes a useful base. Profile v2 keeps it coherent instead of introducing another unrelated palette.

### Dark surface

- Carbon: `#0B1110`
- Deep line: `#22312B`
- Primary text: `#F4F7F5`
- Secondary text: `#C7D1CC`
- Muted text: `#86948E`
- Signal green: `#57B884`
- Milestone gold: `#C9A84F`

### Light surface

- Soft ivory: `#F7F9F8`
- Border: `#D9E2DE`
- Primary text: `#111816`
- Secondary text: `#33443D`
- Muted text: `#66756E`
- Signal green: `#2F8F68`
- Milestone gold: `#C9A84F`

Green communicates engineering/system continuity. Gold is intentionally rare and should mark one milestone or high-value detail, not ordinary decoration.

## Typography

Rendered SVG text uses a safe fallthrough stack:

`Inter, Segoe UI, Arial, sans-serif`

Native profile content uses GitHub's own typography. The visual system must not depend on shipping custom font files.

Text hierarchy inside SVG assets:

- identity: bold and dominant;
- role line: one concise line;
- micro-labels: optional and never essential;
- paragraphs: prohibited inside decorative assets.

## Hero system

The hero should become a real responsive asset family rather than one desktop banner scaled everywhere.

Target family:

```text
assets/hero/
├── hero-desktop-light.svg
├── hero-desktop-dark.svg
├── hero-mobile-light.svg
└── hero-mobile-dark.svg
```

Desktop and mobile versions share the same message and motif. The mobile version removes secondary microcopy instead of shrinking it into unreadable text.

The hero should contain only:

- Imadeddine Es-sebaiy;
- one concise engineering positioning line;
- one recognisable Engineering Signal motif;
- optional `IMAD-CPP` system label.

Detailed descriptions stay in Markdown directly below the hero.

## Deep-page header system

Every major profile page may have a compact static header using the same visual grammar.

Examples:

- `ABOUT / SYSTEMS & PRODUCT`
- `WORK / BUILD & SHIP`
- `EDUCATION / LEARN & APPLY`
- `CERTIFICATIONS / VERIFIED LEARNING`
- `GITHUB / ENGINEERING PRACTICE`

Headers identify the page; they do not repeat page content.

## Project visuals

Project visuals are not generic cards.

Each case study may use one wide cover containing:

- project name;
- one-line purpose;
- role or focus;
- a project-specific diagram or structured motif where useful.

The design remains visually related to the personal system but does not overwrite the project's own brand identity.

N9raw visuals must respect N9raw's approved Page Turn logo and brand rules when its logo is used. Personal profile motifs must never alter or recreate the N9raw symbol.

## Native Markdown first

Important content is never trapped inside images.

Use native Markdown for:

- biography;
- roles;
- project explanations;
- architecture reasoning;
- education details;
- certification details;
- links and evidence.

Use SVG only when visual structure improves recognition or comprehension.

## Responsive rules

- Main content is single-column by default.
- No primary information depends on a desktop-only side-by-side layout.
- Major SVGs render at `width="100%"`.
- Mobile-specific hero variants are preferred over tiny scaled desktop text.
- Project covers must remain understandable around a 320–390 px viewport.
- Text inside mobile SVGs is kept intentionally sparse.
- Native link navigation is allowed to wrap naturally.

## Light and dark mode

Theme variants are paired. A dark asset is never created without considering its light counterpart.

Use `<picture>` for theme-aware rendering where GitHub supports the chosen markup.

The content hierarchy and meaning must remain identical across themes.

## Accessibility

Major SVG assets must contain:

- `role="img"`;
- a meaningful `<title>`;
- a concise `<desc>`;
- sufficient contrast;
- no essential information encoded by color alone.

Decorative SVG elements should not create repetitive screen-reader noise.

Link labels in Markdown remain descriptive; visual CTA text is not the only path to a destination.

## Static-only rule

Prohibited:

- GIF files;
- animated SVG elements;
- typing animations;
- auto-updating contribution/stat cards;
- visitor counters;
- blinking cursors;
- marquees;
- remote badge walls;
- decorative motion.

The profile should still look current years from now without depending on third-party rendering services.

## Photography

Photography is allowed, but not required.

If a portrait is introduced later, it should be used once as a deliberate identity element, not repeated through the page. It must not compete with the engineering content or become the dominant visual language.

## Visual acceptance gate

A profile visual is ready only when:

- it belongs to the Engineering Signal system;
- it works in both required themes;
- it is readable on mobile;
- it does not contain important long-form copy;
- it has accessible metadata;
- it contains no animation;
- it does not imitate generic GitHub profile templates;
- it does not introduce an unrelated palette or motif;
- it supports the content instead of competing with it.
