#!/usr/bin/env python3
"""Smoke test: checks the environment, not the paper's results."""
import sys

checks = {
    "Python 3.13": lambda: sys.version_info[:2] == (3, 13),
    "Dependencies": lambda: __import__("pandas") and __import__("tldextract"),
    "Sample data": lambda: __import__("pathlib").Path("./data/samples").is_dir(),
}

ok = True
for name, check in checks.items():
    try:
        passed = bool(check())
    except Exception:
        passed = False
    print(f"{name:<16} {'OK' if passed else 'FAILED'}")
    ok &= passed

print("\nEnvironment is ready." if ok else "\nSetup Failed")
sys.exit(0 if ok else 1)