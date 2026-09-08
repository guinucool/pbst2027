# Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents (2026)

This repository contains the artifacts for the paper "Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents".

This repository contains both the evidence collected during our analysis and the code required to reproduce our experiments.

The following artifacts can be found:

- ARTIFACT-APPENDIX.md: compulsory markdown file for PETS submsion containing extra information for reviewers.
- Data folder:
  - Evidence folder contains actual data from our experiments:
    - `data/evidence/labelled-domains.csv`. A CSV file containing the third parties manually labelled found in each service, along with the account and consent conditions under which they were observed. "Tracking/Other" column contains the manual label.
    - `data/evidence/fingerprinters.json`. A json file containing the found fingerprinting APIS in the actual network captures.
    - `data/"canary-tokens"/`. CSVs containing the IP directions that opened the canary links, both [cannary tokens implementation](data/evidence/canary-tokens/Canary-Tokens-Alerts.csv)  and [our self hosted solution](data/evidence/canary-tokens/Canary-Tokens-Alerts-Selfhosted.csv).
  - Results folder contains data obtained by executing the scripts on the sample captures.
    - Expected folder: contains the results expected from running the scripts.
    - Tests folder: where the results from the execution of the scripts are stored.
  - Samples folder
    - Sample har captures from grok to test scripts
- Code folders, folders that contain the code for reproducing the experiments:
  - tpintegration folder: the python used scripts to extract and label the third party domains in the HAR captures.
  - fingerprint folder: the python used scripts to identify javascript code related to fingerprinting.
  - privacy analysis folder: the python used scripts to obatin the personal identifiers in the HAR captures.

> **⚠️ Actual Network Traffic (ProtocolMonitor, HAR files, etc...) and Application (Android Manifests, etc...) Artifacts will not be publicly available as they contain sensitive data**

> Analysis was conducted using both the tools provided in this repository and manual inspection.

## Running code

### Installing dependencies

- Python 3.13.7: Create virtual environment and install requirements

```bash
python -m venv venv 
source ./venv/bin/activate 
pip install -r requirements.txt
```

- Other python version: Create virtual environment with correct python version (using uv) and install requirements

```bash
uv venv --python 3.13.7 venv
source ./venv/bin/activate
uv pip install -r requirements.txt
```

### Third-party Service Analysis (S-5)

This code is used to extract and label the third-party domains seen in the har captures.

It works in two steps, first extract the domains and then label them to attribute them to an organization.

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

TO-DO: transform jupyter notebooks and normalize dependencies

**Execution:**

```bash
# Change directory to privacyanalysis
cd privacyanalysis
```

### Fingerprint analysis (S-6.2.1 -> JS Fingerprinting Indicators)

The `fingerprint.py` script reads HAR capture files from a folder and detects fingerprinting API usage based on `fp-inspector_apis.txt`. This file contains the apis that only appear in in fingerprinting scripts according to fp-inspector. This are the ones marked with infinity ratio. Source: [FPInspector potentioal fingerprinting apis](https://github.com/uiowa-irl/FP-Inspector/blob/master/Data/potential_fingerprinting_APIs.md). *Disclaimer: the naming in the execution of the test script is different because of folder structure*

The output is a json file containing all the APIs that have been searched for and the captures where it appear. Example:

```json
{
 "mozSetImageElement": [],
    "magnetometer": [
        "Mistral-Web",
        "Copilot-Web"
    ],
}
```

mozSetImageElement was not found anywhere, while magnetometer was found in Mistral and Copilot web experiments

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

| Label | Description |
|-------|-------------|
| A1    | Guest (No login) |
| A2    | Free |
| A3    | Premium |

**Privacy Mode (P)**

| Label | Description |
|-------|-------------|
| P1    | Normal Chat |
| P2    | Incognito Chat |

**Privacy Settings (T)**

| Label | Description |
|-------|-------------|
| T1    | Default Privacy Settings |
| T2    | Minimum Privacy Settings |
| T3    | Maximum Privacy Settings |

**Cookie Consent (C)**

| Label | Description |
|-------|-------------|
| C0    | No Consent Banner |
| C1    | Ignore Banner |
| C2    | Reject Non-Essential Cookies |
| C3    | Accept Non-Essential Cookies |

**Share (S)**

| Label | Description |
|-------|-------------|
| S1    | Chat was not shared |
| S2    | Chat was shared |

**Interaction Phase (I)**

| Label | Description |
|-------|-------------|
| I1    | Regular Interaction |
| I2    | Load shared chat |

The collected artifacts are organized using the following directory structure:

```
WEB/
|-----LLM1/
|     |-----LLM1-AX-PX-TX-CX-SX-YYYYMMDD/
|     |     |-----IX
|     |     |     |-----xxx.har
|     |     |     |-----ProtocolMonitorxxx.json
...   ...   ...   ...
```
