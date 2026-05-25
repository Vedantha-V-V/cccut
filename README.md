# CCCUT

Implementation of the Unix Command Line Tool cut

## Project Link
[cut Tool](https://codingchallenges.fyi/challenges/challenge-cut/)

## Requirements
- python3
- pip

## Installation
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pyinstaller
```

## Build
```bash
pyinstaller --onefile cut.py
mv ~/Codespaces/Projects/cccut/dist/cut ~/Codespaces/Projects/cccut
```

## Running
```bash
./cut [OPTION] [file]
```

## Functionality
```bash
usage: cccut [-h] [-f FLAG] [-d SPACER] [file]

Print selected parts of lines from each FILE to standard output.

positional arguments:
  file

options:
  -h, --help            show this help message and exit
  -f FLAG, --flag FLAG
  -d SPACER, --spacer SPACER

Try cut --help for more information.
```