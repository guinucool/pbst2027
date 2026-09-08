# Artifact Appendix

Paper title: **Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents**

Requested Badge(s):
  - [x] **Available**
  - [x] **Functional**
  - [x] **Reproduced**

## Description

Article: "Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents" Oliveira et al.
The artifacts are formed by the following:

Bibtex:

```bibtex
@inproceedings{oliveira2026prompt,
  author  = {Oliveira, Guilherme and
             Sanchez, Miguel and
             De Santa Olalla G{\'o}mez, Juan Manuel and
             Serna, Roi S. and
             Jackevicius, Tautvydas and
             Garcia-Herrero, Jorge and
             Girish, Aniketh and
             Suarez-Tangil, Guillermo and
             Vallina-Rodriguez, Narseo},
  title   = {Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis
             of Web and Mobile Conversational AI Agents},
  booktitle = {Proceedings on Privacy Enhancing Technologies (PoPETs)},
  year    = {2026},
}
```

This repository contains both the evidence collected during our analysis and the code required to reproduce our experiments.

The following artifacts can be found:

- ARTIFACT-APPENDIX.md: compulsory markdown file for PETS submsion containing extra information for reviewers.
- Data folder:
  - Evidence folder contains actual data from our experiments:
    - `data/evidence/labelled-domains.csv`. A CSV file containing the third parties manually labelled found in each service, along with the account and consent conditions under which they were observed. "Tracking/Other" column contains the manual label.
    - `data/evidence/fingerprinters.json`. A json file containing the found fingerprinting APIS in the actual network captures.
    - `data/"canary-tokens"/`. CSVs containing the IP directions that opened the canary links.
  - Results folder contains data obtained by executing the scripts on the sample captures.
    - Expected folder: contains the results expected from running the scripts.
    - Tests folder: where the results from the execution of the scripts are stored.
  - Samples folder
    - Sample har captures from grok to test scripts
- Code folders, folders that contain the code for reproducing the experiments:
  - tpintegration folder: the python used scripts to extract and label the third party domains in the HAR captures.
  - fingerprint folder: the python used scripts to identify javascript code related to fingerprinting.
  - privacy analysis folder: the python used scripts to obatin the personal identifiers in the HAR captures.

### Security/Privacy Issues and Ethical Concerns

The uploaded artifacts pose no risk to the security or privacy of the evaluator's machine, and raise no ethical concerns. Executing them does not require disabling any security mechanisms.

The full interaction captures cannot be released, as they contain private data collected during our experiments. We instead provide a representative subset of sample captures to run the experiments.

## Basic Requirements

Our artifacts have no special hardware or software requirements. Any commodity laptop with Python and an internet connection is sufficient to reproduce our analyses.

### Hardware Requirements

No specialized hardware is required. The analysis scripts run on any commodity x86-64 or ARM laptop; we developed and tested them on a machine x86-64 with 16 GB of RAM. **GUI-CHECK**.

### Software Requirements

1. OS agnstic (preferably Linux or similar), tests performed on Linux 7.2.2-arch1-1 and **GUI-FILL-IN**.
2. OS packages: only python needed.
3. Artifact packaging: python virtual environment.
4. Programming language version: Python 3.13.7 .
5. List of packages needed in [requirements.txt](./requirements.txt) .
6. No machine learning models needed.
7. No aditional datasets needed.

### Estimated Time and Storage Consumption

- **Estimated time:** less than 15 minutes
- **Storage consumption:** approximately 600 MiB

## Environment

Setting up the environment requires only cloning the repository, ensuring the
correct Python version is available, and installing the dependencies listed in
`requirements.txt` inside a virtual environment.

### Accessibility

