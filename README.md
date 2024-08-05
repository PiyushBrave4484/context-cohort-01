[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/crowdbotics-research-projects/context-cohort-01)

# Project Details

Welcome and thank you for being part of this research project. You are in Cohort 1 and you can find details on how to get started [here](https://crowdbotics.notion.site/Cohort-1-5db06b845fce4a2a95265e4c8cf4d5b8).

Project requirements are located [here](https://crowdbotics.notion.site/Project-Requirements-c886f74c68a94098a1fd463c59471795?pvs=4).

## Project Structure

The repository is structured as a DevContainer and contains the following features:

- A Python 3.12 environment installed from the default Microsoft Devcontainer registry.
- A Docker configuration for local and web codespaces development, including a PostgreSQL database.
  - PostgreSQL runs on its default port 5432.
- Zsh shell

### Preinstalled Python Packages

- FastAPI
- Uvicorn
- SQLAlchemy
- Alembic
- Pyscopg2
- Python Dotenv
- Python Multipart

#### Preinstalled Python Packages for Development

- Black
- Pytest
- Pytest-cov
- Coverage

### Preinstalled VS Code Extensions

- Python
- Pylance
- Black formatter
- SQL Tools for PostgreSQL

## Getting Started

### Github Codespaces on the Web

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/crowdbotics-research-projects/context-cohort-01)

### Local Development

1. Install the VSCode Devcontainer extension.
2. Open the repository in VSCode.

## Running the Application

### Using DevContainers

This project is set up to be used with Visual Studio Code DevContainers. To start the application:

1. Open the project in Visual Studio Code.
2. Reopen the project in a DevContainer.
3. The application will automatically build and start.

### Using Docker Compose

Alternatively, you can run the application using Docker Compose:

```sh
docker-compose up --build
```

## Create and Apply Migrations

This project uses Alembic to manage migrations and changes to the database.

1. Create a new migration after updating the models:

```sh
alembic revision --autogenerate -m "Update models with correct table names and relationships"
```

2. Apply the migrations:

```sh
alembic upgrade head
```
