# 🚀 Flask_Rest_API_Template

A production-ready, modular REST API template built with Flask! Perfect for kickstarting your next project with a well-structured foundation. 🛠️

## 🎯 Key Features

1. **Modular Application Design**
   - Uses the [Application Factory](https://flask.palletsprojects.com/en/master/patterns/appfactories/) and [Blueprints](https://flask.palletsprojects.com/en/master/blueprints/) patterns.
   - Environment-specific configurations (`dev`, `test`, `prod`) managed via `config.py`.
   - Easily customizable URL prefixes for APIs and health checks.

2. **Robust REST APIs with Flask-RESTX**
   - Swagger-powered API documentation.
   - Flexible API docs location via `API_DOCS_URL` in `config.py`.

3. **Comprehensive Unit Testing**
   - Testing framework with `flask-testing`.
   - Test cases organized in `person.v1.test_views.py` and `user.v1.test_views.py`.

4. **Production-Ready WSGI App**
   - Deploy using `gunicorn` with a pre-configured `gunicorn_config.py`.
   - Support for reverse proxies.

5. **Clean Project Structure**
   - Logical separation of concerns, with each versioned API neatly organized.

## 🚀 Getting Started

### 🛠️ Install and Run Locally

1. **Create a Python 3 virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install the dependencies:**

    ```bash
    pip install -r sample_project/requirements.txt
    ```

3. **Run the development server:**

    ```bash
    python run.py
    ```

    Your server should now be running at: `http://127.0.0.1:5000/`

4. **Access the Swagger API docs:**

    [http://localhost:5000/sample_project/api/v1.0/doc/](http://localhost:5000/sample_project/api/v1.0/doc/)

### 🐳 Running with Docker

1. **Build the Docker image:**

    ```bash
    docker build -t project:1 .
    ```

2. **Run the Docker container:**

    ```bash
    docker run --name project --env-file .env -d -p 8000:8000 project:1
    ```

3. **View the Swagger API docs:**

    [http://localhost:8000/sample_project/api/v1.0/doc/](http://localhost:8000/sample_project/api/v1.0/doc/)

4. **Run tests inside the Docker container:**

    ```bash
    docker exec -it project bash
    pytest .
    ```

### ✅ Static Code Analysis

```bash
flake8
```

### ✅ Run Unit Tests
```
pytest .
```

### 📊 Generate Test Coverage Report
```
coverage run -m pytest
coverage report --omit='*lib/*.py,*test_*.py'
coverage xml -i
```

### 🏗️ Project Structure
```
sample_project/
├── api_v1.py                     # API instance associated with a blueprint, linking person and user namespaces
├── app.py                        # Flask application instance with registered blueprints
├── config.py                     # Environment configurations
├── healthcheck.py                # Healthcheck endpoint
├── person/
│   └── v1/                       # Namespace for person-related endpoints
├── user/
│   └── v1/                       # Namespace for user-related endpoints
├── tests/                        # Unit tests
├── requirements.txt              # Project dependencies
└── ...
```

### 🙌 Contributing

If you find this template useful, feel free to give it a star ⭐ on GitHub! Your support is greatly appreciated. Also, follow me for more projects and updates.

[GitHub](https://github.com/asadalif18/)



