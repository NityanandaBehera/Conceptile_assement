# Quiz App - Django Application
###  A simple Django-based quiz application where users can sign up, log in, take a quiz session, and get detailed results based on their performance.

## Features
1. User authentication (signup, login, and logout).
2. Take a quiz with random multiple-choice questions.
3. Submit answers and get feedback on performance.
4. View quiz statistics with correct and incorrect answers.

## Technologies

1. Django 5.1.4 - Web framework used to build the app.
2. MySQL - Database for storing quiz data and user information.
3. Whitenoise - Static file handling.
4. Python 3.9+ - Programming language for the backend.
5. HTML/CSS/JS - Frontend technologies for building the user interface.

## Steps to Install 

1. Clone the repository:

```
git clone [https://github.com/your-username/quiz_app.git](https://github.com/NityanandaBehera/Conceptile_assement.git)
```
cd quiz_app

2. Create a virtual environment:

   ```
   python3 -m venv venv
   venv\Scripts\activate

   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Database Configuration
   ```
   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_HOST=localhost
   DB_PORT=3306
   SECRET_KEY=your_secret_key
   DEBUG=False  # Set to True during development
   ```
5.  Migrating the Database
   ```
     py manage.py makemigrations
     py manage.py migrate
   ```
6. Run the server locally
   ```
   py manage.py runserver
   ```   
