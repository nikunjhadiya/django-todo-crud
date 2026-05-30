# Django Todo CRUD Application

A modern Todo Management System built using Django. This project allows users to create, view, update, and delete tasks through a clean and responsive interface.

---

## Project Overview

This project was developed as part of my Django learning journey. It demonstrates the implementation of CRUD (Create, Read, Update, Delete) operations using Django Models, Views, Templates, URL Routing, and SQLite Database.

The application helps users manage daily tasks efficiently through a simple and user-friendly interface.

---

## Features

### Task Management
- Add new tasks
- View all tasks
- Update existing tasks
- Delete tasks

### User Interface
- Responsive navigation bar
- Clean table layout
- Modern form design
- Fixed navigation menu
- Mobile-friendly design

### Backend Functionality
- Django Models
- Django Views
- URL Routing
- SQLite Database Integration
- Template Inheritance
- Static CSS Styling

---

## Technologies Used

### Frontend
- HTML5
- CSS3

### Backend
- Python
- Django

### Database
- SQLite

### Version Control
- Git
- GitHub

---

## Project Structure

```text
myproject/
│
├── base/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── add.html
│   │   ├── update.html
│   │   └── nav.html
│   │
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── static/
│   └── css/
│       └── style.css
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

---

## Database Model

```python
class TaskModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
```

---

## CRUD Operations

### Create Task
Users can add new tasks by entering:
- Title
- Description

### Read Tasks
All tasks are displayed in a structured table.

### Update Task
Users can modify:
- Task Title
- Task Description

### Delete Task
Users can remove tasks from the database.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/django-todo-crud.git
```

### Move Into Project

```bash
cd django-todo-crud
```

### Create Virtual Environment

```bash
python -m venv myenv
```

### Activate Environment

Windows:

```bash
myenv\Scripts\activate
```

### Install Dependencies

```bash
pip install django
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

### Open Browser

```text
http://127.0.0.1:8000/
```

---

## Learning Outcomes

Through this project I learned:

- Django Project Structure
- Models and Database Operations
- URL Configuration
- CRUD Functionality
- Template Inheritance
- Static File Management
- Git and GitHub Workflow
- Responsive UI Design

---

## Development Timeline

### Day 1
- Created Django project and app
- Configured templates and static files
- Designed navigation bar

### Day 2
- Built TaskModel
- Implemented Add Task functionality
- Connected SQLite database

### Day 3
- Developed Home page
- Displayed tasks in table format
- Added responsive CSS styling

### Day 4
- Implemented Update functionality
- Implemented Delete functionality
- Improved UI and GitHub deployment

---

## Future Improvements

- User Authentication
- Task Status (Completed/Pending)
- Search Tasks
- Pagination
- Task Categories
- Dark Mode
- REST API Integration

---

## Author

Nikunj

Python Developer | Django Learner

---

## GitHub Repository

Upload this project to GitHub and continue improving it with new features.