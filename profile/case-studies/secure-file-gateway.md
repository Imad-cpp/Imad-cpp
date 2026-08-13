# Secure File Gateway — Case Study

[← Back to Work](../work.md) · [Profile](../../README.md) · [Repository](https://github.com/Imad-cpp/secure-file-gateway) · [v1.0.0 Release](https://github.com/Imad-cpp/secure-file-gateway/releases/tag/v1.0.0)

## Case-study map

<img src="../../assets/icons/backend-systems.svg" width="20" alt=""> **Backend boundary** — authenticated Laravel API for file ingestion, metadata, controlled delivery and deletion.  
<img src="../../assets/icons/cybersecurity.svg" width="20" alt=""> **Untrusted-by-default files** — validation, private quarantine, server-detected MIME, SHA-256 and fail-closed scanning.  
<img src="../../assets/icons/backend-systems.svg" width="20" alt=""> **Asynchronous lifecycle** — Redis-backed scan jobs move server-controlled file states through clean, rejected or failed outcomes.  
<img src="../../assets/icons/infrastructure.svg" width="20" alt=""> **Real dependency evidence** — CI boots PostgreSQL, Redis, MinIO and ClamAV and exercises the application through the real container topology.  
<img src="../../assets/icons/github-practice.svg" width="20" alt=""> **Release engineering** — OpenAPI drift checks, locked dependencies, static analysis, secret hygiene, exact-commit release audit and immutable-tag discipline.  
<img src="../../assets/icons/verified-learning.svg" width="20" alt=""> **Public evidence** — the repository and `v1.0.0` release are inspectable GitHub artifacts rather than private implementation claims.

## Context

**Secure File Gateway** is a public security-focused Laravel API project built to demonstrate a narrow but serious engineering boundary: accepting files without treating uploaded content as trustworthy.

**Role:** Backend Engineering · Security Engineering · API Design · CI / Release Engineering

**Public V1:** [`v1.0.0`](https://github.com/Imad-cpp/secure-file-gateway/releases/tag/v1.0.0)  
**Verified release commit:** `a81e94a9d27a2c2a4511bd45ebced759502b8a64`

## <img src="../../assets/icons/cybersecurity.svg" width="20" alt=""> Problem

File upload looks simple until the application has to defend the boundary around it.

A safer design has to account for problems such as:

- extension spoofing and MIME mismatch;
- malicious content;
- filename/path abuse;
- duplicate-file privacy leaks;
- object-level authorization failures;
- unsafe public storage;
- stale quarantine data;
- signed-link misuse;
- scanner/dependency failures; and
- logs or errors exposing private storage details.

The project deliberately keeps the scope small enough that these controls can be explicit, testable and reviewable.

## <img src="../../assets/icons/backend-systems.svg" width="20" alt=""> V1 system boundary

The core flow is:

```text
Authenticate
    ↓
Validate upload policy
    ↓
Private quarantine
    ↓
Server MIME + SHA-256
    ↓
Redis scan job
    ↓
ClamAV
    ↓
AVAILABLE / REJECTED / SCAN_FAILED
    ↓
Authorized short-lived delivery
```

The V1 stack includes:

`Laravel 13` · `Sanctum` · `PostgreSQL` · `Redis` · `S3-compatible private storage` · `ClamAV` · `OpenAPI` · `Docker Compose` · `GitHub Actions`

## <img src="../../assets/icons/cybersecurity.svg" width="20" alt=""> Security model

The implementation follows several explicit invariants:

- every upload is untrusted by default;
- quarantine objects are never a normal user download surface;
- client filenames and client MIME declarations do not control storage behavior;
- storage keys are server-generated;
- server-side MIME must agree with the allowed extension policy;
- a file cannot become `AVAILABLE` without a clean scanner result and successful promotion into private clean storage;
- scanner errors fail closed;
- file read, download and deletion paths enforce ownership;
- duplicate detection is scoped per owner to avoid a cross-user file-presence oracle; and
- API responses and audit metadata do not expose private object keys, credentials, bearer tokens or signed URLs.

## <img src="../../assets/icons/backend-systems.svg" width="20" alt=""> Lifecycle and failure handling

The lifecycle is controlled by the server rather than the client:

```text
QUARANTINED → SCANNING → AVAILABLE
                  ├────→ REJECTED
                  └────→ SCAN_FAILED

QUARANTINED / SCANNING / AVAILABLE / REJECTED / SCAN_FAILED
                         ↓
                      DELETED
```

The project also treats object storage and database persistence as separate failure domains. Upload and cleanup paths use compensating behavior so a failed database or queue step does not silently become a successful file state.

## <img src="../../assets/icons/cybersecurity.svg" width="20" alt=""> Authorization and delivery

Authentication uses Laravel Sanctum bearer tokens with finite lifetime and throttled auth surfaces.

File metadata is owner-scoped, and foreign file identifiers use enumeration-resistant behavior rather than returning a distinct authorization signal.

A downloadable file must already be `AVAILABLE`. The application issues a short-lived signed capability, then re-checks lifecycle state when content is requested. Deletion therefore revokes future delivery even if an older capability URL still exists.

## <img src="../../assets/icons/infrastructure.svg" width="20" alt=""> Real integration evidence

The permanent CI workflow does more than unit-test application code.

Its infrastructure integration job boots the actual local topology with:

- Laravel application container;
- PostgreSQL;
- Redis;
- MinIO-compatible private object storage; and
- ClamAV.

CI applies PostgreSQL migrations, waits for aggregate readiness, starts the Redis-backed scan worker, sends a clean file through the complete application path, exercises a runtime-generated EICAR antivirus test fixture, and runs the reproducible public V1 demo.

The clean path must reach `AVAILABLE`, issue a temporary delivery capability, return byte-identical content and delete successfully. The EICAR path must reach `REJECTED` and remain non-downloadable.

## <img src="../../assets/icons/github-practice.svg" width="20" alt=""> GitHub and release engineering

`v1.0.0` is tied to a specific verified commit instead of being created from an informal “looks good” state.

The permanent **Application Quality** workflow contains four release-relevant gates:

1. `php-quality` — strict Composer lock validation/install, Pint, Larastan/PHPStan, tests, OpenAPI route-drift checks and Composer audit;
2. `secret-hygiene` — full-history Gitleaks scanning;
3. `infrastructure-integration` — real PostgreSQL/Redis/object-storage/ClamAV lifecycle and reproducible demo; and
4. `release-audit` — a dependent Definition-of-Done gate that runs only after the other three succeed and emits `V1_RELEASE_AUDIT=PASS`.

The public `v1.0.0` annotated tag resolves to:

```text
a81e94a9d27a2c2a4511bd45ebced759502b8a64
```

The release was published only after the post-merge quality workflow passed on that exact `main` commit.

## <img src="../../assets/icons/verified-learning.svg" width="20" alt=""> Evidence boundary

The project intentionally does **not** claim:

- production readiness or production availability guarantees;
- malware-detection completeness or arbitrary-file safety;
- production monitoring or incident-response maturity;
- an immutable forensic audit ledger;
- generic bucket-wide orphan discovery; or
- performance/scale benchmarks.

That boundary matters to me: public engineering evidence should show what was actually demonstrated, not expand a portfolio project into unsupported production claims.

## What this project demonstrates

<img src="../../assets/icons/backend-systems.svg" width="20" alt=""> **Backend systems** — authenticated API design, PostgreSQL metadata, queues, object-storage boundaries and lifecycle logic.  
<img src="../../assets/icons/cybersecurity.svg" width="20" alt=""> **Security engineering** — threat-aware upload policy, object authorization, private storage, fail-closed scanning and safe delivery.  
<img src="../../assets/icons/infrastructure.svg" width="20" alt=""> **Integration reliability** — real Redis, PostgreSQL, object storage and ClamAV exercised in CI.  
<img src="../../assets/icons/github-practice.svg" width="20" alt=""> **Engineering discipline** — OpenAPI, locked dependencies, static analysis, secret scanning, release audit and exact-commit publication.

## Public evidence

- [Repository →](https://github.com/Imad-cpp/secure-file-gateway)
- [Secure File Gateway v1.0.0 →](https://github.com/Imad-cpp/secure-file-gateway/releases/tag/v1.0.0)
- [V1 release audit →](https://github.com/Imad-cpp/secure-file-gateway/blob/v1.0.0/docs/V1_RELEASE_AUDIT.md)
- [V1 evidence ledger →](https://github.com/Imad-cpp/secure-file-gateway/blob/v1.0.0/docs/V1_EVIDENCE.md)
- [OpenAPI contract →](https://github.com/Imad-cpp/secure-file-gateway/blob/v1.0.0/openapi.yaml)

---

[Back to Work →](../work.md)
