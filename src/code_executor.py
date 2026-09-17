import subprocess
import sys
import tempfile
from pathlib import Path
import json
import time

def execute_solution(
    code: str,
    function_name: str,
    inputs: tuple,
    timeout_seconds: float = 2.0,
):
    test_script = f"""
{code}

import json

inputs = {inputs!r}

result = {function_name}(*inputs)

print(json.dumps(result))
"""

    with tempfile.TemporaryDirectory() as temp_dir:
        script_path = Path(temp_dir) / "solution.py"
        script_path.write_text(test_script, encoding="utf-8")

        try:
            start_time = time.perf_counter()
            completed = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
            )
            runtime_ms = (time.perf_counter() - start_time) * 1000

            if completed.returncode != 0:
                return {
                    "success": False,
                    "result": None,
                    "error_type": "runtime_error",
                    "error_message": completed.stderr.strip(),
                    "runtime_ms": runtime_ms ,
                }

            output = completed.stdout.strip()

            return {
                "success": True,
                "result": json.loads(output),
                "error_type": None,
                "error_message": None,
                "runtime_ms": runtime_ms,
            }

        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "result": None,
                "error_type": "timeout",
                "error_message": (
                    f"Execution exceeded {timeout_seconds} seconds."
                ),
                "runtime_ms": timeout_seconds * 1000,
            }