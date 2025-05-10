@echo off
setlocal

set "file_extension=.fmb"

for %%f in (*%file_extension%) do (
    echo Opening "%%f"
    start "" "%%f"
    pause
    taskkill /f /im "fmwdevenv.exe" /fi "windowtitle eq %%f" >nul 2>&1
)

echo Done opening all %file_extension% files.
endlocal
pause