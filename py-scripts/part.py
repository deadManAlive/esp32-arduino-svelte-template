import csv
from typing import Tuple

import shutil
import platform
import requests
import os
import subprocess

DBG = True

def lazy_user_want_us_to_get_default_csv():
    # step 1: check if arduino-cli found in path
    arduino_cli = shutil.which("arduino-cli")

    print(arduino_cli)

    # step 2: if not found, download
    if arduino_cli is None or DBG:

        dlink = None
        fname = None

        sysarch = f"{platform.system()}_{platform.architecture()[0]}"

        response = requests.get("https://api.github.com/repos/arduino/arduino-cli/releases/latest")

        for asset in response.json()["assets"]:
            if sysarch in asset['name'] and 'msi' not in asset['name']:
                fname = asset['name']
                dlink = asset['browser_download_url']
                print(dlink)

        if dlink is None or fname is None:
            raise FileNotFoundError(f"Cannot find arduino-cli github asset that have '{sysarch}' substring.")

        asset_archive = requests.get(dlink)

        os.makedirs("./bin", exist_ok=True)

        with open(f"./bin/{fname}", "wb") as f:
            f.write(asset_archive.content)

        shutil.unpack_archive(f"./bin/{fname}", "./bin/arduino-cli")

        arduino_cli = "./bin/arduino-cli/arduino-cli"


def get_spiffs_parameter(partition_table: str ="default.csv") -> Tuple[str | None, str | None]:
    """11
    Get SPIFFS partition offset and size from partition table

    Takes one optional argument `partition_table` as a csv partition table, \\ 
    defaults to `default.csv` at current working directory.

    format: name, type, subtype, offset, size, flags 
        
    """
    spiffs_offset = None
    spiffs_size = None

    with open(partition_table, mode='r') as csv_file:
        csv_dict = csv.DictReader(csv_file, fieldnames=["name", "type", "subtype", "offset", "size", "flags"])
        line_count = 0
        for row in csv_dict:
            if row["name"] == "spiffs":
                spiffs_offset = row['offset'].strip()
                spiffs_size = row['size'].strip()
                
        return spiffs_offset, spiffs_size


if __name__ == "__main__":
    lazy_user_want_us_to_get_default_csv()