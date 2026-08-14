# Opportunity Tracker — Case Study

[← Back to Work](../work.md) · [Profile](../../README.md) · [Repository](https://github.com/Imad-cpp/opportunity-tracker) · [v1.0.0 Release](https://github.com/Imad-cpp/opportunity-tracker/releases/tag/v1.0.0)

## Case-study map

<img src="../../assets/icons/product-engineering.svg" width="20" alt=""> **Product boundary** — a private application workspace centered on deadlines, next actions and progression rather than a generic job board.  
<img src="../../assets/icons/backend-systems.svg" width="20" alt=""> **Full-stack system** — Next.js/React/TypeScript browser application backed by a Laravel API and PostgreSQL source of truth.  
<img src="../../assets/icons/cybersecurity.svg" width="20" alt=""> **Owner isolation** — every private opportunity read and mutation is scoped server-side; foreign identifiers use enumeration-resistant `404` behavior.  
<img src="../../assets/icons/backend-systems.svg" width="20" alt=""> **Workflow integrity** — status changes and lifecycle history are transactionally coupled, deadlines preserve precision, and archive/delete semantics stay explicit.  
<img src="../../assets/icons/github-practice.svg" width="20" alt=""> **Release evidence** — OpenAPI drift checks, static analysis, secret scanning, dependency audits, migration rollback, Docker smoke and a full browser E2E journey run on the exact release commit.  
<img src="../../assets/icons/verified-learning.svg" width="20" alt=""> **Public proof** — `v1.0.0` is published from the same GitHub-verified commit that passed all permanent release workflows.

## Context

**Opportunity Tracker** is a public full-stack portfolio project for turning scattered opportunity links, deadlines and application notes into one private workflow.

The product is intentionally manual and owner-scoped. It does not scrape third-party sites, rank opportunities with AI or act as a public job board. The engineering objective is to make a narrow personal workflow reliable, inspectable and difficult to accidentally weaken.

**Role:** Product Engineering · Full-stack Engineering · API Design · Security Engineering · CI / Release Engineering

**Public V1:** [`v1.0.0`](https://github.com/Imad-cpp/opportunity-tracker/releases/tag/v1.0.0)  
**Verified release commit:** `694c404415025974f4aa78498bb0e555ca4a2109`

## <img src="../../assets/icons/product-engineering.svg" width="20" alt=""> Problem

Tracking applications usually starts with browser tabs, saved posts, messages and notes. That creates a simple but persistent coordination problem:

- important deadlines are separated from the opportunity itself;
- next actions are easy to forget;
- application status becomes inconsistent across notes;
- archived or rejected items clutter active work;
- searching old opportunities becomes slow; and
- there is no reliable history of what changed.

The product therefore focuses on four questions:

1. What opportunities am I actively tracking?
2. What deadline or next action is closest?
3. Where is each application in the process?
4. What changed recently?

## <img src="../../assets/icons/product-engineering.svg" width="20" alt=""> Product boundary

The core V1 workflow is:

```text
Capture → Prioritize → Prepare → Apply → Follow up → Close
```

V1 includes:

- first-party registration, sign-in and sign-out;
- create/read/edit/archive/restore/permanent-delete flows;
- jobs, internships, scholarships, programs and other opportunity types;
- user-controlled application status;
- priority, organization, source URL, location and plain-text notes;
- date-only or exact-time deadlines;
- next actions with dates;
- search and allowlisted filters;
- deterministic pagination;
- activity history; and
- an action-first dashboard for due-soon, overdue and next-action attention.

The deliberate non-goals are equally important: no scraping, AI matching/writing, CV storage, inbox synchronization, public profiles, shared workspaces, native mobile app, automated status transitions or production notification infrastructure.

## <img src="../../assets/icons/backend-systems.svg" width="20" alt=""> System architecture

The V1 application boundary is:

```text
Browser
  ↓
Next.js + React + TypeScript
  ↓ HTTPS / JSON
Laravel API
  ↓
PostgreSQL
```

The implemented runtime line is:

`Next.js 16.3.1` · `React 19` · `TypeScript` · `Laravel 13` · `PHP 8.4` · `PostgreSQL 18.x` · `Docker Compose` · `GitHub Actions`

PostgreSQL is the only V1 source of truth. Search, dashboard aggregation and lifecycle behavior stay inside the application/database boundary instead of adding Redis, a search engine or microservices before a real requirement needs them.

## <img src="../../assets/icons/cybersecurity.svg" width="20" alt=""> Identity and owner isolation

Authentication uses Laravel Sanctum first-party cookie/session authentication with CSRF protection. The browser does not persist long-lived bearer tokens.

The important authorization rule is simple: an authenticated user can only access their own opportunities.

That rule is enforced server-side rather than inferred from browser state. Private reads and mutations begin from owner-scoped queries, and a foreign opportunity UUID is treated like a missing resource with `404` behavior rather than exposing whether another user's object exists.

The running-stack security workflow also verifies:

- Sanctum CSRF bootstrap;
- trusted credentialed CORS behavior;
- rejection of a state-changing request without the XSRF header; and
- a stable HTTP 419 `CSRF_TOKEN_MISMATCH` error envelope.

## <img src="../../assets/icons/backend-systems.svg" width="20" alt=""> Workflow and data integrity

Status is not an ordinary editable field. A dedicated status path changes application state and records the corresponding history event in one PostgreSQL transaction.

The project also distinguishes several semantics that are easy to flatten in a simpler CRUD implementation:

- archive is reversible while delete is permanent;
- no-op requests do not manufacture duplicate history;
- date-only deadlines stay distinguishable from exact date/time deadlines;
- exact deadlines are normalized while the relevant time zone is retained;
- due-soon/overdue attention is derived only where it is meaningful; and
- user-authored notes stay plain text rather than becoming an HTML surface.

Search is owner-scoped, bounded, allowlisted and deterministically paginated instead of exposing arbitrary query/sort behavior.

## <img src="../../assets/icons/product-engineering.svg" width="20" alt=""> Browser product evidence

The browser application is not a static dashboard mock-up. V1 exposes the complete private workflow:

- create an account;
- sign out and sign back in;
- create an opportunity;
- edit its fields;
- update status;
- search/filter the workspace;
- inspect next actions in the dashboard;
- archive and view archived items;
- restore; and
- permanently delete with explicit confirmation.

The UI includes responsive mobile/desktop layouts, accessible server-validation errors, visible keyboard focus, reduced-motion behavior and explicit loading, empty, error and disabled states.

The E2E suite also stores literal HTML/script text in notes and verifies that it is rendered as text rather than creating a script element.

## <img src="../../assets/icons/github-practice.svg" width="20" alt=""> Contract, CI and release engineering

The repository treats its engineering record as part of the product.

The HTTP boundary is documented in OpenAPI 3.1 and checked against implemented Laravel routes, authentication requirements, references and critical enums. PHPStan, formatting, PostgreSQL-backed tests, Composer audit, full-history Gitleaks scanning and migration rollback/reapply checks are permanent gates.

For the browser/runtime boundary, CI also performs:

- locked npm installation;
- lint and TypeScript checks;
- production Next.js build;
- unconditional high-severity production dependency audit;
- Docker stack build/start and surface smoke; and
- the complete Playwright V1 journey against the running stack.

Before release, the web runtime moved from Next.js 16.2.11 to stable Next.js 16.3.1. That resolved the previous upstream PostCSS/Sharp audit chain, allowing the temporary bounded audit exception to be deleted and the normal hard-fail dependency gate to be restored.

## Exact-commit V1 publication

The release-preparation PR was first green on its candidate head. After squash merge, all seven permanent workflows ran again on the exact `main` commit:

```text
694c404415025974f4aa78498bb0e555ca4a2109
```

The release was published only after that post-merge SHA passed:

- Application Quality;
- Browser E2E;
- Browser Stack Security;
- Contract Quality;
- PHP Static Analysis;
- Secret Hygiene; and
- Migration Rollback.

The `v1.0.0` tag points directly to that same commit, and the GitHub Release is published from the same target rather than from a later unverified state.

## <img src="../../assets/icons/verified-learning.svg" width="20" alt=""> Evidence boundary

The project intentionally does **not** claim:

- production hosting or production availability;
- automatic opportunity discovery;
- AI ranking or application assistance;
- collaborative/team workflows;
- notification infrastructure;
- large-scale performance benchmarks; or
- that a portfolio V1 replaces a production operations program.

The point of the project is stronger when those boundaries remain explicit: it demonstrates product structure, full-stack implementation, security-minded authorization, state integrity and release discipline without inflating the evidence.

## What this project demonstrates

<img src="../../assets/icons/product-engineering.svg" width="20" alt=""> **Product engineering** — turning a common personal workflow into explicit scope, non-scope, states and next-action-oriented UX.  
<img src="../../assets/icons/backend-systems.svg" width="20" alt=""> **Full-stack systems** — Next.js/React browser flows, Laravel API behavior, PostgreSQL persistence and OpenAPI contract discipline.  
<img src="../../assets/icons/cybersecurity.svg" width="20" alt=""> **Security-minded engineering** — session/CSRF boundaries, owner isolation, enumeration resistance, safe notes and dependency hygiene.  
<img src="../../assets/icons/github-practice.svg" width="20" alt=""> **Release engineering** — permanent CI, browser E2E, rollback verification and exact-commit publication.

## Public evidence

- [Repository →](https://github.com/Imad-cpp/opportunity-tracker)
- [Opportunity Tracker v1.0.0 →](https://github.com/Imad-cpp/opportunity-tracker/releases/tag/v1.0.0)
- [V1 release notes →](https://github.com/Imad-cpp/opportunity-tracker/blob/v1.0.0/docs/RELEASE_NOTES_V1.0.0.md)
- [Definition of Done →](https://github.com/Imad-cpp/opportunity-tracker/blob/v1.0.0/docs/DEFINITION_OF_DONE.md)
- [OpenAPI contract →](https://github.com/Imad-cpp/opportunity-tracker/blob/v1.0.0/docs/openapi.json)

---

[Back to Work →](../work.md)
