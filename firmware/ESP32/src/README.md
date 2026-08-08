# src/

PlatformIO's default convention expects the entry point at `src/main.cpp`.
This project instead keeps the sketch at `main/main.ino` (so it also opens
directly in the Arduino IDE without renaming), and points PlatformIO at it
via `build_src_filter` in `platformio.ini`.

If you prefer the PlatformIO-native layout, move the firmware logic here as
`src/main.cpp` (identical content to `main/main.ino`, `.ino`→`.cpp` syntax
differences are minimal for this simple sketch) and remove the
`build_src_filter` override from `platformio.ini`.
