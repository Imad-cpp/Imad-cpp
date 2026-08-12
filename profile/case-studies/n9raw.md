# N9raw — Case Study

[← Back to Work](../work.md) · [Profile](../../README.md) · [Next: Nour FPN](nour-fpn.md)

## Context

**N9raw** is the main product I am building: a Moroccan student platform designed to help students move from studying and orientation toward opportunities, further education and their first steps into employment.

The product is intentionally broader than a resource library or a blog. Its long-term direction is to organize useful student information around **stage, intent and next action**.

**Role:** Founder · Product · Engineering · Infrastructure

## Problem

Moroccan students often have to search across university sites, social pages, groups, PDFs and disconnected services to answer basic questions:

- What can I study?
- Where can I find reliable course resources?
- Which opportunity fits my level?
- What deadline is approaching?
- What should I do next?

The problem is not only missing information. It is **fragmentation, trust and poor structure**.

## Product approach

N9raw is designed around five primary public areas:

- **Étudier**
- **S’orienter**
- **Opportunités**
- **Étudier à l’étranger**
- **S’informer**

Search is treated as a permanent primary discovery mechanism rather than a secondary utility.

Important factual content is designed to carry source, verification and lifecycle information instead of appearing as anonymous copy.

## My role

I work across multiple layers of the project:

### Product

- defining the product direction and scope;
- structuring student journeys;
- prioritising useful actions over decorative features;
- defining trust requirements for academic and opportunity information.

### Architecture

- shaping the web/API architecture;
- defining module boundaries;
- data and search modelling;
- permissions and privacy rules;
- staging and operational boundaries.

### Engineering governance

- source-of-truth documentation;
- decision logs and ADRs;
- implementation phases and backlog order;
- quality gates and definitions of done;
- GitHub issues, commits, PRs and CI records.

### Infrastructure

- private-staging planning;
- access isolation;
- Cloudflare-oriented edge/access design;
- deployment and rollback thinking;
- separation from other production workloads.

## System approach

The approved architecture uses:

### Web

`Next.js` · `React` · `TypeScript`

### API and administration

`Laravel` modular monolith · `Filament`

### Data and async work

`PostgreSQL` · `Redis` · queues

### Search

`Meilisearch` with PostgreSQL remaining the source of truth

### Edge and delivery

`Cloudflare` · GitHub/GitHub Actions · private object storage design

The project deliberately avoids microservices in the first version because the product does not yet need distributed-system complexity.

## Important constraints

N9raw is designed for a student audience, including minors. That changes the engineering standard.

The project places emphasis on:

- data minimisation;
- server-side permissions;
- private staging;
- controlled file handling;
- source and rights review;
- no real student data in development fixtures;
- accessibility and Arabic/RTL support;
- explicit approval before public launch.

## GitHub engineering

The private platform project uses a documented engineering process where important decisions are traceable before implementation.

Examples of the working model include:

```text
Source of Truth
      ↓
Decision / ADR
      ↓
Scoped backlog item
      ↓
Implementation
      ↓
CI and review
      ↓
Accepted change
      ↓
Progress + changelog update
```

This discipline is particularly useful because product, data, security and architecture decisions can otherwise drift across long-running work.

## Current state

N9raw is under active development. The platform architecture and product blueprint are established, while implementation continues in controlled phases.

The public GitHub organization contains the material that is intentionally ready to share. Private application repositories remain private while development is ongoing.

## What this project demonstrates

N9raw is the clearest example of how I like to work across disciplines:

- product definition;
- software architecture;
- structured data;
- search and information design;
- privacy/security constraints;
- GitHub governance;
- infrastructure planning; and
- long-term system maintainability.

## Public links

- [N9raw](https://n9raw.com)
- [N9raw on GitHub](https://github.com/N9RAW)

---

[Next case study: Nour FPN →](nour-fpn.md)
