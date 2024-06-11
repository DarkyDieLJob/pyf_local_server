@echo off
cd %~dp0
call venv\Scripts\activate
cd local_server
set /p appname=Introduce el nombre de la aplicación: 
python manage.py startapp %appname%
pause
