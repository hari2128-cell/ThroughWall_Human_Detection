# Components

## Bill of components used in the prototype

| Component | Qty | Purpose |
|---|---|---|
| ESP32 Dev Board (WROOM-32) | 1 | Main controller — ADC sampling + UART streaming |
| Microwave Doppler Radar Module (X-band CW, analog IF out) | 1 | Motion sensing element |
| Breadboard | 1 | Prototyping |
| Jumper wires (M-M, M-F) | ~10 | Wiring |
| USB Micro/USB-C cable | 1 | Power + serial link to PC |
| 100 nF ceramic capacitor | 1-2 | Decoupling on radar supply rail |
| 10 µF electrolytic/tantalum capacitor | 1 | Bulk decoupling on radar supply rail |
| (Optional) LM7805 / AMS1117-5.0 regulator | 1 | If radar needs 5V and headroom is tight |
| (Optional) Enclosure box | 1 | See `hardware/Enclosure/` |

See `hardware/BOM/BOM.csv` for a spreadsheet version with approximate cost,
and `docs/Datasheets/` for component datasheets.

## Selecting a radar module

Any CW Doppler module with a raw analog IF output works with this firmware
as-is (e.g. HB100 + IF amplifier board, CDM324). Modules that only expose a
digital motion-detected pin (e.g. RCWL-0516 default configuration) can still
be used, but the firmware would need to read a digital GPIO instead of the
ADC, and the FFT-based analysis would be skipped in favor of the module's
built-in detection pulse.
