# Procrastinate POC

This is a proof of concept (POC) application demonstrating the usage of [Procrastinate](https://procrastinate.readthedocs.io/), a PostgreSQL-based distributed task processing library for Python.

## Overview

This POC showcases how to:
- Set up and configure Procrastinate
- Define and queue tasks
- Process tasks asynchronously
- Handle task failures and retries
- Deploy using Docker and Docker Compose

## Prerequisites

- Docker
- Docker Compose
- Python 3.9+
- PostgreSQL
- pip

## Setup

### Local Development

1. Install dependencies:
```bash
pip install procrastinate psycopg2-binary
```

2. Configure PostgreSQL connection

3. Initialize the database schema:
```bash
python -m procrastinate schema --apply
```

### Docker Setup

1. Build the containers:
```bash
docker-compose build
```

2. Start the services:
```bash
docker-compose up -d
```

The setup includes:
- PostgreSQL database container
- Python application container with Procrastinate
- Adminer for database management (optional)

## Usage

Detailed usage instructions and examples will be added as the POC develops.

## Contributing

This is a POC project. Please refer to the team for contribution guidelines.
