
# FastAPI POC

Simple FastAPI project using a Python virtual environment and `requirements.txt`.

## Setup

### 1. Create virtual environment

```bash
python3.14 -m venv .venv
```

### 2. Activate virtual environment

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip3.14 install -r requirements.txt
```

### 4. Run FastAPI

From the project root:

```bash
uvicorn src.main:app --reload
```

Or:

```bash
python3.14 -m src.main
```

## Requirements

### Save New installed packages

```bash
pip3.14 freeze > requirements.txt
```

This writes the packages installed in the current virtual environment into `requirements.txt`.
Run this Command to update requirements before uploading to git

### Install from requirements

```bash
pip3.14 install -r requirements.txt
```

This reads `requirements.txt` and installs the listed packages into the current virtual environment.
Use Before Running Server

## Useful Commands

Check installed packages:

```bash
pip3.14 list
```

Check packages saved in requirements:

```bash
cat requirements.txt
```

Deactivate virtual environment:

```bash
deactivate
```

## Project Structure

```text
FastApi-POC/
├── .venv/                 # Virtual environment
├── requirements.txt       # Python dependencies
├── README.md
└── src/
    ├── main.py            # FastAPI entry point
    └── config/
        └── envConfig.py   # Environment configuration
```
