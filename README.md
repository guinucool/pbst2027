# Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents (2026)

This repository contains the artifacts for the paper "Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents".

This repository contains both the evidence collected during our analysis and the code required to reproduce our experiments.

## Table of Contents

- [Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents (2026)](#prompt-like-a-butterfly-sting-like-a-tracker-a-privacy-analysis-of-web-and-mobile-conversational-ai-agents-2026)
  - [Table of Contents](#table-of-contents)
  - [Repository Contents](#repository-contents)
  - [Running code](#running-code)
    - [Requirements](#requirements)
    - [Installing dependencies](#installing-dependencies)
    - [Third-party Service Analysis (S-5)](#third-party-service-analysis-s-5)
    - [Privacy analysis (S-6)](#privacy-analysis-s-6)
    - [Fingerprint analysis (S-6.2.1 -\> JS Fingerprinting Indicators)](#fingerprint-analysis-s-621---js-fingerprinting-indicators)
  - [Interaction Artifacts](#interaction-artifacts)
    - [Labelling](#labelling)
    - [Directory Structure](#directory-structure)

## Repository Contents

The following artifacts can be found:

- `ARTIFACT-APPENDIX.md`: compulsory markdown file for PETS submission containing extra information for reviewers.
- **Data folder:**
  - **Evidence folder** contains actual data from our experiments:
    - `data/evidence/labelled-domains.csv`. A CSV file containing the manually labelled third parties found in each service, along with the account and consent conditions under which they were observed. The "Tracking/Other" column contains the manual label.
    - `data/evidence/fingerprinters.json`. A JSON file containing the fingerprinting APIs found in the actual network captures.
    - `data/evidence/canary-tokens/`. CSVs containing the IP addresses that opened the canary links, both [canary tokens implementation](data/evidence/canary-tokens/Canary-Tokens-Alerts.csv) and [our self-hosted solution](data/evidence/canary-tokens/Canary-Tokens-Alerts-Selfhosted.csv).
  - **Results folder** contains data obtained by executing the scripts on the sample captures.
    - **Expected folder:** contains the results expected from running the scripts.
    - **Tests folder:** where the results from the execution of the scripts are stored.
  - **Samples folder**
    - Sample HAR captures from `grok` to test scripts
- **Code folders**, folders that contain the code for reproducing the experiments:
  - `tpintegration` folder: the Python scripts used to extract and label the third-party domains in the HAR captures.
  - `fingerprint` folder: the Python scripts used to identify JavaScript code related to fingerprinting.
  - `privacyanalysis` folder: the Python scripts used to obtain the personal identifiers in the HAR captures.

> [!WARNING]
> **Actual Network Traffic (ProtocolMonitor, HAR files, etc.) and Application (Android Manifests, etc.) Artifacts will not be publicly available as they contain sensitive data.**

> [!NOTE]
> Analysis was conducted using both the tools provided in this repository and manual inspection.

## Running code

### Requirements

- **Python 3.13.7** (the version the scripts were developed and tested against). Other versions can be used through [`uv`](https://github.com/astral-sh/uv), as shown below.
- All Python dependencies are pinned in `requirements.txt`.
- The commands below assume a Unix-like shell (Linux or macOS).

### Installing dependencies

**Python 3.13.7** — create a virtual environment and install the requirements:

```bash
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

**Other Python versions** — create a virtual environment with the correct Python version (using `uv`) and install the requirements:

```bash
uv venv --python 3.13.7 venv
source ./venv/bin/activate
uv pip install -r requirements.txt
```

### Third-party Service Analysis (S-5)

This code is used to extract and label the third-party domains seen in the HAR captures.

It works in two steps: first extract the domains, and then label them to attribute them to an organization.

**Execution:**

```bash
# Change directory to tpintegration
cd tpintegration
# Extract the 3rd-party domains
python main.py extract
# Label the domains
python main.py label
```

### Privacy analysis (S-6)

> [!NOTE]
> **TO-DO:** transform Jupyter notebooks and normalize dependencies.

**Execution:**

```bash
# Change directory to privacyanalysis
cd privacyanalysis
```

### Fingerprint analysis (S-6.2.1 -> JS Fingerprinting Indicators)

The `fingerprint.py` script reads HAR capture files from a folder and detects fingerprinting API usage based on `fp-inspector_apis.txt`. This file contains the APIs that only appear in fingerprinting scripts according to FP-Inspector. These are the ones marked with an infinity ratio. Source: [FP-Inspector potential fingerprinting APIs](https://github.com/uiowa-irl/FP-Inspector/blob/master/Data/potential_fingerprinting_APIs.md).

> [!NOTE]
> *Disclaimer: the naming in the execution of the test script is different because of the folder structure.*

The output is a JSON file containing all the APIs that have been searched for and the captures where they appear. Example:

```json
{
    "mozSetImageElement": [],
    "magnetometer": [
        "Mistral-Web",
        "Copilot-Web"
    ]
}
```

`mozSetImageElement` was not found anywhere, while `magnetometer` was found in the Mistral and Copilot web experiments.

**Execution:**

```bash
# Change directory to fingerprint
cd fingerprint
# Extract the fingerprinting apis used
python fingerprint.py
```

## Interaction Artifacts

### Labelling

We labelled our experiments such that each condition they represent can be easily identified.

**Account Status (A)**

| Label | Description      |
| ----- | ---------------- |
| A1    | Guest (No login) |
| A2    | Free             |
| A3    | Premium          |

**Privacy Mode (P)**

| Label | Description    |
| ----- | -------------- |
| P1    | Normal Chat    |
| P2    | Incognito Chat |

**Privacy Settings (T)**

| Label | Description               |
| ----- | ------------------------- |
| T1    | Default Privacy Settings  |
| T2    | Minimum Privacy Settings  |
| T3    | Maximum Privacy Settings  |

**Cookie Consent (C)**

| Label | Description                   |
| ----- | ----------------------------- |
| C0    | No Consent Banner             |
| C1    | Ignore Banner                 |
| C2    | Reject Non-Essential Cookies  |
| C3    | Accept Non-Essential Cookies  |

**Share (S)**

| Label | Description             |
| ----- | ----------------------- |
| S1    | Chat was not shared     |
| S2    | Chat was shared         |

**Interaction Phase (I)**

| Label | Description          |
| ----- | -------------------- |
| I1    | Regular Interaction  |
| I2    | Load shared chat     |

### Directory Structure

The collected artifacts are organized using the following directory structure:

```text
WEB/
|-----LLM1/
|     |-----LLM1-AX-PX-TX-CX-SX-YYYYMMDD/
|     |     |-----IX
|     |     |     |-----xxx.har
|     |     |     |-----ProtocolMonitorxxx.json
...   ...   ...   ...
```

The condition codes are combined in the folder name, and the interaction phase is a subfolder inside it. For example:

```text
WEB/LLM1/LLM1-A2-P1-T1-C3-S1-20260114/I1/
```

reads as: LLM1, free account (`A2`), normal chat (`P1`), default privacy settings (`T1`), non-essential cookies accepted (`C3`), chat not shared (`S1`), captured on 2026-01-14, regular interaction (`I1`).