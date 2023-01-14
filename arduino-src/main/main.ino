#include <SPIFFS.h>

void setup() {
    Serial.begin(115200);

    if (SPIFFS.begin(true)){
        Serial.println("Error in mounting SPIFFS.");
        return;
    }

    File root = SPIFFS.open("/");
    File file = root.openNextFile();

    while(file) {
        Serial.print("file: ");
    }
}

void loop() {}