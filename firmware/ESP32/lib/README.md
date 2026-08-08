# lib/

PlatformIO convention folder for private, project-specific libraries (each
in its own subfolder with a `library.json`/`library.properties`). Not
currently used — this firmware only depends on the built-in ESP32 Arduino
core (`Arduino.h`, ADC functions).

If you later add an external dependency not available via the Arduino
Library Manager (e.g. a vendor-provided radar SDK), vendor it here instead
of relying on a system-wide install, so the build is reproducible.
