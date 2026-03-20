# Ring Timer (Python)
*created: 2024/07/12*

A macOS CLI tool that rings your laptop at a set interval — useful as a periodic reminder or focus timer.

## Requirements

- macOS (uses `afplay` for audio)
- Python 3.11+
- [pynput](https://pypi.org/project/pynput/) — install via `pip install pynput`

## Usage

*(Activate venv if needed)*
```bash
python3 -m venv venv
source venv/bin/activate
```

### Run directly

```bash
# Check version
python main.py --version

# Prompt for interval on startup
python main.py

# Pass interval in seconds as an argument
python main.py 1800   # ring every 30 minutes
```

### Controls

| Key       | Action                        |
|-----------|-------------------------------|
| `Space`   | Continue to the next interval |
| `Esc`     | Exit the program              |
| `Ctrl+C`  | Force exit                    |

## Testing

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest test_main.py

# Run tests with coverage
python -m pytest test_main.py --cov=main --cov-report=term-missing

# Run tests with unittest
python -m unittest test_main.py
```

## Build (standalone binary)

```bash
pip install pyinstaller
pyinstaller --onefile main.py
./dist/main
```
