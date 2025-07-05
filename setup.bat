@echo off
REM This batch file runs s_cut.py to create a desktop shortcut for NexusTrade

cd /d "%~dp0"
python s_cut.py

pause