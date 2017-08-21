@echo off
set /p SEARCH_QUERY=Cerca: 
set SEARCH_QUERY=%SEARCH_QUERY:"=\"%
cd %~dp0%
set EXC_PATH=%~dp0%\tnt-downloader.py
python %EXC_PATH% "%SEARCH_QUERY%"
pause