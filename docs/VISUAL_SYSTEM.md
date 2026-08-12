# Imad-cpp Profile v1 — Visual System

Status: Approved
Owner: Imadeddine Es-sebaiy
Approved: 2026-08-12

## Direction

The approved direction is **Premium Minimal Engineer**.

Official visual name:

# IMAD-CPP / Engineering Signal System

The profile should feel engineered, calm and intentional: more like a technical portfolio system than a social-media banner collection.

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
- terse engineering labels such as `BUILD`, `SECURE`, `SHIP` or `LEARN` are used only when they add meaning.

The motif must never become code rain, a circuit-board wallpaper, a tiled logo pattern or a decorative grid covering every asset.

## Color system

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

Green communicates engineering/system continuity. Gold is intentionally rare and marks a meaningful milestone rather than ordinary decoration.

## Typography

Rendered SVG text uses a safe fallthrough stack:

`Inter, Segoe UI, Arial, sans-serif`

Native profile content uses GitHub's own typography. No custom font files are required or shipped.

## Responsive hero family

Profile V1 uses four explicit hero variants:

```text
assets/hero/
├── hero-desktop-light.svg
├── hero-desktop-dark.svg
├── hero-mobile-light.svg
└── hero-mobile-dark.svg
```

The mobile version removes secondary complexity instead of shrinking desktop text into unreadable microcopy.

The hero contains only:

- `IMAD-CPP / ENGINEERING SIGNAL`;
- Imadeddine Es-sebaiy;
- a concise positioning line;
- the Engineering Signal motif; and
- a short build/security message where space allows.

Detailed biography stays in Markdown.

## Engineering Signal icon family

The post-v1.0 refinement layer adds a compact local SVG icon family for repeated engineering signals:

```text
assets/icons/
├── product-engineering.svg
├── backend-systems.svg
├── cybersecurity.svg
├── infrastructure.svg
├── github-practice.svg
├── verified-learning.svg
├── website.svg
└── professional-network.svg
```

These icons are **recognition and navigation cues, not decoration**.

Rules:

- use only local static SVG assets;
- use signal green for structure and a restrained gold milestone where meaningful;
- do not substitute generic capability cues with official third-party logos;
- do not build badge walls from the icon family;
- do not repeat an icon merely to fill empty space;
- keep inline usage compact, generally around `18–24px`;
- when adjacent text already names the concept, an empty HTML `alt` is acceptable to avoid duplicate screen-reader output; and
- standalone SVG assets still carry their own `<title>`, `<desc>` and `role="img"` metadata.

## Scan-first page hierarchy

Deep pages and case studies use compact text-led maps before long-form detail when that materially improves scanning.

Approved patterns include:

- **Signal areas** on the root README;
- **Capability map** on Work;
- **Learning path** on Education;
- **Verified learning timeline** on Certifications;
- **Engineering record map** on GitHub Engineering; and
- **Case-study map** on project case studies.

These maps must remain short and semantic. They are not substitutes for the detailed Markdown below them.

A typical map uses an icon, a concise label and one short directional statement:

```text
Product → define the problem and system boundary
Backend → implement application and integration logic
Security → protect access, data and operational boundaries
Infrastructure → deploy and operate reliably
Evidence → keep claims traceable and reviewable
```

Avoid turning scan maps into large tables, card grids or decorative dashboards.

## Visual density rules

The root README is the highest-traffic surface and should remain visually restrained.

- Do not keep adding new visual sections after the first-read hierarchy is already clear.
- Prefer improving deeper pages over increasing root-page density.
- Repeated content defaults to short rows or native Markdown structure, not cards.
- Inline icons should improve recognition at a glance; if removing the icon does not reduce comprehension or navigation speed, the icon may be unnecessary.
- Long explanations, evidence and caveats belong in deeper pages and case studies.

## Project visuals

Project visuals are recognition surfaces, not generic UI cards.

They may contain:

- project name;
- one-line purpose;
- role/focus; and
- a restrained project-specific signal motif.

They do not replace the corresponding case study.

When N9raw brand assets are used, N9raw's own approved Page Turn logo and brand rules remain authoritative. The personal Engineering Signal system must not alter or recreate the N9raw symbol.

## Case-study presentation

Case studies should tell a credible engineering or founder story without inflating evidence.

Preferred hierarchy is adapted to the project, for example:

```text
Problem
  ↓
Role / Product approach
  ↓
System or operational approach
  ↓
Important decisions / constraints
  ↓
Evidence boundary
  ↓
Current state
```

The visual system must reinforce evidence quality:

- private implementation detail is not presented as publicly inspectable evidence;
- founder/product evidence is not converted into software claims without implementation proof;
- security-sensitive infrastructure detail stays private; and
- current-state wording must remain distinguishable from future direction.

## Native Markdown first

Important content stays native:

- biography;
- project explanations;
- architecture reasoning;
- education details;
- certification details;
- links and evidence.

SVG is for identity and structure, not paragraphs.

## Responsive rules

- Main content is single-column.
- No primary information depends on desktop-only side-by-side layout.
- Major SVGs render at `width="100%"`.
- Mobile-specific hero variants are preferred over scaled desktop microcopy.
- Essential visual text remains readable around 320–390 px widths.
- Native navigation may wrap naturally.
- No information depends on hover.
- Inline icons must remain legible without forcing horizontal scrolling.

## Light and dark mode

Theme variants carry the same hierarchy and meaning.

Use `<picture>` for theme-aware rendering where GitHub supports the chosen markup.

A dark asset is never treated as complete without its light counterpart when the asset is intended to be theme-aware.

Compact Engineering Signal icons may use a single transparent asset when their palette remains legible on both GitHub themes.

## Accessibility

Major SVG assets must contain:

- `role="img"`;
- a meaningful `<title>`;
- a concise `<desc>`;
- sufficient text/background contrast; and
- no essential information encoded by color alone.

Visual links are never the only path to important content.

Inline decorative/recognition icons must be paired with explicit adjacent text so meaning never depends on the icon alone.

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

The visual identity should still work years later without depending on third-party rendering services.

## Photography

Photography is optional.

If a portrait is introduced, it should appear once as a deliberate identity element and should not dominate the engineering content or become a repeated decorative device.

## Visual acceptance gate

A profile visual is ready only when:

- it belongs to Engineering Signal;
- it works in every required theme/viewport variant;
- it remains readable on mobile;
- it does not contain important long-form copy;
- it has accessible metadata;
- it contains no animation;
- it does not imitate generic GitHub profile templates;
- it does not introduce an unrelated palette or motif;
- it improves recognition, navigation or hierarchy rather than only adding decoration; and
- it supports the content instead of competing with it.
