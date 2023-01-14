from part import lazy_user_want_us_to_get_arduino_cli as acli

import json
import subprocess
import sys

"""
    pass port as 'port=PORT'
"""

def deploy():
    acmd = acli()

    port = None

    p = next((opt for opt in sys.argv if "port=" in opt), None)

    if p is None:
        with open("./arduino-config.json") as cfgfile:
            cfg = json.load(cfgfile)
            port = cfg["port"]
            board = cfg["board"]

            if port == "":
                raise ValueError("Port is not set in 'arduino-config.json'!")
    else:
        port = p.split("=")[1]
        with open("./arduino-config.json", "r") as cfgfile:
            cfg = json.load(cfgfile)
            cfg["port"] = port
            board = cfg["board"]
        with open("./arduino-config.json", "w") as cfgfile:
            json.dump(cfg, cfgfile, indent=4)

    if port == "":
        raise ValueError("Port is not set in 'arduino-config.json'!")

    cpl = subprocess.run([
        acmd,
        "compile",
        "-v",
        "--fqbn",
        board,
        "--build-path",
        "./build",
        "./arduino-src/main"
        ], capture_output=True, text=True)

    if cpl.stderr != "":
        print(f"Error in compilaton: {cpl.stderr}")

    upl = subprocess.run([
        acmd,
        "upload",
        "-v",
        "-p",
        port,
        "--fqbn",
        board,
        "--input-dir",
        "./build",
        "./arduino-src/main"
    ], capture_output=True, text=True)

    if upl.stderr != "":
        print(f"Error in uploading: {upl.stderr}")


if __name__ == "__main__":
    deploy()