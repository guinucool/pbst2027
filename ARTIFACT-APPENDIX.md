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
    - `data/"Canary tokens"/`. CSVs containing the IP directions that opened the canary links.
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

### Testing the Environment (Required for Functional and Reproduced badges)

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

## Artifact Evaluation (Required for Functional and Reproduced badges)

This section should include all the steps required to evaluate your artifact's
functionality and validate your paper's key results and claims. Therefore,
highlight your paper's main results and claims in the first subsection. And
describe the experiments that support your claims in the subsection after that.

### Main Results and Claims

List all your paper's results and claims that are supported by your submitted
artifacts.

#### Main Result 1: Name

Describe the results in 1 to 3 sentences. Mention what the independent and
dependent variables are; independent variables are the ones on the x-axes of
your figures, whereas the dependent ones are on the y-axes. By varying the
independent variable (e.g., file size) in a given manner (e.g., linearly), we
expect to see trends in the dependent variable (e.g., runtime, communication
overhead) vary in another manner (e.g., exponentially). Refer to the related
sections, figures, and/or tables in your paper and reference the experiments
that support this result/claim. See example below.

#### Main Result 2: Example Name

Our paper claims that when varying the file size linearly, the runtime also
increases linearly. This claim is reproducible by executing our
[Experiment 2](#experiment-2-example-name). In this experiment, we change the
file size linearly, from 2KB to 24KB, at intervals of 2KB each, and we show that
the runtime also increases linearly, reaching at most 1ms. We report these
results in "Figure 1a" and "Table 3" (Column 3 or Row 2) of our paper.

### Experiments
List each experiment to execute to reproduce your results. Describe:
 - How to execute it in detailed steps.
 - What the expected result is.
 - How long it takes to execute in human and compute times (approximately).
 - How much space it consumes on disk (approximately) (omit if <10GB).
 - Which claim and results does it support, and how.

#### Experiment 1: Name
- Time: replace with estimate in human-minutes/hours + compute-minutes/hours.
- Storage: replace with estimate for disk space used (omit if <10GB).

Provide a short explanation of the experiment and expected results. Describe
thoroughly the steps to perform the experiment and to collect and organize the
results as expected from your paper (see example below). Use code segments to
simplify the workflow, as follows.

```bash
python3 experiment_1.py
```

#### Experiment 2: Example Name

- Time: 10 human-minutes + 3 compute-hours
- Storage: 20GB

This example experiment reproduces
[Main Result 2: Example Name](#main-result-2-example-name), the following script
will run the simulation automatically with the different parameters specified in
the paper. (You may run the following command from the example Docker image.)

```bash
python3 main.py
```

Results from this example experiment will be aggregated over several iterations
by the script and output directly in raw format along with variances and
standard deviations in the `output-folder/` directory. You will also find there
the plots for "Figure 1a" in `.pdf` format and the table for "Table 3" in `.tex`
format. These can be directly compared to the results reported in the paper, and
should not quantitatively vary by more than 5% from expected results.


## Limitations (Required for Functional and Reproduced badges)

Describe which steps, experiments, results, graphs, tables, etc. are _not
reproducible_ with the provided artifact. Explain why this is not
included/possible and argue why the artifact should _still_ be evaluated for the
respective badges.

## Notes on Reusability (Encouraged for all badges)

First, this section might not apply to your artifacts. Describe how your
artifact can be used beyond your research paper, e.g., as a general framework.
The overall goal of artifact evaluation is not only to reproduce and verify your
research but also to help other researchers to re-use and extend your artifacts.
Discuss how your artifacts can be adapted to other settings, e.g., more input
dimensions, other datasets, and other behavior, through replacing individual
modules and functionality or running more iterations of a specific module.
