# Django Todo CRUD Application

A full-stack Todo Management System built using Django. This application allows users to create, view, update, and delete tasks through a clean, responsive, and user-friendly interface. The project demonstrates core Django concepts including Models, Views, URL Routing, Templates, Static Files, Database Integration, and CRUD Operations.

---

# Project Overview

The Django Todo CRUD Application is designed to help users organize and manage daily tasks efficiently. It provides a simple dashboard where users can add new tasks, view existing tasks, edit task details, and remove completed or unwanted tasks.

This project was developed as part of my Django learning journey and focuses on understanding how frontend and backend components interact within the Django framework.

---

# Key Features

### Task Management

- Create new tasks
- View all tasks
- Update existing tasks
- Delete tasks
- Dynamic task listing from database

### User Interface

- Responsive design
- Fixed navigation bar
- Professional table layout
- Modern form styling
- Mobile-friendly structure
- Clean user experience

### Backend Functionality

- Django Models
- Django Views
- URL Routing
- SQLite Database
- Template Rendering
- Form Processing
- Database CRUD Operations

---

# Technologies Used

## Frontend

- HTML5
- CSS3
- Django Templates

## Backend

- Python
- Django Framework

## Database

- SQLite3

## Development Tools

- VS Code
- Git
- GitHub

---

# Project Architecture

```text
Client Request
      │
      ▼
Django URL Routing
      │
      ▼
Views.py
      │
      ▼
TaskModel (Database)
      │
      ▼
Templates (HTML)
      │
      ▼
CSS Styling
      │
      ▼
Response to User
```

---

# Project Structure

```text
myproject/
│
├── base/
│   │
│   ├── migrations/
│   │
│   ├── templates/
│   │   ├── main.html
│   │   ├── nav.html
│   │   ├── home.html
│   │   ├── add.html
│   │   ├── update.html
│   │   ├── completed.html
│   │   ├── trash.html
│   │   └── about.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── static/
│   └── css/
│       └── style.css
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

---

# Database Design

## Task Model

```python
class TaskModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
```

### Fields

| Field       | Type      | Description      |
| ----------- | --------- | ---------------- |
| id          | AutoField | Primary Key      |
| title       | CharField | Task Title       |
| description | TextField | Task Description |

---

# CRUD Operations

## Create Task

Users can create a task by entering:

- Task Title
- Task Description

Data is stored in SQLite database using:

```python
TaskModel.objects.create()
```

---

## Read Tasks

All tasks are retrieved using:

```python
TaskModel.objects.all()
```

and displayed inside a responsive table.

---

## Update Task

Existing tasks can be modified using:

```python
TaskModel.objects.get(id=pk)
```

and updated through a form.

---

## Delete Task

Tasks can be removed using:

```python
TaskModel.objects.get(id=pk).delete()
```

---

# Frontend Components

## Navigation Bar

Contains links to:

- Home
- Add Task
- Completed
- Trash
- About

### Features

- Fixed position
- Responsive layout
- Hover effects

---

## Home Page

Displays all tasks in a table.

### Columns

- Title
- Description
- Actions

### Actions

- Update
- Delete

---

## Add Task Page

Allows users to:

- Enter task title
- Enter task description
- Submit task

---

## Update Task Page

Allows users to:

- Edit title
- Edit description
- Save changes

---

# Backend Workflow

### Add Task Flow

```text
User Form
    │
    ▼
POST Request
    │
    ▼
views.py
    │
    ▼
TaskModel.objects.create()
    │
    ▼
Database
```

### Update Task Flow

```text
User Clicks Update
    │
    ▼
Fetch Task By ID
    │
    ▼
Update Values
    │
    ▼
Save()
    │
    ▼
Redirect Home
```

### Delete Task Flow

```text
User Clicks Delete
    │
    ▼
Fetch Task By ID
    │
    ▼
Delete()
    │
    ▼
Redirect Home
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/nikunjhadiya/django-todo-crud.git
```

## Navigate to Project

```bash
cd django-todo-crud
```

## Create Virtual Environment

```bash
python -m venv myenv
```

## Activate Environment

```bash
myenv\Scripts\activate
```

## Install Django

```bash
pip install django
```

## Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Run Server

```bash
python manage.py runserver
```

Visit:

```text
http://127.0.0.1:8000/
```

---

# Skills Demonstrated

- Python Programming
- Django Framework
- CRUD Operations
- MVC/MVT Architecture
- Database Management
- Template Inheritance
- Frontend Development
- Responsive Design
- Git Version Control
- GitHub Repository Management

---

# Future Enhancements

- User Authentication
- Task Categories
- Task Priorities
- Search Functionality
- Pagination
- REST API
- Email Notifications
- Dark Mode
- Dashboard Analytics

---

# Author

**Nikunj Hadiya**

Python Developer | Django Developer

### Connect With Me

Portfolio: https://nikunjhadiya.netlify.app/

LinkedIn: https://www.linkedin.com/in/nikunjhadiya/

GitHub: https://github.com/nikunjhadiya

---

⭐ If you like this project, consider giving it a star on GitHub.
