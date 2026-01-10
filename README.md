# gTTS Text-to-Speech Utilities

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](ref/LICENSE)

A small collection of helper scripts for working with Google Text-to-Speech and the `gtts-cli` tool on Windows.

## Table of Contents
- [gTTS Text-to-Speech Utilities](#gtts-text-to-speech-utilities)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Included Scripts](#included-scripts)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Helper Scripts](#helper-scripts)
  - [Kardenwort Ecosystem](#kardenwort-ecosystem)
  - [License](#license)

---

## Description
This repository contains lightweight scripts to synthesize and play speech using Google TTS tooling. The code favors simple, portable commands that call existing CLI tools (`gtts-cli`, `ffplay`, `curl`) or provide small Python helpers.

[Return to Top](#gtts-text-to-speech-utilities)

## Included Scripts
- `gTTS.py` — Python wrapper that invokes `gtts-cli` and pipes audio into `ffplay` for immediate playback.
- `out.py` — small helper for output tasks.
- `a/` — archived helper scripts (historical utilities; see folder for legacy tools).

[Return to Top](#gtts-text-to-speech-utilities)

## Requirements
- Python 3.x
- `gtts-cli` (can be installed in a virtualenv or available as `gtts-cli.exe`).
- `ffmpeg` / `ffplay` for audio playback.
- `curl` — only required for legacy scripts inside `a/` if you choose to run archived examples.

[Return to Top](#gtts-text-to-speech-utilities)

## Installation
1. Clone this repository.
2. (Recommended) Create and use a Python virtual environment to isolate dependencies. Examples below create a `venv/` directory in the project root.

Windows (PowerShell):

```powershell
python -m venv venv
.\\venv\\Scripts\\Activate.ps1
pip install --upgrade pip
```

Windows (cmd.exe):

```cmd
python -m venv venv
venv\\Scripts\\activate.bat
pip install --upgrade pip
```

Linux / macOS (bash/zsh):

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

After activating the virtual environment, install any optional Python packages you need (for example `pyperclip` if you use clipboard helpers):

```bash
pip install pyperclip
```

3. Ensure `gtts-cli` and `ffplay` are on your PATH, or update the scripts with absolute paths to those binaries.

[Return to Top](#gtts-text-to-speech-utilities)

## Usage

Play text using the local `gtts-cli`/`ffplay` pipeline:

```powershell
python gTTS.py en "Hello, world"
```

The `a/` folder contains archived helper scripts and legacy examples; these are provided for reference only and are not actively maintained.

If you need an example of synthesis pipelines, prefer the root-level `gTTS.py` script and update paths to match your environment.

## Helper Scripts
Edit the scripts to point at your local installations if the bundled paths are not correct (for example, the `gtts-cli.exe` and `ffplay.exe` locations in `gTTS.py`).

[Return to Top](#gtts-text-to-speech-utilities)

## Kardenwort Ecosystem

This project is part of the Kardenwort ecosystem — a collection of small, focused utilities and examples maintained for personal productivity and learning. Kardenwort projects aim to be minimal, documented, and easy to adapt for local workflows.

[Return to Top](#gtts-text-to-speech-utilities)

## License
See `ref/LICENSE` for license details (MIT).
