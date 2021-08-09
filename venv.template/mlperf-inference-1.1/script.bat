@echo off

rem
rem Developer(s): 
rem  * Grigori Fursin, OctoML.ai
rem

set cur_path=%~dp0

call %cur_path%\common.bat ck pull repo:ck-mlops
if %errorlevel% neq 0 (exit /b 1)

rem Install packages to CK env entries
call %cur_path%\common.bat ck setup kernel --var.install_to_env=yes
if %errorlevel% neq 0 (exit /b 1)

call %cur_path%\common.bat ck detect soft:compiler.python --full_path=%CK_VENV_PYTHON_BIN%
if %errorlevel% neq 0 (exit /b 1)

call %cur_path%\common.bat ck install package --quiet --tags=mlperf,inference,src,r1.1
if %errorlevel% neq 0 (exit /b 1)

call %cur_path%\common.bat ck show env
if %errorlevel% neq 0 (exit /b 1)

exit /b 0
