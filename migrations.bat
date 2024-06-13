@echo off
cd %~dp0
call venv\Scripts\activate
cd local_server
python manage.py makemigrations
python manage.py migrate
python manage.py check
pause
