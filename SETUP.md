# REST API for autopark application
# Installation

Clone repository and cd into cloned folder

`git clone https://github.com/igorkruglyak/autopark.git`
### For UNIX-like systems
+ Install [pyenv](https://github.com/yyuu/pyenv#installation).
+ Install [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv#installation).
+ Install Python 3.10.0 : `pyenv install 3.10.0`.
+ Create a new virtualenv : `pyenv virtualenv 3.10.0 <name of virtualenv>`.
+ Activate virtualenv : `pyenv local <name of virtualenv>`.
+ Install requirements for a project : `pip install -r requirements.txt`
+ Install required migrations : `python manage.py makemigrations`
+ Run migrate : `python manage.py migrate`
+ Run server : `python manage.py runserver`
+ Also you can create superuser for admin page : `python manage.py createsuperuser`
### For Windows
[Python 3.10.0](https://www.python.org/downloads/);
[Git](https://git-scm.com/);
must be installed.
+ Create a new virtual environment : `python -m venv “venv”`
+ Activate a new virtual environment : `.\venv\Scripts\activate`
+ Install requirements for a project : `pip install -r requirements.txt`
+ Install required migrations : `python manage.py makemigrations`
+ Run migrate : `python manage.py migrate`
+ Run server : `python manage.py runserver`
+ Also you can create superuser for admin page : `python manage.py createsuperuser`
