echo ck pull repo:ck-ml
ck pull repo:ck-ml

rem Install packages to CK env entries
echo ck setup kernel --var.install_to_env=yes
ck setup kernel --var.install_to_env=yes

echo ck detect platform.os --platform_init_uoa=generic-linux-dummy
ck detect platform.os --platform_init_uoa=generic-linux-dummy

echo ck detect soft:compiler.python --full_path=${CK_VENV_PYTHON_BIN}
ck detect soft:compiler.python --full_path=${CK_VENV_PYTHON_BIN}

echo ck detect soft:compiler.gcc --full_path=`which gcc`
ck detect soft:compiler.gcc --full_path=`which gcc`

echo ck detect soft:tool.cmake
ck detect soft:tool.cmake

echo ck install package --quiet --tags=mlperf,inference,src,r1.0
ck install package --quiet --tags=mlperf,inference,src,r1.0

echo ck install package --tags=lib,python-package,absl
ck install package --tags=lib,python-package,absl

echo ck install package --tags=lib,python-package,numpy
ck install package --tags=lib,python-package,numpy

echo ck install package --tags=lib,python-package,mlperf,loadgen
ck install package --tags=lib,python-package,mlperf,loadgen

echo ck show env
echo ============================================================
ck show env
