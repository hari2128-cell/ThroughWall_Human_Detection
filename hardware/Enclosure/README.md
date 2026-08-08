# Enclosure

## Design considerations

- **RF transparency**: the enclosure wall facing the sensing direction must
  be non-metallic (plastic, wood, cardboard) and thin enough to avoid
  attenuating the already-weak reflected microwave signal. Avoid metallic
  paints, foil tape, or metal standoffs directly in front of the radar.
- **Ventilation**: include small vent holes/slots — the ESP32 and radar
  module can warm up during continuous operation.
- **Access**: leave the USB port accessible for power/serial without
  opening the case.
- **Mounting**: through-holes/standoffs for the ESP32 board and radar
  module, spaced to keep the radar module unobstructed.

## Suggested build

A simple 3D-printed or laser-cut box (~100mm x 70mm x 30mm) with:
- A radar-facing panel with no internal metal supports
- A cutout/slot for the USB cable
- Snap-fit or screw-on lid for access to reset/boot buttons during development

## Files to add
- [ ] CAD source file (`.stl`/`.step`/`.f3d`) for a 3D-printed enclosure
- [ ] Laser-cut plans (`.svg`/`.dxf`) if using a cut-panel design
- [ ] Photos of the assembled enclosure → also copy into `images/`
