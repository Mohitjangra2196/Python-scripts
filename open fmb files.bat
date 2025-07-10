@echo off
setlocal

set "file_extension=.fmb"
set "log_file=log.txt"

REM Clear the log file at the beginning
> "%log_file%" echo Starting log for .fmb files...
>> "%log_file%" echo ----------------------------------

for %%f in (*%file_extension%) do (
    echo Opening "%%f"
    echo Opening "%%f" >> "%log_file%"
    start "" "%%f"
    pause
)

echo Done opening all %file_extension% files.
echo Done opening all %file_extension% files. >> "%log_file%"
endlocal
pause
