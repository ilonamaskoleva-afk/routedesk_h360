import os, textwrap, json, zipfile, pathlib

# Указываем путь для генерации проекта в текущей директории
root = pathlib.Path("routedesk_backend_ml")
files = {}

def add(path, content):
    """Добавляет файл в словарь для последующей записи"""
    files[path] = textwrap.dedent(content).lstrip()

# ---------------------------------------------------------------------------
# README.md
# ---------------------------------------------------------------------------
add("README.md", r"""
# RouteDesk — Backend + ML starter

Backend API (FastAPI + PostgreSQL) and an isolated ML experiment package for classifying internal requests into five departments:
`IT`, `АХО`, `Кадры`, `Бухгалтерия`, `Учебный отдел`.

## Important

- This is a runnable starter implementation, not a validated production system.
- The included CSV is **synthetic demo data**. Do not present its model metrics as real research results.
- The baseline and evaluation pipeline run locally. ruBERT fine-tuning is optional and requires a properly labelled dataset plus sufficient compute.
- The LLM adapter is deliberately provider-neutral: it returns a clear configuration error until you connect an approved LLM endpoint.
- Before using real university requests, obtain permission, remove personal data, and check the institution's data-handling requirements.

## Requirements

- Python 3.11+
- Docker Desktop / Docker Engine with Compose
- For local ML experiments: `pip install -r ml/requirements.txt`
- For ruBERT: GPU recommended; install the ML requirements and run the optional training command.

## Quick start: Backend + PostgreSQL

1. Copy `.env.example` to `.env`.
2. Run:

```bash
docker compose up --build
