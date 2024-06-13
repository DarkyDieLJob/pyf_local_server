@echo off
cd %~dp0
call venv\Scripts\activate
cd local_server
python manage.py runserver 192.168.1.104:8080
python manage.py runserver 192.168.0.15:8080
pause
