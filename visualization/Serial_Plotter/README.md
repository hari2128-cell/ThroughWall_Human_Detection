# Serial Plotter

The fastest zero-setup way to sanity-check the radar signal, with no
MATLAB or Python needed: the Arduino IDE's built-in **Serial Plotter**.

## Usage

1. Flash `firmware/ESP32/main/main.ino` as normal.
2. In the Arduino IDE: **Tools → Serial Plotter** (or `Ctrl+Shift+L`).
3. Set the baud rate dropdown in the Serial Plotter window to **115200** to
   match the firmware.
4. You should see a live scrolling line graph of the raw ADC samples
   (0-4095). Wave your hand in front of the radar module — you should see
   the trace visibly deflect/oscillate compared to the static baseline.

This is a raw, unfiltered view (no DC removal, no FFT) — it's meant purely
as a quick hardware sanity check before moving to the full MATLAB/Python
pipelines for real filtering, FFT, and motion detection.

## Alternative: PlatformIO Serial Monitor with plotting

If using PlatformIO instead of the Arduino IDE:
```bash
pio device monitor --filter printable
```
For actual graphing from PlatformIO, use the `visualization/Live_Monitoring`
or `visualization/Python_GUI` Python tools instead, which apply real
filtering, since PlatformIO's monitor is text-only.

## Troubleshooting
- **Flat line at 0 or 4095**: check wiring — radar IF output should connect
  to GPIO34, not VCC or GND.
- **Noisy but no response to motion**: confirm radar module is powered
  (check its supply voltage against `hardware/Datasheets`) and check for
  loose jumper wires.
- **No data at all**: confirm the baud rate matches (115200) and the
  correct COM/serial port is selected.
