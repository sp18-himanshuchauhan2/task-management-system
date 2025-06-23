# 📝 Task Management API Backend

A simple Task Management System built using **Django** and **Django REST Framework**. This backend provides APIs for user registration, login, and full task CRUD operations — including filtering, status updates, and deadlines.

---

## 🚀 Features

- User Registration & Token-based Login
- Create, Read, Update, Delete (CRUD) tasks
- Filter tasks by status or due date
- Token Authentication
- Secure, user-specific task access
- Pagination and optional search support

---

## ⚙️ Tech Stack

- Python 3
- Django 4
- Django REST Framework
- SQLite (default) or PostgreSQL
- Postman (for testing)

---

## 📁 Project Structure

taskmanager/
│
├── taskmanager/ # Main project settings
├── tasks/ # Task app with models, views, serializers, urls
│
├── db.sqlite3 # Default database
├── manage.py
├── README.md
└── requirements.txt # (Optional) For deployment

yaml
Copy code

---

## 🧑‍💻 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/taskmanager-backend.git
cd taskmanager-backend
2. Create a Virtual Environment (Optional but Recommended)
bash
Copy code
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
3. Install Dependencies
bash
Copy code
pip install django djangorestframework
4. Apply Migrations and Run Server
bash
Copy code
python manage.py migrate
python manage.py runserver
Visit: http://127.0.0.1:8000/admin

🔐 Authentication
This project uses Token Authentication via DRF.

After registering or logging in, a token will be returned.

Include it in Authorization header of future requests:

makefile
Copy code
Authorization: Token your_token_here
