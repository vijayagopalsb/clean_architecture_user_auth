## Clean Architecture User Authentication

This project is a trivial implementation of Clean Architecture principles in Python with a FastAPI application. A core user authentication use case – user registration – showcases how to separate concerns across domain entities, use cases, interface adapters, and external frameworks.

Consider this project as a starter or educational reference for developers looking to understand and apply Clean Architecture in real-world backend services, emphasizing testability, scalability, and independent business logic.

Of course, this is a trivial implementation, but it lays all the groundwork for extending the application to include additional features like login, JWT-based authentication, persistent storage (and more), without compromising architectural boundaries.

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

### Usage Example

Once the FastAPI server is running, we can test the user registration endpoint using either Swagger UI, cURL, or Postman.

- Swagger UI

 Browser at  http://127.0.0.1:8000/docs 

An interactive API documentation page will show where we can test the <u>register</u> endpoint.

1. Click on the POST /register endpoint.
2. Click "Try it out".
3. Enter the following JSON payload:
```bash
{
  "username": "vijay",
  "password": "securepass",
  "email": "vijay@example.com"
}
```
4. Click Execute to register a new user.

- cURL

```bash
curl -X POST "http://127.0.0.1:8000/register" \
  -H "Content-Type: application/json" \
  -d '{"username": "vijay", "password": "securepass", "email": "vijay@example.com"}'
```

- Postman

Set the method to POST

Set the URL to: http://127.0.0.1:8000/register

Go to the Headers tab and add:

| Key          | Value            |
| ------------ | ---------------- |
| Content-Type | application/json |


Go to the Body tab:

- Select raw

- Choose JSON as the format

- Paste the following example:

```bash
{
  "username": "vijay",
  "password": "securepass",
  "email": "vijay@example.com"
}
```

Click the "Send" button.

### Expected Response

if successful:

```bash
{
  "message": "User registered successfully"
}
```

if user already exists:

```bash
{
  "detail": "User already exists"
}
```


