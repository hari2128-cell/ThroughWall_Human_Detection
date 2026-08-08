# Scripts

Host-side Python utilities supporting data collection, preprocessing,
visualization, and general workflow.

| Folder | Purpose |
|---|---|
| `Data_Collection/` | Record live serial data from the ESP32 to CSV |
| `Data_Preprocessing/` | Batch DC-removal + band-pass filtering of raw recordings |
| `Visualization/` | Quick static plots (waveform + spectrum) for reports |
| `Utilities/` | Serial port discovery, CSV validation/sanity checks |

Install dependencies once for all scripts:
```bash
pip install -r requirements.txt --break-system-packages   # or use a venv
```

## Typical workflow

```bash
python Utilities/find_serial_port.py
python Data_Collection/record_serial_to_csv.py --port <PORT> --duration 30 --out ../datasets/Raw/trial1.csv
python Utilities/validate_csv.py --input ../datasets/Raw/trial1.csv
python Data_Preprocessing/preprocess_recording.py --input-dir ../datasets/Raw --output-dir ../datasets/Processed
python Visualization/quick_plot.py --input ../datasets/Raw/trial1.csv --output ../results/Graphs/trial1.png
```
