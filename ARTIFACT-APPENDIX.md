# Artifact Appendix

Paper title: **Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents**

Requested Badge(s):
  - [x] **Available**
  - [x] **Functional**
  - [x] **Reproduced**

## Description
Replace this with the following:

Article: "Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents" Oliveira et al.
The artifacts are formed by the following:

- A CSV file containing the third parties found in each service, along with the account and consent conditions under which they were observed - `tpdomains.csv`
- A script that, given the interaction artifacts, produces the basis of the aforementioned CSV - `domains.ipynb`
- A script that collects a specification of the identifiers present in the interaction artifacts, to be later used in the disclosure hunting script - `collector.ipynb`
- A script that, given a list of third-party domains and a list of identifiers, searches for possible third-party disclosures in the interaction artifacts - `hunter.ipynb`
- A script that reads HAR capture files from a folder and detects fingerprinting API usage based on `fp-inspector_apis.txt` - `fingerprint.py`.

### Security/Privacy Issues and Ethical Concerns

There are no ethical Issues with the artifacts.

## Basic Requirements

None

### Hardware Requirements

None

### Software Requirements (Required for Functional and Reproduced badges)

1. List the OS you used to run your artifact, along with its version (e.g.,
   Ubuntu 22.04). If your artifact can only run on a specific OS or a specific
   OS version, list it and explain why here. In general, your artifact reviewers
   will probably have access to a machine with a different OS or different OS
   version than yours; they should still be able to run appropriately packaged
   artifacts.
2. List the OS packages that your artifact requires, along with their versions.
3. Artifact packaging: If you use a container runtime (e.g., Docker) to run the
   artifact, list the container runtime and its version (e.g., Docker 23.0.3).
   If you use VMs, list the hypervisor (e.g., VirtualBox) to run the artifact.
4. List the programming language compiler or interpreter you used to run your
   artifact (e.g., Python 3.13.7). Your Docker image or VM image should have
   this version of the programming languages installed already. Your Dockerfile
   should start from a base image with this programming language version.
5. List packages that your artifact depends on, along with their versions. For
   example, Python-based privacy-preserving machine learning artifacts typically
   require `numpy`, `scipy`, etc. You may point to a file in your artifact with
   this list, such as a `requirements.txt` file. If you rely on proprietary
   software (e.g. Matlab R2025a), list this here and consider providing access
   to reviewers through HotCRP.
6. List any machine learning models required to run your artifact, along with
   their versions. If your model is hosted on a different repository, such as on
   Zenodo, then your artifact should download it automatically (same for
   datasets). If a required ML model is _not_ in your artifact, provide a dummy
   model to demonstrate the functionality of the rest of your artifact.
7. List any datasets required to run your artifact. If any required dataset is
   not in your artifact, you should provide a synthetic dataset that showcases
   the expected data format.

decouple
pandas==2.3.3
ipwhois
pycountry-convert
asttokens==3.0.1
comm==0.2.3
debugpy==1.8.21
decorator==5.3.1
exceptiongroup==1.3.1
executing==2.2.1
ipykernel==7.3.0
ipython==8.39.0
jedi==0.20.0
jupyter_client==8.9.1
jupyter_core==5.9.1
matplotlib-inline==0.2.2
nest-asyncio==1.6.0
numpy==2.2.6
packaging==26.2
parso==0.8.7
pexpect==4.9.0
platformdirs==4.10.0
prompt_toolkit==3.0.52
psutil==7.2.2
ptyprocess==0.7.0
pure_eval==0.2.3
Pygments==2.20.0
python-dateutil==2.9.0.post0
pytz==2026.2
pyzmq==27.1.0
six==1.17.0
stack-data==0.6.3
tornado==6.5.7
traitlets==5.15.1
typing_extensions==4.15.0
tzdata==2026.2
wcwidth==0.8.1
certifi==2026.5.20
charset-normalizer==3.4.7
dnspython==2.8.0
filelock==3.29.1
idna==3.18
requests==2.34.2
requests-file==3.0.1
tldextract==5.3.1
urllib3==2.7.0

### Estimated Time and Storage Consumption (Required for Functional and Reproduced badges)

Replace the following with estimated values for:

- The overall human and compute times required to run the artifact.
- The overall disk space consumed by the artifact.

This helps reviewers schedule the evaluation in their time plan and others in
general to see if everything is running as intended. This should also be
specified at a finer granularity for each experiment (see below).

If your experiments require long compute times (e.g., more than 2 days) consider
providing experiments with reduced scale, especially for the "Functional" badge.

## Environment (Required for all badges)

In the following, describe how to access your artifact and all related and
necessary data and software components. Afterward, describe how to set up
everything and how to verify that everything is set up correctly.

### Accessibility (Required for all badges)

GitHub

Replace the following by a description of how to access your artifact via
persistent sources. Valid hosting options are institutional and third-party
digital repositories (e.g., GitHub, Gitlab, BitBucket, Zenodo, Figshare, etc.).
Please do not use personal web pages or cloud storage services like Google
Drive, Dropbox, etc.

Note that once your artifact evaluation is finalized and a badge decision has
been made, artifact chairs will collect a stable and persistent reference to
your artifact to list on the website. For version-controlled repositories (e.g.,
Git repositories), this will be a specific commit-id or tag.

You _should not_ link to a specific commit here at submission time, as changes
will likely happen during the evaluation process to address the reviewers'
feedback, resulting in the link being out-of-date. Instead, you may link to the
latest commit in your branch (e.g. main) as follows:
https://github.com/PoPETS-AEC/example-docker-python-pip/tree/main

### Set Up the Environment (Required for Functional and Reproduced badges)

Replace the following by a description of how one should set up the environment
for your artifact, including downloading and installing dependencies and the
installation of the artifact itself (i.e., from the very first download or clone
command one should perform). Be as specific as possible here. If possible, use
code segments to simplify the workflow, e.g.,

```bash
git clone https://github.com/PoPETS-AEC/example-docker-python-pip.git
docker build -t example-docker-python-pip:main .
```

Describe the expected results where it makes sense to do so.

### Testing the Environment (Required for Functional and Reproduced badges)

Replace the following by a description of the basic functionality tests to check
if the environment is set up correctly. These tests could be unit tests,
training an ML model on very low training data, etc. If these tests succeed, all
required software should be functioning correctly. Use code segments to simplify
the workflow, e.g.,

Launch the Docker container, attach the current working directory (i.e., run
from the root of the cloned git repository) as a volume, set the context to be
that volume, and provide an interactive bash terminal:

```bash
docker run --rm -it -v ${PWD}:/workspaces/example-docker-python-pip \
    -w /workspaces/example-docker-python-pip \
    --entrypoint bash example-docker-python-pip:main
```

Then within the Docker container, run:

```bash
./test.sh
```

Include the expected output.

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
