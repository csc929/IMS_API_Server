## Inventory Management System (IMS) - API Server Component

## About
This guide outlines how to set up and use a self-hosted Inventory Management System (IMS) built with Python, Django, and MySQL. The repository for the frontend app component is at: https://github.com/csc535/IMS_Frontend

An Inventory Management System (IMS) is a software application that helps businesses track, manage, and optimize their inventory levels. It's essentially the brain behind efficient stock control, ensuring you have the right amount of the right products at the right time.
Overall, an IMS is a valuable tool for businesses of all sizes, helping them gain better control over their inventory, reduce costs, and improve overall operational efficiency.

This project offers a web frontend that connects to a RESTful API backend. Data is stored in either a SQLite, mySQL or PostgreSQL database.

**Software Needed:**
- **Web Server (RESTful API):**
 - Technology: Django, Django REST framework
- **Database (MySQL):**
 - Technology: MySQL

**Tools (Optional):**
- **Integrated Development Environment (IDE):**
 - Options: Visual Studio, Visual Studio Code, PyCharm
- **Database Management Tool: **
 - Option: DBeaver
- **API Testing Tool: **
 - Option: Postman

**Languages:**
 - Python

**Features:**
- Login
- Change Password
- Manage Users (Admin Only)
- Logout
- Add Item
- Edit Item
- Delete Item
- View Inventory
- Search Item
- Refresh Inventory
- Pagination
- Toggle Inventory View (Warehouse/Store)

**Important Note**: This guide assumes a basic understanding of Python programming and terminal usage.

**Setup Instructions for Web Server (RESTful API):**
**1. Install Python:**
Download and install the latest version of Python from https://www.python.org/downloads/. Ensure you add Python to your system path during installation.
**2. Choose an IDE (Optional):**
While not strictly necessary, an IDE can improve development experience. Install Visual Studio Code, PyCharm, or a similar IDE of your preference.
**3. Download and Install MySQL:**
Install MySQL server for your operating system.
**4. Clone the Project Repository (if applicable):**
If you have access to a Git repository containing the IMS project code, clone it using Git Bash or a Git GUI client.
**5. Install all dependencies from a requirements.txt file for Web Server (RESTful API)**
pip install -r requirements.txt

**Explanation:**
- pip: This is the Python package installer.
- install: This tells pip that you want to install packages.
- r: This option tells pip to read requirements from a file.
- requirements.txt: This is the name of the file that contains the list of dependencies to install.

**Important Note**: Make sure the requirements.txt file is in the same directory where you run the command.

#### **Web Server (RESTful API) Project Setup:**
**1. Project Structure:** If you don't have a Git repository, you'll need to manually set up the project structure with a backend Django application.
**2. Configure Django Settings:** Edit the settings.py file to configure database connection details for your MySQL instance.

**Important Note:** Replace placeholders like your_database_name, your_database_user, and your_database_password with your actual MySQL credentials.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

**Database Setup:**

**1. Create a Database:** Use the MySQL command line or a management tool (like DBeaver) to create a database for your IMS application.
**2. Run Database Migrations:** Navigate to your project directory in the terminal and run the following commands in your terminal to create database table structures based on your models:
python manage.py makemigrations Accounts IMS_Control
python manage.py migrate
**3. Create Superuser:** Create an initial superuser account to log in and manage the system:
##### Replace with your details
python manage.py createsuperuser --username superadmin --email  superadmin@youremail.com

**Run the Development Server:**
Navigate to the project directory in your terminal and run: 
python manage.py runserver
##### This starts the Django development server, typically accessible at http://127.0.0.1:8000/ in your web browser.
