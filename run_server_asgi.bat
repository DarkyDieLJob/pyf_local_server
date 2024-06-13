@echo off
cd %~dp0
call venv\Scripts\activate
cd local_server
daphne local_server.asgi:application
pause
