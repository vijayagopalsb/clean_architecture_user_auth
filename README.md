## Clean Architecture User Authentication

A Python-based user authentication system designed following Clean Architecture principles. This project emphasizes separation of concerns, scalability, and testability.

### Architecture Overview

The project is structured into distinct layers:

- **Domain**: Core business entities and logic.
- **Use Cases**: Application-specific business rules.
- **Interface Adapters**: Translates data between the use cases and external systems.
- **Frameworks & Drivers**: External tools and frameworks (e.g., web frameworks, databases).
- **Shared**: Common utilities and services used across layers.

This architecture ensures that inner layers remain independent of external frameworks and technologies.

### Prerequisites

- Python 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)

### Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Project Structure

```bash
clean_architecture_user_auth/
├── adapters/
├── domain/
├── frameworks/
├── shared/
├── use_cases/
├── requirements.txt
├── README.md
└── ...
```

###  Run Application

```bash
uvicorn frameworks.fastapi.main:app --reload
```

### Testing

 ```plaintext

 url: 127.0.0.1:8000/register

 post data:

{
  "username": "vijay",
  "password": "qwerty123",
  "email": "vijay@example.com"
}

Response:

{
  "message": "User registered successfully"
}

 ```
