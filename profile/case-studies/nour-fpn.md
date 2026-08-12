<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="../../assets/projects/case-nour-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="../../assets/projects/case-nour-light.svg">
    <img src="../../assets/projects/case-nour-light.svg" width="100%" alt="Nour FPN case study — Backend, Integrations, Automation and Operations">
  </picture>
</p>

# Nour FPN — Case Study

[← Back to Work](../work.md) · [Profile](../../README.md) · [Previous: N9raw](n9raw.md) · [Next: Student Dev Kit](n9raw-student-dev-kit.md)

## Context

**Nour FPN** is a WhatsApp-first student assistant for students at the Faculté Pluridisciplinaire de Nador, developed under N9raw.

It is designed to make common student services easier to reach from a familiar channel, especially when students need quick academic information rather than another dashboard to learn.

**Role:** Product · Backend · Integrations · Operations

## Problem

Student information is often spread across several places and may be difficult to reach quickly from a phone.

Nour FPN brings practical academic services into one conversational flow so that a student can access the next useful action without navigating several separate systems.

## What the system supports

The current application includes flows and services around areas such as:

- student lookup and confirmation;
- results and grades;
- timetables;
- exam planning;
- repartitions and groups;
- institutional email guidance;
- faculty/program WhatsApp links;
- FAQ;
- problem reporting; and
- multilingual interaction.

Some capabilities can exist technically while remaining disabled at the product-routing layer until they are ready for active use.

## Architecture

At a public-safe level, the core message path is:

```text
WhatsApp Cloud API
        ↓
Laravel webhook
        ↓
Queued incoming-message processing
        ↓
Student / academic domain services
        ↓
Response sender
        ↓
Meta Graph API
```

The system uses Laravel with asynchronous processing so that incoming webhook handling, student-service logic and outgoing messages are not collapsed into one fragile request.

## Administration

The project also includes administration for controlled operational work, including scoped management of student-facing content and academic mappings.

The permission model is designed so that different operational roles do not automatically receive access to every sensitive field or action.

## Multilingual design

Nour FPN supports:

- Arabic / Darija-oriented student interactions;
- French; and
- English.

This is not only a translation concern. It affects conversation structure, labels, directionality and how short mobile interactions are written.

## Security and privacy

Because the system handles student-related information, I treat privacy boundaries as part of the architecture.

Important design principles include:

- limiting sensitive information to authorised contexts;
- avoiding unnecessary exposure in logs and public surfaces;
- separating administrative permissions;
- keeping credentials and raw provider payloads private;
- controlled production changes; and
- never using real student data as public portfolio evidence.

This case study intentionally omits private infrastructure identifiers, credentials, internal security details and student records.

## Operations

Nour FPN has also given me practical experience with the operational side of a real service:

- Linux and Nginx;
- PHP/Laravel deployment;
- queues and worker supervision;
- environment configuration;
- release/deploy separation;
- production diagnostics; and
- safe change procedures.

This is one of the projects where application development and operations are tightly connected: a correct feature is not useful if the webhook, queue or worker path is unreliable.

## GitHub and documentation

The private repository keeps current-state documentation and operational guidance alongside the application so production-sensitive work does not depend only on memory or chat history.

The project remains private because the repository contains implementation and operational detail that is not appropriate to expose publicly.

## Current state

Nour FPN is an operational, pre-1.0 product under controlled development.

It is an independent student initiative and does not replace official FPN or Université Mohammed Premier systems.

## What this project demonstrates

Nour FPN is my strongest practical example of:

- Laravel backend engineering;
- webhook and external API integration;
- asynchronous message processing;
- conversational product flows;
- scoped administration;
- student-data privacy thinking;
- Linux production operations; and
- maintaining a real service after initial implementation.

---

[Next case study: N9raw Student Dev Kit →](n9raw-student-dev-kit.md)
