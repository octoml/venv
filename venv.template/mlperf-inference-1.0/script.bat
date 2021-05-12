@echo off

rem
rem Developer(s): 
rem  * Grigori Fursin, OctoML.ai
rem

call common.bat ck pull repo:ck-ml
if %errorlevel% neq 0 (exit /b 1)

rem Install packages to CK env entries
call common.bat ck setup kernel --var.install_to_env=yes
if %errorlevel% neq 0 (exit /b 1)

call common.bat ck detect platform.os --platform_init_uoa=generic-linux-dummy
if %errorlevel% neq 0 (exit /b 1)

call common.bat ck detect soft:compiler.python --full_path=${CK_VENV_PYTHON_BIN}
if %errorlevel% neq 0 (exit /b 1)

call common.bat ck detect soft:compiler.gcc --full_path=`which gcc`
if %errorlevel% neq 0 (exit /b 1)

call common.bat ck detect soft:tool.cmake
if %errorlevel% neq 0 (exit /b 1)

call common.bat ck install package --quiet --tags=mlperf,inference,src,r1.0
if %errorlevel% neq 0 (exit /b 1)

call common.bat ck install package --tags=lib,python-package,absl
if %errorlevel% neq 0 (exit /b 1)

call common.bat ck install package --tags=lib,python-package,numpy
if %errorlevel% neq 0 (exit /b 1)

call common.bat ck install package --tags=lib,python-package,mlperf,loadgen
if %errorlevel% neq 0 (exit /b 1)

call common.bat ck install package --tags=lib,python-package,matplotlib
if %errorlevel% neq 0 (exit /b 1)

call common.bat ck install package --tags=lib,python-package,cython
if %errorlevel% neq 0 (exit /b 1)

call common.bat ck install package --tags=lib,python-package,opencv-python-headless
if %errorlevel% neq 0 (exit /b 1)

call common.bat ck install package --tags=tool,coco,api
if %errorlevel% neq 0 (exit /b 1)

call common.bat ck show env
if %errorlevel% neq 0 (exit /b 1)

exit /b 0
