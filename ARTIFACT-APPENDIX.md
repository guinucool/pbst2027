# Artifact Appendix

Paper title: **Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents**

Requested Badge(s):
  - [x] **Available**
  - [x] **Functional**
  - [x] **Reproduced**

## Description

Artifacts for the article "Prompt like a Butterfly, Sting like a Tracker: A
Privacy Analysis of Web and Mobile Conversational AI Agents" (Oliveira et al.).

Bibtex:

```bibtex
@inproceedings{oliveira2027prompt,
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
  year    = {2027},
}
```

This repository contains both the evidence collected during our analysis and the
code required to reproduce our experiments.

The following artifacts can be found:

- `ARTIFACT-APPENDIX.md`: compulsory Markdown file for the PoPETs submission,
  containing extra information for reviewers.
- `data/`:
  - `data/evidence/` contains the actual data from our experiments:
    - `data/evidence/labelled-domains.csv`: a CSV file containing the manually
      labeled third parties found in each service, along with the account and
      consent conditions under which they were observed. The "Tracking/Other"
      column contains the manual label.
    - `data/evidence/fingerprinters.json`: a JSON file containing the
      fingerprinting APIs found in the actual network captures.
    - `data/evidence/canary-tokens/`: CSV files containing the IP addresses that
      opened the canary links.
  - `data/results/` contains the data obtained by executing the scripts on the
    sample captures:
    - `data/results/expected/`: the results expected from running the scripts.
    - `data/results/tests/`: where the results of the execution of the scripts
      are stored.
  - `data/samples/`: sample HAR captures from Grok, used to test the scripts.
- Code folders, which contain the code for reproducing the experiments:
  - `tpintegration/`: the Python scripts used to extract and label the
    third-party domains in the HAR captures.
  - `fingerprint/`: the Python scripts used to identify JavaScript code related
    to fingerprinting.
  - `privacyanalysis/`: the Python scripts used to obtain the personal
    identifiers in the HAR captures.

### Security/Privacy Issues and Ethical Concerns

The uploaded artifacts pose no risk to the security or privacy of the
evaluator's machine, and raise no ethical concerns. Executing them does not
require disabling any security mechanism.

The full interaction captures cannot be released, as they contain private data
collected during our experiments. We instead provide a representative subset of
sample captures with which to run the experiments.

> [!IMPORTANT]
> **Check ROI**: I just want to know if it fits here. Maybe we can put it somewhere
> else, but I think it is important to mencion.
>
> These sample captures were created specifically to run the experiments and were
> collected long after those used in the paper. Consequently, results obtained from
> them should not be considered representative of the findings reported in the main
> study.

## Basic Requirements

Our artifacts have no special hardware or software requirements. Any commodity
laptop with Python and an internet connection is sufficient to reproduce our
analyses.

### Hardware Requirements

No specialized hardware is required. The analysis scripts run on any commodity
x86-64 or ARM laptop; we developed and tested them on an x86-64 machine with
16 GB of RAM.

### Software Requirements

1. OS-agnostic (Linux or similar preferred); tested on Arch Linux
   (kernel 7.2.2-arch1-1) and on Ubuntu (kernel 6.8.0-138-generic).
2. OS packages: only Python is needed.
3. Artifact packaging: Python virtual environment.
4. Programming language version: Python 3.13.7.
5. List of packages needed in [requirements.txt](./requirements.txt).
6. No machine learning models needed.
7. No additional datasets needed.

### Estimated Time and Storage Consumption

> [!IMPORTANT]
> **FROM GUI**: I will run all the experiments and calculate the actual size.

- **Estimated time:** less than 30 minutes
- **Storage consumption:** approximately 600 MiB

## Environment

Setting up the environment requires only cloning the repository, ensuring the
correct Python version is available, and installing the dependencies listed in
`requirements.txt` inside a virtual environment.

### Accessibility

> [!IMPORTANT]
> **TODO (GUI-CHECK):** confirm the repository URL is public and, if a stable
> archival copy (e.g. a Zenodo DOI or a tagged commit) is required for the
> Available badge, add it here. (I will leave this for last) Maybe change the repo for 2027 before submission? Careful to change everywhere in the doc

