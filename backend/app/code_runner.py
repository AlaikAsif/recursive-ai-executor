import subprocess
from typing import Tuple

def run_shell_command(command: str, timeout: int = 10) -> Tuple[int, str, str]:
    """Run a shell command and return (returncode, stdout, stderr)."""
    try:
        completed = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=timeout)
        return completed.returncode, completed.stdout, completed.stderr
    except subprocess.TimeoutExpired as e:
        return -1, "", f"timeout: {e}"
    except Exception as e:
        return -1, "", str(e)
