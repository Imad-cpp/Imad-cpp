<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="../../assets/projects/case-nour-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="../../assets/projects/case-nour-light.svg">
    <img src="../../assets/projects/case-nour-light.svg" width="100%" alt="Nour FPN case study — Backend, Integrations, Automation and Operations">
  </picture>
</p>

# Nour FPN — Case Study

[← Back to Work](../work.md) · [Profile](../../README.md) · [Previous: N9raw](n9raw.md) · [Next: Student Dev Kit](n9raw-student-dev-kit.md)

## Case-study map

<img src="../../assets/icons/product-engineering.svg" width="20" alt=""> **Problem** — make practical academic services easier to reach from a familiar mobile channel.  
<img src="../../assets/icons/backend-systems.svg" width="20" alt=""> **Student flow** — connect student-facing WhatsApp interactions to academic-service logic.  
<img src="../../assets/icons/backend-systems.svg" width="20" alt=""> **Backend & integrations** — Laravel, webhooks, queues, domain services and outgoing provider calls.  
<img src="../../assets/icons/cybersecurity.svg" width="20" alt=""> **Admin & permissions** — keep operational roles scoped instead of exposing every sensitive field or action.  
<img src="../../assets/icons/infrastructure.svg" width="20" alt=""> **Operations** — run and diagnose a real service across Linux, Nginx, workers and deployment paths.  
<img src="../../assets/icons/cybersecurity.svg" width="20" alt=""> **Security & privacy** — keep student data, credentials and private operational detail out of public evidence.

## Context

**Nour FPN** is a WhatsApp-first student assistant for students at the Faculté Pluridisciplinaire de Nador, developed under N9raw.

It is designed to make common student services easier to reach from a familiar channel, especially when students need quick academic information rather than another dashboard to learn.

**Role:** Product · Backend · Integrations · Operations

## <img src="../../assets/icons/product-engineering.svg" width="20" alt=""> Problem

Student information is often spread across several places and may be difficult to reach quickly from a phone.

Nour FPN brings practical academic services into one conversational flow so that a student can access the next useful action without navigating several separate systems.

## <img src="../../assets/icons/product-engineering.svg" width="20" alt=""> Student-facing flow

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

## <img src="../../assets/icons/backend-systems.svg" width="20" alt=""> Backend and integrations

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

## <img src="../../assets/icons/cybersecurity.svg" width="20" alt=""> Administration and permissions

The project includes administration for controlled operational work, including scoped management of student-facing content and academic mappings.

The permission model is designed so that different operational roles do not automatically receive access to every sensitive field or action.

## <img src="../../assets/icons/product-engineering.svg" width="20" alt=""> Multilingual interaction

Nour FPN supports:

- Arabic / Darija-oriented student interactions;
- French; and
- English.

This is not only a translation concern. It affects conversation structure, labels, directionality and how short mobile interactions are written.

## <img src="../../assets/icons/cybersecurity.svg" width="20" alt=""> Security and privacy

Because the system handles student-related information, I treat privacy boundaries as part of the architecture.

Important design principles include:

- limiting sensitive information to authorised contexts;
- avoiding unnecessary exposure in logs and public surfaces;
- separating administrative permissions;
- keeping credentials and raw provider payloads private;
- controlled production changes; and
- never using real student data as public portfolio evidence.

This case study intentionally omits private infrastructure identifiers, credentials, internal security details and student records.

## <img src="../../assets/icons/infrastructure.svg" width="20" alt=""> Operations

Nour FPN has given me practical experience with the operational side of a real service:

- Linux and Nginx;
- PHP/Laravel deployment;
- queues and worker supervision;
- environment configuration;
- release/deploy separation;
- production diagnostics; and
- safe change procedures.

This is one of the projects where application development and operations are tightly connected: a correct feature is not useful if the webhook, queue or worker path is unreliable.

## <img src="../../assets/icons/github-practice.svg" width="20" alt=""> Engineering record

The private repository keeps current-state documentation and operational guidance alongside the application so production-sensitive work does not depend only on memory or chat history.

The project remains private because the repository contains implementation and operational detail that is not appropriate to expose publicly.

## <img src="../../assets/icons/verified-learning.svg" width="20" alt=""> Current state

Nour FPN is an operational, pre-1.0 product under controlled development.

It is an independent student initiative and does not replace official FPN or Université Mohammed Premier systems.

## What this project demonstrates

<img src="../../assets/icons/backend-systems.svg" width="20" alt=""> **Backend systems** — Laravel backend engineering, webhook integration and asynchronous message processing.  
<img src="../../assets/icons/product-engineering.svg" width="20" alt=""> **Product flows** — conversational service design and multilingual student interaction.  
<img src="../../assets/icons/cybersecurity.svg" width="20" alt=""> **Scoped administration** — permissions and student-data privacy thinking.  
<img src="../../assets/icons/infrastructure.svg" width="20" alt=""> **Operations** — Linux production operations and maintaining a real service after initial implementation.

---

[Next case study: N9raw Student Dev Kit →](n9raw-student-dev-kit.md)