The artifacts are publicly available on GitHub:
[https://github.com/guinucool/pbst2026](https://github.com/guinucool/pbst2026)

### Set Up the Environment

First, clone the repository and move to its root directory:

```bash
git clone git@github.com:guinucool/pbst2026.git
cd pbst2026
```

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

```text
Python 3.13      OK
Dependencies     OK
Sample data      OK

Environment is ready.
```

Completion takes under one minute. Any `FAILED` line indicates a setup problem.

## Artifact Evaluation

### Main Results and Claims

#### Main Result 1: Conversational AI services integrate third-party tracking, analytics, advertising, and attribution infrastructures across their web and mobile clients

We showed that the tracking infrastructure of the web and mobile ecosystems—pixels, SDKs, persistent identifiers, and server-side forwarding—has been carried into conversational AI clients largely unchanged. Across the providers we studied, we observed contacts with domains belonging to advertising, analytics, and attribution organizations, present in both the web and mobile clients of the same service. This is supported by [Experiment 1](#experiment-1-third-party-service-analysis), in which we extract the third-party domains contacted in the sample captures and attribute them to the organizations operating them. Our manually labeled evidence found in the actual captures can be found in the [labeled domains CSV](data/evidence/labelled-domains.csv).

#### Main Result 2: Conversation-derived artifacts and user information are exposed by conversational AI services, either to third-party entities or through publicly accessible resources

We observed conversational AI services exposing conversation artifacts such as prompts, generated titles, and permalinks to third parties. These disclosures frequently occur alongside persistent identifiers, including advertising IDs, hashed email addresses, and tracking cookies, enabling conversations to be linked to long-term user profiles. We further found that cookie consent and subscription tier provide limited protection, while permissive sharing defaults leave conversation permalinks publicly accessible. This is supported by [Experiment 2](#experiment-2-privacy-analysis), in which we inspect the payloads of the requests directed at the third parties identified in Experiment 1 and recover the conversation artifacts and identifiers they carry.

#### Main Result 3: Conversational AI services have the ability to fingerprint web browsers and probabilistically identify users

Following the findings of prior work, we search for APIs commonly associated with browser fingerprinting across the providers we studied. We find such APIs invoked in scripts served by all of them. Although the presence of these APIs alone does not establish active fingerprinting, it indicates that providers possess the technical capability to derive high-entropy device characteristics. This is supported by [Experiment 3](#experiment-3-fingerprint-analysis), which detects the presence of these APIs in the scripts served to the web clients.

#### Main Result 4: Using canary tokens, we confirmed that shared conversations are subsequently accessed from distributed third-party infrastructure

We embedded canary tokens in conversations shared through the providers' native sharing features and recorded the accesses they triggered. Beyond the accesses attributable to the recipient, we observed retrievals originating from hosting and cloud infrastructure unrelated to the recipient, indicating that shared conversations are collected by third parties after publication. This result is not reproducible from the uploaded artifacts, as it depends on live infrastructure and on tokens tied to our own accounts; the recorded accesses are provided as evidence in `data/evidence/canary-tokens/`, both for the [Canarytokens-based deployment](data/evidence/canary-tokens/Canary-Tokens-Alerts.csv) and for [our self-hosted solution](data/evidence/canary-tokens/Canary-Tokens-Alerts-Selfhosted.csv).

### Experiments

All experiment outputs are written to `data/results/tests`, so that a reviewer's
results can be compared against the expected outcomes in `data/results/expected/` without
overwriting it.

Each script must be run from inside its own folder. The command blocks below
therefore assume the shell starts at the root of the cloned repository, with the
virtual environment active, and change into the relevant folder first.

#### Experiment 1: Third-party Service Analysis

- Time: 2 human-minutes + 20 compute-seconds
- Supports: [Main Result 1](#main-result-1-conversational-ai-services-integrate-third-party-tracking-analytics-advertising-and-attribution-infrastructures-across-their-web-and-mobile-clients) (§5)

This experiment extracts third-party domains from the HAR captures and attributes them to organizations using a manual mapping. It runs in two stages: domain extraction followed by labeling.

The extraction stage generates `tp_classification.csv` to facilitate manual classification. We provide a completed mapping for the sample captures in `tp_labelled.csv`, which is used during the labeling stage. Alternatively, `tp_classification.csv` can be used to create a custom `tp_labelled.csv` mapping.

```bash
# Change directory to tpintegration
cd tpintegration
# Extract the 3rd-party domains
python main.py extract
# Label the domains
python main.py label
```

The labeled domains are written to `data/results/tests/tp_final.csv`. Each domain is
attributed to the organization operating it and to the clients in which it was
observed. The data from the real captures, processed manually, can be found in
[data/evidence/labelled-domains.csv](data/evidence/labelled-domains.csv).

#### Experiment 2: Privacy Analysis

- Time: 20 human-seconds + 25 compute-seconds
- Supports: [Main Result 2](#main-result-2-conversation-derived-artifacts-and-user-information-are-exposed-by-conversational-ai-services-either-to-third-party-entities-or-through-publicly-accessible-resources) (§6)

This experiment analyzes requests to the third parties identified in Experiment 1 for disclosures of conversation artifacts—such as prompts, generated titles, and permalinks—and persistent identifiers.

It proceeds in two stages. First, it extracts automatically detectable identifiers, such as tracking cookies and hashes. It then combines them with the manually provided identifiers and conversation artifacts stored in `info.val` within each sample session folder to identify data disclosed to third parties.

```bash
# Change directory to privacyanalysis
cd privacyanalysis
# Collect predictable identifiers
python main.py collect
# Inspect for dissemination
python main.py hunt
```

The recovered artifacts and identifiers are written to `data/results/tests/pa_final.csv`,
grouped by client and by recipient organization.

#### Experiment 3: Fingerprint Analysis

- Time: 2 human-minutes + 2 compute-minutes
- Supports: [Main Result 3](#main-result-3-conversational-ai-services-have-the-ability-to-fingerprint-web-browsers-and-probabilistically-identify-users) (§6.2.1, JS Fingerprinting Indicators)

The `fingerprint.py` script reads the HAR capture files from a folder and
detects fingerprinting API usage based on `fp-inspector_apis.txt`. This file
contains the APIs that appear only in fingerprinting scripts according to
FP-Inspector, i.e. those marked with an infinity ratio. Source:
[FP-Inspector potential fingerprinting APIs](https://github.com/uiowa-irl/FP-Inspector/blob/master/Data/potential_fingerprinting_APIs.md).

*Disclaimer: the naming in the execution of the test script differs from the
above because of the folder structure.*

```bash
# Change directory to fingerprint
cd fingerprint
# Extract the fingerprinting APIs used
python fingerprint.py
```

The output is a JSON file in `data/results/tests` containing every API searched
for and the captures in which it appears. For example:

```json
{
  "mozSetImageElement": [],
  "magnetometer": [
    "Mistral-Web",
    "Copilot-Web"
  ]
}
```

Here, `mozSetImageElement` was not found anywhere, while `magnetometer` was
found in the Mistral and Copilot web experiments.

## Limitations

Two parts of our methodology are not reproducible from the provided artifacts.

**Traffic collection.** The captures analyzed in the paper cannot be released, as they were produced by interacting with the providers' clients from accounts we control and contain personal data, authentication material, and paid-subscription state. We instead ship a representative subset of sanitized captures, which the analysis scripts run over unmodified. Re-collecting equivalent captures would require an instrumented browser and mobile device, accounts on each provider, and active subscriptions for the tiers we compared — and, because the providers change their clients and third-party integrations continuously, captures taken today would not match ours in any case. The collection step is therefore documented in the paper but out of scope for the artifact. For the same reasons, **Main Result 4** cannot be reproduced: the canary tokens are bound to conversations shared from our own accounts, and the accesses they recorded cannot be regenerated. They are provided as evidence instead.

**Manual inspection.** Several results depend on manual analysis that the scripts support but do not replace. Attributing third-party domains to the organizations operating them requires manual review, as does identifying conversation artifacts and persistent identifiers inside request payloads, where encodings, hashing, and non-standard field names prevent reliable automatic detection. The scripts extract and group the candidates; the labeling itself was done by hand and is provided as evidence in `data/evidence/` so that anyone can inspect our decisions.

## Notes on Reusability

Our analysis pipelines are not specific to the providers we studied. All three
operate on standard HAR captures and are unaware of which service produced them,
so adding a provider — or a new client of an existing provider — requires only
dropping additional captures into the input folder and re-running the scripts.
The same applies to studying a different application domain: any web or mobile
client whose traffic can be captured as HAR can be analyzed without modifying
the code.

> [!IMPORTANT]
> **Check ROI:** I made some changes, they are in bold **previous | new**
> that I feel are more accurate. Keep or delete as you feel.

Individual components can be replaced independently:

- The third-party labeling in `tpintegration` is driven by **an external | a manual** mapping
  of domains to organizations, which can be extended or swapped for another
  attribution **list | criteria**.
- The fingerprinting detection in `fingerprint` reads its API list from
  `fp-inspector_apis.txt`. Substituting a different list — a broader
  FP-Inspector selection, or APIs associated with another behavior of interest —
  changes what the script looks for without touching the script itself.
- The payload inspection in `privacyanalysis` takes the third parties identified
  upstream, **as well as manually selected persitent identifiers (`info.val`)**,
  as input, so it can be pointed at any set of recipients **and values** rather than
  the ones we selected.

Researchers wanting to reuse the artifact as a measurement framework would need
to supply their own collection step, for the reasons set out under Limitations.
The analysis side, which is where most of our engineering effort went, is
reusable as provided.