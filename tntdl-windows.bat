@echo off
set /p SEARCH_QUERY=Cerca: 
set SEARCH_QUERY=%SEARCH_QUERY:"=\"%
cd %~dp0%
python tnt-downloader.py "%SEARCH_QUERY%"
pause