**GUI-CHECK**
The artifacts are publicly available on GitHub:
[https://github.com/guinucool/pbst2026](https://github.com/guinucool/pbst2026)

### Set Up the Environment

**GUI-CHECK**
If Python 3.13.7 is already installed, create a virtual environment and install
the requirements:

```bash
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Otherwise, `uv` can be used to provision the required Python version alongside
the virtual environment:

```bash
uv venv --python 3.13.7 venv
source ./venv/bin/activate
uv pip install -r requirements.txt
```

Describe the expected results where it makes sense to do so.

### Testing the Environment

With the virtual environment active (see above), run the test script from the
root of the cloned repository:

```bash
# If not already activated
source ./venv/bin/activate
python test.py 
```

The script verifies that all dependencies resolve, that the provided sample
captures are present and parseable, and that the analysis pipeline runs
end to end on a single capture. Expected output:

```bash
Python 3.13      OK
Dependencies     OK
Sample data      OK

Environment is ready.
```

Completion takes under one minute. Any `FAILED` line indicates a setup problem;

## Artifact Evaluation

### Main Results and Claims

#### Main Result 1: Conversational AI services integrate third-party tracking, analytics, advertising, and attribution infrastructures across their web and mobile clients

We showed that the tracking infrastructure of the web and mobile ecosystems—pixels, SDKs, persistent identifiers, and server-side forwarding—has been carried into conversational AI clients largely unchanged. Across the providers we studied, we observed contacts with domains belonging to advertising, analytics, and attribution organizations, present in both the web and mobile clients of the same service. This is supported by [Experiment 1](#experiment-1-third-party-service-analysis), in which we extract the third-party domains contacted in the sample captures and attribute them to the organizations operating them. Our manually labeled evidence found in the actual captures can be found in the [labeled domains CSV](data/evidence/labelled-domains.csv).

#### Main Result 2: Conversation-derived artifacts and user information are exposed by conversational AI services, either to third-party entities or through publicly accessible resources

We observed conversational AI services exposing conversation artifacts such as prompts, generated titles, and permalinks to third parties. These disclosures frequently occur alongside persistent identifiers, including advertising IDs, hashed email addresses, and tracking cookies, enabling conversations to be linked to long-term user profiles. We further found that cookie consent and subscription tier provide limited protection, while permissive sharing defaults leave conversation permalinks publicly accessible. This is supported by [Experiment 2](#experiment-2-privacy-analysis), in which we inspect the payloads of the requests directed at the third parties identified in Experiment 1 and recover the conversation artifacts and identifiers they carry.

#### Main Result 3: Conversational AI services have the ability to fingerprint web browsers and probabilistically identify users

Following prior work findings, we search for APIs commonly associated with browser fingerprinting across most providers. We find such APIs invoked in scripts served by all providers. Although the presence of these APIs alone does not establish active fingerprinting, it indicates that providers possess the technical capability to derive high-entropy device characteristics. This is supported by [Experiment 3](#experiment-3-fingerprint-analysis), which detects the presence of these APIs in the scripts served to the web clients.

#### Main Result 4: Using canary tokens, we confirmed that shared conversations are subsequently accessed from distributed third-party infrastructure

We embedded canary tokens in conversations shared through the providers' native sharing features and recorded the accesses they triggered. Beyond the accesses attributable to the recipient, we observed retrievals originating from hosting and cloud infrastructure unrelated to the recipient, indicating that shared conversations are collected by third parties after publication. This result is not reproducible from the uploaded artifacts, as it depends on live infrastructure and on tokens tied to our own accounts; the recorded accesses are provided as evidence in data/evidence/canary-tokens both [cannary tokens implementation](data/evidence/canary-tokens/Canary-Tokens-Alerts.csv)  and [our self hosted solution](data/evidence/canary-tokens/Canary-Tokens-Alerts-Selfhosted.csv).

### Experiments

All experiment outputs are written to `data/results/tests`, so that a reviewer's results can be compared against the evidence in `data/evidence/` without overwriting it.

#### Experiment 1: Third-party Service Analysis

- Time: 5 human-minutes + 5 compute-minutes
- Supports: [Main Result 1](#main-result-1-conversational-ai-services-integrate-third-party-tracking-analytics-advertising-and-attribution-infrastructures-across-their-web-and-mobile-clients) (S-5)

This experiment extracts and labels the third-party domains seen in the HAR captures. It works in two steps: first the domains are extracted from the captures, then they are labeled to attribute them to an organization.

```bash
# Change directory to tpintegration
cd tpintegration
# Extract the 3rd-party domains
python main.py extract
# Label the domains
python main.py label
```

The labeled domains are written to `data/results/tests`. Each domain is attributed to the organization operating it and to the clients in which it was observed. The data from the real captures manually processed can be found in [data/evidence/labelled-domains.csv](data/evidence/labelled-domains.csv).

#### Experiment 2: Privacy Analysis

- Time: 5 human-minutes + 5 compute-minutes
- Supports: [Main Result 2](#main-result-2-conversation-derived-artifacts-and-user-information-are-exposed-by-conversational-ai-services-either-to-third-party-entities-or-through-publicly-accessible-resources) (S-6)

This experiment takes the captures filtered to the third parties identified in Experiment 1 and inspects the request payloads for conversation artifacts—prompts, generated titles, and permalinks—and for the persistent identifiers accompanying them.

```bash
# Change directory to privacyanalysis
cd privacyanalysis
```

The recovered artifacts and identifiers are written to `data/results/tests`, grouped by client and by recipient organization.

#### Experiment 3: Fingerprint Analysis

- Time: 5 human-minutes + 5 compute-minutes
- Supports: [Main Result 3](#main-result-3-conversational-ai-services-have-the-ability-to-fingerprint-web-browsers-and-probabilistically-identify-users) (S-6.2.1, JS Fingerprinting Indicators)

The `fingerprint.py` script reads the HAR capture files from a folder and detects fingerprinting API usage based on `fp-inspector_apis.txt`. This file contains the APIs that appear only in fingerprinting scripts according to FP-Inspector, i.e. those marked with an infinity ratio. Source: [FP-Inspector potential fingerprinting APIs](https://github.com/uiowa-irl/FP-Inspector/blob/master/Data/potential_fingerprinting_APIs.md).

*Disclaimer: the naming in the execution of the test script differs from the above because of the folder structure.*

```bash
# Change directory to fingerprint
cd fingerprint
# Extract the fingerprinting apis used
python fingerprint.py
```

The output is a JSON file in `data/results/tests` containing every API searched for and the captures in which it appears. For example:

```json
{
  "mozSetImageElement": [],
  "magnetometer": [
    "Mistral-Web",
    "Copilot-Web"
  ]
}
```

Here `mozSetImageElement` was not found anywhere, while `magnetometer` was found in the Mistral and Copilot web experiments.

## Limitations

Two parts of our methodology are not reproducible from the provided artifacts.

**Traffic collection.** The captures analysed in the paper cannot be released, as they were produced by interacting with the providers' clients from accounts we control and contain personal data, authentication material, and paid-subscription state. We instead ship a representative subset of sanitised captures, which the analysis scripts run over unmodified. Re-collecting equivalent captures would require an instrumented browser and mobile device, accounts on each provider, active subscriptions for the tiers we compared — and, because the providers change their clients and third-party integrations continuously, captures taken today would not match ours in any case. The collection step is therefore documented in the paper but out of scope for the artifact.

**Manual inspection.** Several results depend on manual analysis that the scripts support but do not replace. Attributing third-party domains to the organisations operating them requires manual review, as does identifying conversation artifacts and persistent identifiers inside request payloads, where encodings, hashing, and non-standard field names prevent reliable automatic detection. The scripts extract and group the candidates; the labelling itself was done by hand and is provided as evidence in `data/evidence/` so that anyone can inspect our decisions.

**Main Result 4** is not reproducible for the reasons given above: the canary tokens are bound to conversations shared from our own accounts, and the accesses they recorded cannot be regenerated.

## Notes on Reusability

Our analysis pipelines are not specific to the providers we studied. All three operate on standard HAR captures and are unaware of which service produced them, so adding a provider — or a new client of an existing provider — requires only dropping additional captures into the input folder and re-running the scripts. The same applies to studying a different application domain: any web or mobile client whose traffic can be captured as HAR can be analysed without modifying the code.

Individual components can be replaced independently:

- The third-party labelling in `tpintegration` is driven by an external mapping of domains to organisations, which can be extended or swapped for another attribution list.
- The fingerprinting detection in `fingerprint` reads its API list from `fp-inspector_apis.txt`. Substituting a different list — a broader FP-Inspector selection, or APIs associated with another behaviour of interest — changes what the script looks for without touching the script itself.
- The payload inspection in `privacyanalysis` takes the third parties identified upstream as input, so it can be pointed at any set of recipients rather than the ones we selected.
Researchers wanting to reuse the artifact as a measurement framework would need to supply their own collection step, for the reasons set out under Limitations. The analysis side, which is where most of our engineering effort went, is reusable as provided.
