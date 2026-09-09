import os

# Regex patterns matching known tracking-value formats found in cookies/params.
# Each entry maps a known tracker/vendor key to the pattern used to identify its value.
VALUES = {
    "_fbp":   r'fb\.1\.\d{13}\.\d{1,40}',
    "_ttp":   r'[A-Z0-9]{1,40}_\.tt\.1',
    "_twpid": r'tw\.\d{13}\.\d{1,40}',
    "_dcid":  r'dcid\.1\.\d{13}\.\d{1,40}',
    "em":     r'tv\.1~em\.[A-Za-z0-9+/=_-]{40,44}',
    "hash":   r'\b(?:[a-f0-9]{64}|[a-f0-9]{40}|[a-f0-9]{32})\b'
}

# Regex patterns matching known tracking-related cookie/parameter names.
# Used to identify a tracker by the name of the field rather than its value.
NAMES = {
    "intercom-device-id": r'intercom-device-id',
    "intercom-id":        r'intercom-id',
    "_ga":                r'^_ga$',
    "_dd_s":              r'_dd_s',
    "AnonId":             r'x-anonuserid|anonymousUser|pplx\.visitor-id|datr|MUID|ajs_anonymous_id'
}

# Regex patterns used to extract a specific sub-value (e.g. an ID) out of a
# larger matched string, via a capture group.
EXTRACTS = [
    r'GA1\.1\.(\d{1,40}\.\d{10})',
    r'aid=([a-f0-9\-]+)&',
    r'claudeai\.v1\.([a-f0-9\-]+)'
]

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

# Column order for CSV files containing detected leaks to third-party domains,
# and the experimental conditions under which they appeared.
LEAKS = ['LLM', 'Organization', 'Domain', 'Path', 'Location', 'Name', 'Value', 'Account', 'Chat', 'Privacy', 'Consent', 'Interaction']

# Filesystem locations for input samples and output result files.
HAR_ROOT_PATH = '../data/samples'
RESULTS_PATH = '../data/results/tests'

# Specific file paths used for reading labelled/expected data and writing final results.
LABELLED_FILE = os.path.join(RESULTS_PATH, 'tp_labelled.csv')
FINAL_FILE = os.path.join(RESULTS_PATH, 'pa_final.csv')
VALUES_FILE = 'info.val'
COLLECTED_FILE = 'collected.val'

# Prefix used to name flagged (i.e. tracker-matched) HAR entries.
FLAGGED_PREFIX = 'flagged_'
FLAGGED_SUFFIX = 'flag'

# Parameter name used to identify a user's email in values files.
EMAIL_PARAM = 'useremail'

# Fields whose values should be hashed for comparison.
HASH_VALUES = ['useremail', 'owneremail']

# Fields that represent conversation identifiers.
CONVERSATION_IDS = ['conversationid', 'shareid']

# Category label used when classifying third-party domains and organizations.
FIRSTPARTY = 'First-Party'