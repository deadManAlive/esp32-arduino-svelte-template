# ESP-32 Svelte Project Template
[ESP32](https://www.espressif.com/en/products/socs/esp32) is a low-cost MCU that is very rich in features and of course portable. Meanwhile, [Svelte](https://svelte.dev/) is a compile time front-end framework (basically just HTML + JS compiler) that outputs responsive UI without relying on vDOM like React or Vue. This template ease uploading static assets to ESP32 persistent memory (in this case, **SPIFFS** is used).
## Requirements
* Node.js
* Python 3.x
* [Arduino-CLI](https://arduino.github.io/arduino-cli/) (in PATH) is recommended, or
* Arduino SDK (installed with Arduino IDE)
    * If using IDE 1.x, just use [Arduino extension](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.vscode-arduino) for Visual Studio Code, or the IDE itself.
    * Just the same for IDE 2.x, but this version also has built-in Arduino-CLI (usually NOT in PATH, we take care of it).
> ##### Recommended
> * Use Visual Studio Code
## Getting started
* Clone this repo.
* `npm i`
* `pip install -r requirements.txt`