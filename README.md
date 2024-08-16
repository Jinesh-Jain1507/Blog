# Django Blog Website

This is a simple blog website built using Django, a Python web framework. The website allows users to create accounts, write blog posts, and manage their content.

## Implementation Video

[![Watch Again](https://img.youtube.com/vi/0VNlHU5WGkg/0.jpg)](https://www.youtube.com/watch?v=0VNlHU5WGkg)

## Features

- **User authentication**: Users can sign up, log in, and log out.
- **CRUD operations for blog posts**: Create, read, update, and delete operations for blog posts.
- **Responsive design**: The website is optimized for desktop and mobile devices.
- **Admin panel**: Admin users can manage blog posts, comments, and user accounts.

## Technologies Used

- **Django**: Python web framework for building the backend of the website.
- **HTML/CSS**: Frontend markup and styling.
- **Bootstrap**: Frontend framework for responsive design.
- **SQLite**: Database system for storing blog posts, comments, and user data.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Jinesh-Jain1507/blog.git

2. **Navigate to the project directory**:
   ```bash
   cd blog

3. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv env

4. **Activate the virtual environment**:

   - **On Windows:
     ```bash
     .\env\Scripts\activate
   - **On macOS/Linux:
     ```bash
     source env/bin/activate

5. Install python (https://www.python.org/downloads/) then install django:
   ```bash
   pip install django

6. Make migrations:
   ```bash
   python manage.py makemigrations

7. Create the database schema
   ```bash
   python manage.py migrate

8. Create a superuser (admin user) for accessing the admin panel:
   ```bash
   python manage.py createsuperuser

9. Start the development server:
   ```bash
   python manage.py runserver

Open your web browser and navigate to http://localhost:8000 to access the website.


