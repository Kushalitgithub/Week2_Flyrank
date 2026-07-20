# 🚀 Task API

A simple and beginner-friendly **RESTful Task Management API** built with **FastAPI**. This project demonstrates the complete **CRUD** (Create, Read, Update, Delete) workflow, input validation, proper HTTP status codes, and interactive API documentation using **Swagger UI**.

---

## ✨ Features

* 📋 Create new tasks
* 🔍 Retrieve all tasks
* 🎯 Retrieve a task by ID
* ✏️ Update existing tasks
* 🗑️ Delete tasks
* ✅ Input validation
* 🚦 Proper HTTP status codes (200, 201, 204, 400, 404)
* 📖 Interactive API documentation with Swagger UI

---

## 🛠️ Tech Stack

* **Python 3**
* **FastAPI**
* **Uvicorn**
* **Pydantic**

---

# 📂 Project Structure

```text
TaskAPI/
│── main.py
│── requirements.txt
│── README.md
│── .gitignore
└── images/
    └── swagger-ui.png
```

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the API

```bash
uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

# 📖 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🌐 API Endpoints

| Method | Endpoint      | Description             | Success Code |
| ------ | ------------- | ----------------------- | -----------: |
| GET    | `/`           | API information         |          200 |
| GET    | `/health`     | Health check            |          200 |
| GET    | `/tasks`      | Get all tasks           |          200 |
| GET    | `/tasks/{id}` | Get a task by ID        |          200 |
| POST   | `/tasks`      | Create a new task       |          201 |
| PUT    | `/tasks/{id}` | Update an existing task |          200 |
| DELETE | `/tasks/{id}` | Delete a task           |          204 |

---

# 🧪 Example API Request

### Create a Task

```bash
curl -i -X POST http://127.0.0.1:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Buy milk"}'
```

### Example Response

```http
HTTP/1.1 201 Created
content-type: application/json

{
  "id": 4,
  "title": "Buy milk",
  "done": false
}
```

---

# 📸 Swagger UI

Add your screenshot after opening:

```
http://127.0.0.1:8000/docs
```

Example:

```markdown
![Swagger UI](images/swagger-ui.png)
```

---

# 🧪 Testing

You can test the API using:

* Swagger UI
* curl
* Postman
* Insomnia

---

# 🎯 Learning Outcomes

This project helped me learn:

* REST API fundamentals
* FastAPI routing
* CRUD operations
* Request validation with Pydantic
* HTTP status codes
* Path parameters
* Request bodies
* Interactive API documentation
* Git and GitHub workflow

---

# 🚀 Future Improvements

* PostgreSQL database integration
* Docker support
* User authentication (JWT)
* Pagination and filtering
* Automated testing
* Repository and service layers

---

# 👨‍💻 Author

**Kushal Bhattarai**

Bachelor of Computer Science (AI)

Passionate about AI, backend development, and building practical software projects.

---

## ⭐ Support

If you found this project helpful, consider giving the repository a **⭐ Star** on GitHub!
