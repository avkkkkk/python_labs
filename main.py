import json
import platform
import sys
import os
import getpass

result = {
    "system": platform.platform(),
    "release": platform.release(),
    "version": platform.version(),
    "hostname": platform.node(),
    "python_version": platform.python_version(),
    "interpreter_path": sys.executable,
    "cpu_count": os.cpu_count(),
    "username": getpass.getuser(),
}
with open("result.json", "w") as f:
    json.dump(result, f, indent=4)
