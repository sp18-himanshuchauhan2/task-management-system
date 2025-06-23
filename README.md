# 📝 Task Management API Backend

A simple Task Management System built using **Django** and **Django REST Framework**. This backend provides APIs for user registration, login, and full task CRUD operations — including filtering, status updates, and deadlines.

---

## 🚀 Features

- User Registration & Token-based Login
- Create, Read, Update, Delete (CRUD) tasks
- Filter tasks by status or due date
- Token Authentication
- Secure, user-specific task access

---

## ⚙️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (default)
- Postman (for testing)

---

## 📁 Project Structure

```bash
taskmanager/
│
├── taskmanager/            # Main project settings
├── tasks/                  # Task app with models, views, serializers, urls
│               
├── .gitignore
├── db.sqlite3              # Default database
├── manage.py
├── README.md
└── requirements.txt
```

---

## 🧑‍💻 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sp18-himanshuchauhan2/task-management-system.git
cd task-management-system
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations and Run Server

```bash
python manage.py migrate
python manage.py runserver
Visit: http://127.0.0.1:8000
```

## 🔐 Authentication
This project uses **Token Authentication** via DRF.
<ul>
    <li>After registering or logging in, a token will be returned.</li>
    <li>Include it in Authorization header of future requests:</li>
</ul>

```makefile
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## 📮 API Endpoints
### 🧑 User Auth

| Endpoint         | Method | Description         |
| ---------------- | ------ | ------------------- |
| `/api/register/` | POST   | Register new user   |
| `/api/login/`    | POST   | Login and get token |

