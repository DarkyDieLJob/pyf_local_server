@echo off
cd %~dp0
call venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
echo.
echo ¡Actualización completada!
pause
