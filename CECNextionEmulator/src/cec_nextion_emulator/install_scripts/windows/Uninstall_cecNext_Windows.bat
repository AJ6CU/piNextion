@echo off

SET "folder_name=CEC"
SET "default_ini_file=%USERPROFILE%\.CECNextionEmulator.ini"

RMDIR /s /q "%USERPROFILE%\Documents\%folder_name%"
DEL "%default_ini_file%"
