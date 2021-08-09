@echo off

rem
rem Developer(s): 
rem  * Grigori Fursin, OctoML.ai
rem

set cur_path=%~dp0

call %cur_path%\common.bat ck pull repo:octoml@mlops
if %errorlevel% neq 0 (exit /b 1)

rem Install packages to CK env entries
call %cur_path%\common.bat ck setup kernel --var.install_to_env=yes
if %errorlevel% neq 0 (exit /b 1)

call %cur_path%\common.bat ck detect platform.os --platform_init_uoa=generic-linux-dummy
if %errorlevel% neq 0 (exit /b 1)

call %cur_path%\common.bat ck detect soft:compiler.python --full_path=%CK_VENV_PYTHON_BIN%
if %errorlevel% neq 0 (exit /b 1)

exit /b 0
