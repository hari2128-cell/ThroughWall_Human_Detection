# Utilities

Small helper scripts that support the main data-collection/analysis
workflow.

| Script | Purpose |
|---|---|
| `find_serial_port.py` | Lists available serial ports and their descriptions, to identify which one the ESP32 enumerated as |
| `validate_csv.py` | Sanity-checks a recorded CSV: sample count, implied duration, min/max/mean, and flags likely ADC saturation (wiring problems) |

## Example

```bash
python find_serial_port.py
python validate_csv.py --input ../../datasets/Raw/human_walking.csv --fs 1000
```

Verified output on the shipped sample data:
```
Samples: 10000
Implied duration at 1000 Hz: 10.00 s
Min: 1675.16  Max: 2407.26  Mean: 2048.27  Std: 213.47
No significant ADC saturation detected.
```
