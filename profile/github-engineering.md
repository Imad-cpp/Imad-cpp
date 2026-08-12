<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/github-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="../assets/sections/github-light.svg">
    <img src="../assets/sections/github-light.svg" width="100%" alt="GitHub — Engineering Practice">
  </picture>
</p>

# GitHub Engineering

[← Back to profile](../README.md) · [About](about.md) · [Work](work.md) · [Education](education.md) · [Certifications](certifications.md)

GitHub is not only where I store code. In my project work, I use it as a **system of record for engineering decisions, review, delivery and project history**.

## My working model

A typical substantial change starts with a clear problem or scoped task and moves through a controlled path:

```text
Problem / Issue
      ↓
Scope and source-of-truth review
      ↓
Implementation
      ↓
Small coherent commits
      ↓
Checks / CI
      ↓
Review and decision
      ↓
Merge / release record
      ↓
Documentation and changelog
```

The exact workflow changes with the repository. A production platform needs stronger review gates than a personal profile repository, but the principle stays the same: **changes should be understandable after the fact**.

## Issues and scoped work

For larger projects, I prefer to connect implementation to a defined issue, backlog item or documented objective instead of making unrelated changes under one vague task.

A good scoped item answers:

- what problem is being solved;
- what is intentionally out of scope;
- what evidence or source controls the decision;
- what needs to be tested; and
- what would make the work complete.

## Branches and repository hygiene

On collaborative or production-sensitive repositories, I use short-lived branches for isolated changes and remove them after merge so the repository does not accumulate stale work.

For this personal profile repository, I currently keep a deliberate **single-branch steady state (`main`)** because it is owner-only and the profile itself is the published artifact. Historical feature branches are not part of the intended long-term structure.

## Commits

I prefer commits that describe one coherent change and can be understood without reading an entire conversation around them.

Examples of the style I use:

```text
feat: add verified education page
fix: make profile mobile-first and native
docs: define profile visual system
security: tighten staging access controls
```

The goal is not perfect commit-message aesthetics. The goal is useful history.

## Pull requests and review

For projects where change risk justifies it, pull requests are the review boundary.

A useful PR should explain:

- the outcome;
- important implementation decisions;
- tests or checks;
- security/privacy implications where relevant;
- documentation changed;
- blockers or known risks; and
- what should happen next.

I avoid treating a PR as complete only because the code compiles.

## Architecture decisions

For N9raw, material architecture and policy decisions are recorded before implementation rather than being hidden inside code changes.

The project uses concepts such as:

- source-of-truth documents;
- decision logs;
- Architecture Decision Records (ADRs);
- explicit open questions;
- phase and backlog records; and
- a definition of done.

This gives future implementation a stable reference and makes it easier to detect when a new idea conflicts with an earlier approved decision.

## CI and quality gates

I use automation to make routine quality checks repeatable.

Depending on the repository, checks can include:

- linting and formatting;
- type checking;
- automated tests;
- build verification;
- Markdown/document validation;
- secret-pattern scanning;
- accessibility or route coverage checks; and
- deployment/release validation.

CI is most useful when it protects an agreed engineering rule, not when it exists only to display a green badge.

## Documentation as engineering evidence

A maintained repository should help the next person understand both **what exists** and **why it exists**.

Documentation I value includes:

- current-state records;
- architecture boundaries;
- operational runbooks;
- data and permission rules;
- progress logs;
- changelogs;
- release procedures; and
- safe rollback instructions.

## Security and GitHub hygiene

I treat repositories as a potential security boundary.

My working rules include:

- no secrets in commits;
- no student or production personal data in examples;
- private repositories for private application code;
- explicit environment separation;
- synthetic/anonymised test data where possible;
- narrow access to privileged systems; and
- review before publishing implementation details that could expose operational weaknesses.

## Public evidence

Some of my main product repositories are intentionally private while they are under development. I do not present a private repository link as if a visitor can inspect it.

Public GitHub surfaces currently include:

- this personal engineering profile;
- the [N9raw GitHub organization](https://github.com/N9RAW); and
- public material released by N9raw when it is reviewed and ready to maintain.

## What “good GitHub” means to me

A strong GitHub presence is not the largest contribution graph or the longest badge list.

It is a repository where another engineer can answer:

1. What is this project?
2. What state is it in?
3. Why was it designed this way?
4. What changed recently?
5. How is a safe change made?
6. What evidence shows the change works?
7. What must never be committed or exposed?

That is the standard I am working toward across my projects.

---

**Next:** [Explore project case studies →](case-studies/n9raw.md)
