# Python API Framework

Lightweight API automation framework built with Python, pytest, httpx and FastAPI.

The framework currently targets the Restful Booker API and includes a local Fake CRM service for integration and end-to-end testing.

## Installation

Clone the repository and install the project dependencies:

```bash
git clone https://github.com/annBiel09/python-api-restful-booker.git
cd Python_API_Framework

python3 -m venv .venv
source .venv/bin/activate

python -m pip install -r requirements.txt
```

## Running the Fake CRM

Some end-to-end tests require the local Fake CRM service.

```bash
cd fake-crm
uvicorn main:app --reload
```

## Running tests

Run all tests:

```bash
pytest
```

## Code Quality

```bash
ruff check
ruff format
mypy .
```

## Features

The framework currently includes:

- Integration tests
- End-to-end tests
- Token-based authentication
- Random test data generation with Faker
- Fake CRM service for external API simulation