@echo off
setlocal

set "file_extension=.txt"

for %%f in (*%file_extension%) do (
    echo Opening "%%f"
    start "" "%%f"
    pause
    taskkill /f /im "notepad.exe" /fi "windowtitle eq %%f - Notepad" >nul 2>&1
)

echo Done opening all %file_extension% files.
endlocal
pause