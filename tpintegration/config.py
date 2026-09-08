import os

# Domains owned or operated by each AI service provider.
# Used to distinguish first-party requests from third-party network traffic.
FP_DOMAINS = {
    "PERPLEXITY": ["perplexity.ai"],
    "CHATGPT":    ["chatgpt.com", "openai.com"],
    "GROK":       ["grok.com", "x.ai"],
    "CLAUDE":     ["claude.ai", "anthropic.com"],
    "COPILOT":    ["copilot.microsoft.com"],
    "DEEPSEEK":   ["deepseek.com", "high-flyer.cn"],
    "MISTRAL":    ["mistral.ai", "mistral.com"],
    "META":       ["meta.ai", "meta.com"],
    "GEMINI":     ["gemini.google.com"],
}

# Human-readable labels for the experimental configuration codes.
# Each mapping describes one dimension of a recorded test session.
ACCOUNT = {"1": "No Auth", "2": "Free", "3": "Premium"}
CHAT = {"1": "Normal", "2": "Incognito", "3": "Extra"}
PRIVACY = {"1": "Default", "2": "Minimum", "3": "Maximum", "4": "Extra"}
CONSENT = {
    "0": "No consent banner",
    "1": "Ignore Consent",
    "2": "Reject All",
    "3": "Accept All",
}
INTERACTION = {"1": "Normal", "2": "Share", "3": "Load"}

# Column order for CSV files containing detected third-party domains,
# CNAME records, and the experimental conditions under which they appeared.
TP_DOMAIN_COLLECTOR = [
    "LLM",
    "DOMAINS",
    "ThirdParty_Domain",
    "ThirdParty_CNAME",
    "ACCOUNT",
    "CHAT",
    "PRIVACY",
    "CONSENT",
    "INTERACTION",
]

# Column order for CSV files containing to be manually classified third-party domains.
TP_DOMAIN_CLASSIFICATION = ["LLM", "ThirdParty_Domain", "ThirdParty_CNAME"]

# The location of the HAR files collected from the AI service providers.
HAR_ROOT_PATH = "../data/samples"

# The location where the results of the analysis will be saved.
RESULTS_PATH = "../data/results/tests"

# The path to the CSV file containing the collected third-party domains.
COLLECTOR_PATH = os.path.join(RESULTS_PATH, "tp_collector.csv")

# The path to the CSV file containing the collected third-party domains to be manually classified.
CLASSIFICATION_PATH = os.path.join(RESULTS_PATH, "tp_classification.csv")

# The path to the CSV file containing the manually classified third-party domains.
LABELED_PATH = os.path.join(RESULTS_PATH, "tp_labelled.csv")

# The path to the final CSV file containing the classified third-party domains.
FINAL_PATH = os.path.join(RESULTS_PATH, "tp_final.csv")