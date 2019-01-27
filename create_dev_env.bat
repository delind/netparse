::Create virtual env and exit on any failure
call python -m venv ./env
@if %errorlevel% neq 0 (
    echo ERROR: failed to create venv!
    goto end
)
@call "env\Scripts\activate.bat"
@if %errorlevel% neq 0 (
    goto end
)
call python -m pip install pip -U
call pip install -e .
call pip install -r requirements_dev.txt
@echo Successfully created environment!
@call "env\Scripts\activate.bat"

:end
@echo %cmdcmdline% | find /i /c "/c" > nul && pause