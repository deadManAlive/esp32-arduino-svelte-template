"""
    spiffs generator + uploader tools
"""

import esptool
import spiffsgen
import sys
import json

from part import get_spiffs_parameter
                
BIN = "public.spiffs.bin"

"""
    pass port as 'port=PORT'
"""

if __name__ == "__main__":
    spiffs_offset, spiffs_size = get_spiffs_parameter()

    if spiffs_offset is None or spiffs_size is None:
        raise Exception("SPIFFS offset or size undetermined!")
    
    print(f"spiffs offset: [{spiffs_offset}] size: [{spiffs_size}]")

    # generate
    spiffsgen_args = [
        spiffs_size,
        "public",
        BIN
    ]
    
    port = None

    if "--no-upload" in sys.argv:
        spiffsgen.main(spiffsgen_args)
        exit(0)
    else:
        # check if port is given
        p = next((opt for opt in sys.argv if "port=" in opt), None)

        if p is None:
            with open("./arduino-config.json") as cfgfile:
                cfg = json.load(cfgfile)
                port = cfg["port"]

                if port == "":
                    raise ValueError("Port is not set in 'arduino-config.json'!")
        else:
            port = p.split("=")[1]
            with open("./arduino-config.json", "r") as cfgfile:
                cfg = json.load(cfgfile)
                cfg["port"] = port
            with open("./arduino-config.json", "w") as cfgfile:
                json.dump(cfg, cfgfile, indent=4)

        if "--just-upload" not in sys.argv:
            spiffsgen.main(spiffsgen_args)

        
    # upload
    esptool_args = [
        "--chip",
        "esp32",
        "--baud",
        "921600",
        "--port",
        port,
        "--before",
        "default_reset",
        "--after",
        "hard_reset",
        "write_flash",
        "-z",
        "--flash_mode",
        "dio",
        "--flash_freq",
        "80m",
        "--flash_size",
        "detect",
        spiffs_offset,
        BIN
    ]

    print(f"Uploading SPIFFS image {BIN} with size {spiffs_size} ({int(spiffs_size, base=16)}) bytes at offset {spiffs_offset} by {port}.")

    esptool.main(esptool_args)
