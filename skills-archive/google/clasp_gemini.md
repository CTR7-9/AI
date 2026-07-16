# Gemini Project Overview: @google/clasp

This document provides a high-level overview of the `@google/clasp` project to guide AI-based development and maintenance.

## Project Purpose

`clasp` is a command-line tool for developing and managing Google Apps Script projects locally. It allows developers to write code in their preferred local environment, use version control (like Git), and then push the code to their Apps Script projects. It also supports managing deployments, versions, and executing functions remotely.

## Tech Stack

-   **Language:** TypeScript
-   **Platform:** Node.js
-   **CLI Framework:** [Commander.js](https://github.com/tj/commander.js)
-   **Key Libraries:**
    -   `googleapis`: To interact with Google APIs (Apps Script, Drive, etc.).
    -   `google-auth-library`: For handling OAuth2 authentication.
    -   `inquirer`: For interactive command-line prompts.
    -   `ora`: For displaying spinners during long-running operations.
-   **Testing:**
    -   **Framework:** Mocha
    -   **Assertions:** Chai
    -   **Mocking:** Nock (for HTTP requests) and `mock-fs` (for filesystem).
-   **Linting & Formatting:** Biome

## Project Structure

```
.
├── src/
│   ├── commands/   # Definitions for each CLI command (e.g., push, pull, login).
│   ├── core/       # Core logic for interacting with APIs and the filesystem.
│   └── auth/       # Authentication-related logic.
├── test/
│   ├── commands/   # Tests for the CLI commands.
│   └── core/       # Tests for the core logic.
│   └── fixtures/   # Mock data and file templates used in tests.
├── build/          # Compiled JavaScript output from TypeScript.
├── package.json    # Project metadata, dependencies, and scripts.
├── tsconfig.json   # TypeScript compiler configuration.
├── biome.json      # Biome linter/formatter configuration.
└── README.md       # Project documentation.
```

(Excerpted from google/clasp/gemini.md)
