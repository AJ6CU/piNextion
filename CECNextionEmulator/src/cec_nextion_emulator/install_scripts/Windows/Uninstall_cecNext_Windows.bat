REM @echo off

SET "VENV_DIR=%USERPROFILE%\Documents\CEC"
SET "default_ini_file=%USERPROFILE%\.CECNextionEmulator.ini"

RMDIR /s /q "%VENV_DIR%"
DEL "%default_ini_file%"
