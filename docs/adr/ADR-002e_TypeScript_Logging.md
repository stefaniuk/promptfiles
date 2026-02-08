# ADR-002e: TypeScript logging 🧾

> |              |                                                 |
> | ------------ | ----------------------------------------------- |
> | Date         | `2026-02-08` when the decision was last updated |
> | Status       | `Accepted`                                      |
> | Significance | `Quality attributes, Operations`                |

---

- [ADR-002e: TypeScript logging 🧾](#adr-002e-typescript-logging-)
  - [Context 🧭](#context-)
  - [Decision ✅](#decision-)
    - [Assumptions 🧩](#assumptions-)
    - [Drivers 🎯](#drivers-)
    - [Options 🔀](#options-)
      - [Option A: winston (Selected) ✅](#option-a-winston-selected-)
      - [Option B: pino](#option-b-pino)
      - [Option C: log4js](#option-c-log4js)
      - [Option D: bunyan (deprecated)](#option-d-bunyan-deprecated)
      - [Option E: AWS Powertools Logger](#option-e-aws-powertools-logger)
    - [Outcome 🏁](#outcome-)
    - [Rationale 🧠](#rationale-)
  - [Consequences ⚖️](#consequences-️)
  - [Compliance 📏](#compliance-)
  - [Notes 🔗](#notes-)
  - [Actions ✅](#actions-)
  - [Tags 🏷️](#tags-️)

## Context 🧭

The TypeScript tech stack needs a default logging library that supports structured logs, multi-sink output, and good local console readability.

## Decision ✅

### Assumptions 🧩

- Node.js 24.13.0 (LTS) is the baseline runtime.
- TypeScript 5.9 is the baseline language version.
- Structured JSON logs are required for services.

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

#### Option A: winston (Selected) ✅

Use [`winston`](https://github.com/winstonjs/winston) with JSON file transport and console transport for local output.

| Criteria                 | Score/Notes                       |
| ------------------------ | --------------------------------- |
| Structured logging       | ⭐⭐⭐ JSON formats supported     |
| Multi-sink management    | ⭐⭐⭐ Multiple transports        |
| Console pretty/colour    | ⭐⭐ Colourised console transport |
| Log levels and filtering | ⭐⭐⭐ Strong level support       |
| Performance              | ⭐⭐ Good for most services       |
| Dependency footprint     | ⭐⭐ External dependency          |
| Ecosystem support        | ⭐⭐⭐ Widely used                |
| Effort                   | M                                 |
| Weighted score (max 69)  | 61                                |

#### Option B: pino

Use [`pino`](https://github.com/pinojs/pino) with transports and `pino-pretty` for console output.

| Criteria                 | Score/Notes                    |
| ------------------------ | ------------------------------ |
| Structured logging       | ⭐⭐⭐ JSON by default         |
| Multi-sink management    | ⭐⭐ Transports required       |
| Console pretty/colour    | ⭐⭐ `pino-pretty` adds colour |
| Log levels and filtering | ⭐⭐⭐ Strong level support    |
| Performance              | ⭐⭐⭐ Very fast               |
| Dependency footprint     | ⭐⭐ External dependency       |
| Ecosystem support        | ⭐⭐⭐ Strong adoption         |
| Effort                   | M                              |
| Weighted score (max 69)  | 59                             |

**Why not chosen**: Excellent performance, but needs extra setup for multi-sink and pretty output.

#### Option C: log4js

Use [`log4js`](https://github.com/log4js-node/log4js-node) with appenders for file and console.

| Criteria                 | Score/Notes                    |
| ------------------------ | ------------------------------ |
| Structured logging       | ⭐⭐ JSON support with layouts |
| Multi-sink management    | ⭐⭐⭐ Strong appender system  |
| Console pretty/colour    | ⭐⭐ Supports colour layouts   |
| Log levels and filtering | ⭐⭐⭐ Strong level support    |
| Performance              | ⭐⭐ Reasonable                |
| Dependency footprint     | ⭐⭐ External dependency       |
| Ecosystem support        | ⭐⭐ Moderate adoption         |
| Effort                   | M                              |
| Weighted score (max 69)  | 54                             |

**Why not chosen**: Good feature set, but less standard than winston.

#### Option D: bunyan (deprecated)

Use [`bunyan`](https://github.com/trentm/node-bunyan) for JSON logging.

| Criteria                 | Score/Notes                 |
| ------------------------ | --------------------------- |
| Structured logging       | ⭐⭐⭐ JSON-first           |
| Multi-sink management    | ⭐⭐ Streams and pipes      |
| Console pretty/colour    | ⭐⭐ Requires `bunyan` CLI  |
| Log levels and filtering | ⭐⭐⭐ Strong level support |
| Performance              | ⭐⭐ Good                   |
| Dependency footprint     | ⭐⭐ External dependency    |
| Ecosystem support        | ⭐ Low, deprecated          |
| Effort                   | M                           |
| Weighted score (max 69)  | 53                          |

**Why not chosen**: Deprecated and losing ecosystem support.

#### Option E: AWS Powertools Logger

Use [`Powertools Logger`](https://github.com/aws-powertools/powertools-lambda-typescript) for AWS Lambda workloads.

| Criteria                 | Score/Notes                   |
| ------------------------ | ----------------------------- |
| Structured logging       | ⭐⭐⭐ Strong JSON output     |
| Multi-sink management    | ⭐⭐ Focused on Lambda output |
| Console pretty/colour    | ⭐ Limited                    |
| Log levels and filtering | ⭐⭐⭐ Strong level support   |
| Performance              | ⭐⭐ Good                     |
| Dependency footprint     | ⭐⭐ External dependency      |
| Ecosystem support        | ⭐⭐ Strong for Lambda        |
| Effort                   | M                             |
| Weighted score (max 69)  | 51                            |

**Why not chosen**: Best for Lambda-specific workloads rather than the general baseline.

### Outcome 🏁

Adopt `winston` as the default logging library for TypeScript. This decision is reversible if the ecosystem changes.

### Rationale 🧠

Using the weighted criteria, `winston` scores highest because it balances structured logging, multi-sink output, and widespread adoption.

## Consequences ⚖️

- TypeScript services should use winston with JSON file output and console transport.
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
