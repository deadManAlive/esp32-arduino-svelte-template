BOARD = "esp32:esp32:esp32doit-devkit-v1"


if __name__ == "__main__":
    from part import lazy_user_want_us_to_get_arduino_cli as acli
    import subprocess
    
    acmd = acli()
    print(subprocess.run([acmd, "board", "listall"], capture_output=True, text=True).stdout)