# IT-Training-Website

## Project Description

A comprehensive web application modeled after Scope India, aimed at providing an informative and user-friendly platform for IT training and services. This project is built using Python and Django and includes various features to enhance user experience and accessibility.

## Table of Contents
1. [Project Description](#project-description)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contact](#contact)

## Features

- **User Authentication and Authorization:** Users can sign up, log in, and manage their accounts.
- **Course Listings and Details:** View available courses, including details and enrollment options.
- **Enrollment Functionality:** Users can enroll in courses and view their progress.
- **Admin Panel:** Admins can manage courses, users, and other content through an intuitive interface.
- **Responsive Design:** The application is designed to work on both mobile and desktop devices.
- **Third-Party API Integration:** Integration with external APIs for additional functionality (e.g., SMTP).

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Version Control:** Git

## Installation

To set up this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/annlinprathisha/IT-Training-Website.git
   cd ScopeIndiaClone

2. **Create a virtual environment:**
   python -m venv myenv

3. **Activate the virtual environment:**
   myenv\Scripts\activate

4. **Install the required packages:**
   pip install django

5. **Start the Django project:**
   django-admin startproject myproject .

6. **Apply database migrations:**
   python manage.py makemigrations
   python manage.py migrate

7. **Create a superuser (for admin access):**
   python manage.py createsuperuser

8. **Run the development server:**
   python manage.py runserver

9. **Create a new Django app:**
   django-admin startapp myapp

10. **Add the app to INSTALLED_APPS in settings.py:**
   Open `myproject/settings.py` and add 'myapp' to the INSTALLED_APPS list

## Usage

Once the development server is running, you can:

Visit the main site: Navigate to http://127.0.0.1:8000/ to explore the features.
Access the admin panel: Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials to manage content.

# Contact

For any questions or suggestions, feel free to reach out:

Email: annlinprathisha@gmail.com
GitHub: annlinprathisha
