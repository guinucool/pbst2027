import os

# Human-readable labels for the consent-banner interaction codes.
CONSENT = {
    "0": "No consent banner",
    "1": "Ignore Consent",
    "2": "Reject All",
    "3": "Accept All",
}

# Category label used when classifying third-party domains and organizations.
TRACKING = 'Tracking'

# Marker symbols used to distinguish the two point categories in the plot.
LEFT_SYM = 'o'
RIGHT_SYM = 's'

# Padding fractions applied around the plotted points/axes.
X_PAD = 0.04
DOMAIN_PAD = 0.15
CODOMAIN_PAD = 0.10

# Colors used for plotting points and connecting lines.
POINT_COLOR = "#72728E"
LINE_COLORS = {'dashed': "#ff4d4d51", 'solid': "#4545451F"}

# The location where the graphical results will be saved.
RESULTS_PATH = "../data/results/tests"

# The path to the final CSV file containing the classified third-party domains.
TPDOMAINS_PATH = os.path.join(RESULTS_PATH, "tp_final.csv")

# The path where the generated third-party domain graph will be written.
OUTPUT_PATH = os.path.join(RESULTS_PATH, "tp_graph.pdf")