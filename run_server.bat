@echo off
cd %~dp0
call venv\Scripts\activate
cd local_server
python manage.py runserver
pause
