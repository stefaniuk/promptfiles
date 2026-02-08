# ADR-001e: Python logging 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-08` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Quality attributes, Operations`                |

---

- [ADR-001e: Python logging 🧾](#adr-001e-python-logging-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: structlog (Selected) ✅](#option-a-structlog-selected-)
      - [Option B: logging (standard library)](#option-b-logging-standard-library)
      - [Option C: loguru](#option-c-loguru)
      - [Option D: python-json-logger](#option-d-python-json-logger)
      - [Option E: AWS Powertools Logger](#option-e-aws-powertools-logger)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

The Python tech stack needs a default logging approach that supports structured output, multi-sink logging (JSON file plus readable console), log levels, and a good developer experience.

## Decision ✅

### Assumptions 🧩

- Python 3.14.3 is the baseline runtime.
- Structured JSON logs are required for services.
- Local developer output should be readable and optionally coloured.

### Drivers 🎯

- Structured logging support with JSON output
- Multi-sink management (JSON to file and readable console output)
- Pretty, coloured console output for local use
- Log levels and filtering support
- Performance suitable for services and CLIs
- Low dependency footprint
- Ecosystem support and longevity

Weighted criteria use a 1-5 scale (higher is more important). Scores use ⭐ (1), ⭐⭐ (2), ⭐⭐⭐ (3). Weighted totals exclude Effort and have a maximum of 69.

| Criteria                 | Weight | Rationale                                          |
| ------------------------ | ------ | -------------------------------------------------- |
| Structured logging       | 5      | Highest priority for consistency and observability |
| Multi-sink management    | 4      | Core requirement for JSON file plus console output |
| Console pretty/colour    | 4      | Developer experience for local runs                |
| Log levels and filtering | 4      | Needed for operational control                     |
| Performance              | 2      | Important but secondary                            |
| Dependency footprint     | 2      | Prefer lighter dependencies                        |
| Ecosystem support        | 2      | Adoption matters for longevity                     |

### Options 🔀

#### Option A: structlog (Selected) ✅

Use [`structlog`](https://github.com/hynek/structlog) with standard logging handlers for JSON files and console output.

| Criteria                 | Score/Notes                               |
| ------------------------ | ----------------------------------------- |
| Structured logging       | ⭐⭐⭐ Purpose-built for structured logs  |
| Multi-sink management    | ⭐⭐⭐ Integrates with logging handlers   |
| Console pretty/colour    | ⭐⭐ Works with console formatters        |
| Log levels and filtering | ⭐⭐⭐ Standard logging levels            |
| Performance              | ⭐⭐ Good for most services               |
| Dependency footprint     | ⭐⭐ External dependency                  |
| Ecosystem support        | ⭐⭐⭐ Strong adoption in Python services |
| Effort                   | M                                         |
| Weighted score (max 69)  | 61                                        |

#### Option B: logging (standard library)

Use the standard [`logging`](https://github.com/python/cpython) module with custom formatters.

| Criteria                 | Score/Notes                        |
| ------------------------ | ---------------------------------- |
| Structured logging       | ⭐ Requires custom JSON formatting |
| Multi-sink management    | ⭐⭐⭐ Strong handler support      |
| Console pretty/colour    | ⭐ Limited without extra packages  |
| Log levels and filtering | ⭐⭐⭐ Built in levels             |
| Performance              | ⭐⭐⭐ Fast                        |
| Dependency footprint     | ⭐⭐⭐ Standard library            |
| Ecosystem support        | ⭐⭐⭐ Universal                   |
| Effort                   | M                                  |
| Weighted score (max 69)  | 51                                 |

**Why not chosen**: Structured logging is not first-class without extra tooling.

#### Option C: loguru

Use [`loguru`](https://github.com/Delgan/loguru) for ergonomic logging.

| Criteria                 | Score/Notes                          |
| ------------------------ | ------------------------------------ |
| Structured logging       | ⭐⭐ Supports JSON but less explicit |
| Multi-sink management    | ⭐⭐⭐ Strong multi-sink support     |
| Console pretty/colour    | ⭐⭐⭐ Built-in coloured output      |
| Log levels and filtering | ⭐⭐⭐ Strong level support          |
| Performance              | ⭐⭐ Good for most services          |
| Dependency footprint     | ⭐⭐ External dependency             |
| Ecosystem support        | ⭐⭐ Popular but smaller ecosystem   |
| Effort                   | M                                    |
| Weighted score (max 69)  | 58                                   |

**Why not chosen**: Strong developer experience, but structured logging is less central than in structlog.

#### Option D: python-json-logger

Use [`python-json-logger`](https://github.com/madzak/python-json-logger) to add JSON formatting to the standard logging module.

| Criteria                 | Score/Notes                            |
| ------------------------ | -------------------------------------- |
| Structured logging       | ⭐⭐ JSON output with standard logging |
| Multi-sink management    | ⭐⭐ Uses standard handlers            |
| Console pretty/colour    | ⭐ Limited without extra packages      |
| Log levels and filtering | ⭐⭐⭐ Standard logging levels         |
| Performance              | ⭐⭐ Good                              |
| Dependency footprint     | ⭐⭐ External dependency               |
| Ecosystem support        | ⭐⭐ Moderate adoption                 |
| Effort                   | M                                      |
| Weighted score (max 69)  | 46                                     |

**Why not chosen**: Adds JSON output but does not address console experience well.

#### Option E: AWS Powertools Logger

Use [`Powertools Logger`](https://github.com/aws-powertools/powertools-lambda-python) for AWS Lambda workloads.

| Criteria                 | Score/Notes                   |
| ------------------------ | ----------------------------- |
| Structured logging       | ⭐⭐⭐ Strong JSON output     |
| Multi-sink management    | ⭐⭐ Focused on Lambda output |
| Console pretty/colour    | ⭐ Limited                    |
| Log levels and filtering | ⭐⭐⭐ Strong level support   |
| Performance              | ⭐⭐ Good                     |
| Dependency footprint     | ⭐⭐ External dependency      |
| Ecosystem support        | ⭐⭐ Strong in AWS Lambda     |
| Effort                   | M                             |
| Weighted score (max 69)  | 51                            |

**Why not chosen**: Best for Lambda-only workloads rather than a general baseline.

### Outcome 🏁

Adopt `structlog` as the default logging library for Python. This decision is reversible if structured logging expectations or ecosystem support change.

### Rationale 🧠

Using the weighted criteria, `structlog` scores highest because it is purpose-built for structured logs, integrates well with standard handlers, and supports multi-sink patterns with minimal friction.

## Consequences ⚖️

- Python services should use `structlog` for structured logs.
- AWS Lambda services may use Powertools Logger when AWS-specific features are required.

## Compliance 📏

- New services emit structured JSON logs with level and event fields.
- Multi-sink logging (file and console) is configured where required.

## Notes 🔗

- Tech Radar: `./Tech_Radar.md`

## Actions ✅

- [x] Copilot, 2026-02-08, record the logging decision

## Tags 🏷️

`#observability #maintainability #operability`
