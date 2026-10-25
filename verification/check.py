#!/usr/bin/env python3
"""Run both independent finite audits and report their combined result."""

import json
from pathlib import Path
import subprocess
import sys


AUDITS = (
    ("dense_circuit", "verify_bell_layout.py", "passed", True,
     "outcome_branches_checked"),
    ("resource_probability", "verify_construction.py", "status", "PASS",
     "coverage"),
)


def main():
    directory = Path(__file__).resolve().parent
    optimization = ["-" + "O" * sys.flags.optimize] if sys.flags.optimize else []
    results = {}
    for name, script, success_key, success_value, summary_key in AUDITS:
        try:
            process = subprocess.run(
                [sys.executable, *optimization, str(directory / script)],
                capture_output=True, text=True, check=False,
            )
            if process.stderr:
                print(process.stderr, file=sys.stderr, end="")
            if process.returncode:
                if process.stdout:
                    print(process.stdout, file=sys.stderr, end="")
                raise RuntimeError(f"{script} exited with code {process.returncode}")
            result = json.loads(process.stdout)
            if not isinstance(result, dict) or result.get(success_key) != success_value:
                raise ValueError(f"{script} did not report success")
            results[name] = {"status": "PASS", summary_key: result[summary_key]}
        except (OSError, RuntimeError, ValueError, KeyError) as error:
            results[name] = {"status": "FAIL", "error": str(error)}

    passed = all(result["status"] == "PASS" for result in results.values())
    print(json.dumps({"status": "PASS" if passed else "FAIL", "audits": results},
                     indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
