# Compile Python

Showcase how you can easily compile python scripts into binary executables.

These executables, post compilation, _I believe_ can work without needing python
or the packages.

## Installation

```bash
python -m venv .venv/
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
cxfreeze example.py --target-dir dist/
./dist/example
```