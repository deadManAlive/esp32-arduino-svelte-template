# ESP-32 Svelte Project Template
[ESP32](https://www.espressif.com/en/products/socs/esp32) is a low-cost MCU that is very rich in features and of course portable. Meanwhile, [Svelte](https://svelte.dev/) is a compile time front-end framework (basically just HTML + JS compiler) that outputs responsive UI without relying on vDOM like React or Vue. This template ease uploading static assets to ESP32 persistent memory (in this case, **SPIFFS** is used).
## Requirements
* Node.js
* Python 3.x
* [Arduino-CLI](https://arduino.github.io/arduino-cli/) (in PATH) is recommended, or
* Arduino SDK (installed with Arduino IDE)
    * If using IDE 1.x, just use [Arduino extension](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.vscode-arduino) for Visual Studio Code, or the IDE itself.
    * Just the same for IDE 2.x, but this version also has built-in Arduino-CLI (usually NOT in PATH, put the path to cli to `cli` in `arduino-config.json`).
    * Or if you don't feel like it, we'll download it for you. Just run `upload`/`deploy` script.
> ##### Recommended
> * Use Visual Studio Code
## Getting started
* Clone this repo.
* `npm i`
* `pip install -r requirements.txt`
* `npm run upload port=COM7` to upload web server assets to SPIFFS of esp32 at `COM7`.
* `npm run deploy` to deploy program (script automatically use previous set port: `COM7`).

Port is saved as `port` configuration in `arduino-config.json`. Set this value or call `upload`/`deploy` with `port` argument provided. Subsequent calls of those scripts do not need `port` to be provided. Exception will be thrown if `port` configuration is undefined or is an empty string.

> Board configuration is default to DOIT ESP32 DEVKIT V! (set as `board` in `arduino-config.json`). List avaiable esp32 boards with `npm run lisboards` command.

## NPM Scripts
* `build`, `dev`, `start`: Svelte scripts to build/watch/test web server on localhost.
* `mkfs`: Build SPIF file system (`.spiffs.bin`) from `public` folder.
* `upload`: Build SPIFFS from `public` folder then upload to esp32, accept port argument with `port=PORT`.
* `deploy`: Upload arduino program to esp32, accept port argument with `port=PORT`.
* `listboards`: List all available esp32 boards, set accordingly in `board` in `arduino-config.json`
