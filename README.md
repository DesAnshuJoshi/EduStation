
# EduStation - School/College Management System

**Disclaimer: All names and images used in this project are for demonstration purposes only and have no connection with any real business.**
## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
## Introduction

EduStation is a web-based school/college management system developed using SQLite, Django, and Python as backend and HTML, CSS, and JS as front end. The project uses Bootstrap and Chart.JS library for the user interface. The project is in its early stages and provides basic features of accessing the system. Deployment of the project will be done soon.
## Technology Used

EduStation uses the following technologies:

- Django (Python web framework) for backend development
- SQLite for database management
- HTML, CSS, and JS for frontend development
- Bootstrap and Chart.JS for user interface development
## Features

EduStation provides the following features:

- Registration and login of students, teachers, and administrators
- Management of courses, classes, and sections
- Management of student attendance and grades
- Management of teacher assignments and schedules
- Management of administrator tasks and announcements
## Installation

To run EduStation on your local machine, follow these steps:

1. Clone the repository: 

```sh
  git clone https://github.com/DesAnshu/EduStation.git

```

2. Change directory into the project:
```sh
  cd EduStation
```

3. Create a virtual environment:
```sh
  python -m venv env
```

4. Activate the virtual environment:
```sh
  source env/bin/activate
```

5. Install the requirements:
```sh
  pip install -r requirements.txt
```

6. Run the migrations:
```sh
  python manage.py migrate
```

7. Create a superuser:
```sh
  python manage.py createsuperuser
```

8. Run the development server:
```sh
  python manage.py runserver
```

9. Access the application in your web browser at 
```sh
  http://127.0.0.1:8000/
```
    
## Deployment

Deployment of EduStation can be done using any web hosting service that supports Python and Django. Steps for deployment will be added soon.
## Screenshots

![App Screenshot]()


## Contributing

If you would like to contribute to EduStation, please follow these steps:

- Fork the repository.

- Create a new branch:
```
  git checkout -b new-feature
```

- Make your changes and commit them:
```
  git commit -m 'Add new feature'
```

- Push to the branch:
```
git push origin new-feature
```

- Create a pull request.
