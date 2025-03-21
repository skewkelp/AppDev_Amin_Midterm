# AppDev_Amin_Midterm
# Project Title

Task Manager in Django with CRUD functionality. Adding and updating/editing for the status column is based on due_date. If due_date is not passed the current day, status will be "Overdue". Otherwise "Pending".

## Features
- Feature 1
- Feature 2
- Feature 3

## Prerequisites
- Python 3.13.1
- Django 5.1.7
- 11.4.5-MariaDB
- PyMySQL==1.1.1
- mysqlclient==2.2.7

## Setup Instructions
Create the main folder holding the django project folder.

-In vscode created or started the django project
python -m django startproject (project_foldername)
python -m django startproject task_manager


-same file directory 
--run pipenv shell
python -m pipenv shell
(creates Pipfile.lock)

--install pymysql
python -m pipenv install pymysql
(Creates Pipfile)

--made sure mysqlclient is installed 
python -m pipenv install django mysqlclient
python -m pipenv install mysqlclient

-Changing the directory to the the django project
-creating the applevel
py manage.py startapp (applevelname)
py manage.py startapp tasks

-The rest is for doing the necessary changes such as adding urls within the applevel folder, and re editing the project level settings.py file etc. 

-Also made sure to update models.py for the classes for the data column/table.

-then

py manage.py makemigrations
py manage.py migrate


-run the server
py manage.py runserver


http://127.0.0.1:8000/
loading this url will redirect you to this url
http://127.0.0.1:8000/task-manager/view-list/
 with the views.py and urls.py in the applevel folder to load the display table.


NOTES:
database used is the same with previous activity, check settings.py

### Clone the Repository
```bash
git clone https://github.com/username/repo_name.git