# Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents (2026)

This repository contains the artifacts for the paper "Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents".

The following artifacts can be found:

- ARTIFACT-APPENDIX.md: compulsory markdown file for PETS submsion containing extra information for reviewers
- Data folder:
  - Evidence folder
    - A CSV file containing the third parties manually labelled found in each service, along with the account and consent conditions under which they were observed - `data/evidence/labelled-domains.csv`. "Tracking/Other" column contains the manual label.
  - Results folder
    - Expected folder contains the results expected from running the scripts
    - Tests folder: where the results from the execution of the scripts are stored
  - Samples folder
    - Sample har captures from grok to test scripts
- Code folders, folders that contain the code for reproducing the experiments:
  - tpintegration folder: the python used scripts to extract and label the third party domains in the HAR captures
  - fingerprint folder: the python used scripts to identify javascript code related to fingerprinting
  - privacy analysis folder: the python used scripts to obatin the personal identifiers in the HAR captures

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

### Fingerprint analysis (S-6.2.1 -> JS Fingerprinting Indicators)

TO-DO: Adapt scripts to samples and make them work
