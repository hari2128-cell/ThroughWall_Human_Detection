# Datasheets

Place component datasheets (PDF) here for quick reference. Suggested set:

- [ ] `ESP32-WROOM-32_datasheet.pdf` — Espressif ESP32 module datasheet
- [ ] `radar_module_datasheet.pdf` — your specific Doppler radar module
      (e.g. HB100, CDM324, RCWL-0516) — **add the exact model you used**
- [ ] `voltage_regulator_datasheet.pdf` — if using an external regulator
      (see `hardware/Power_Management`)
- [ ] `usb_uart_bridge_datasheet.pdf` — onboard USB-serial chip (e.g.
      CP2102, CH340), if relevant to your board

## Quick reference table (fill in once datasheets are added)

| Component | Key spec | Value |
|---|---|---|
| ESP32 ADC | Resolution | 12-bit (0-4095) |
| ESP32 ADC | Input range (11dB atten) | 0 - ~3.3V |
| Radar module | Operating frequency | _fill in, e.g. 10.525 GHz_ |
| Radar module | Supply voltage | _fill in_ |
| Radar module | IF output range | _fill in_ |
