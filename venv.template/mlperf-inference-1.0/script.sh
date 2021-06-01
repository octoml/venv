#! /bin/bash
#
# Developer(s): 
#  * Grigori Fursin, OctoML.ai
#

function ck_command {

  echo "*************************************************************"
  echo "$1"
  echo ""

  $1

  if [ "${?}" != "0" ]; then 
    exit 1; 
  fi

}

ck_command "ck pull repo:ai"

# Install packages to CK env entries
ck_command "ck setup kernel --var.install_to_env=yes"

ck_command "ck detect platform.os --platform_init_uoa=generic-linux-dummy"

ck_command "ck detect soft:compiler.python --full_path=${CK_VENV_PYTHON_BIN}"

ck_command "ck detect soft:compiler.gcc --full_path=`which gcc`"


# Install pip packages
ck_command "python3 -m pip install protobuf"


#ck_command "ck detect soft:tool.cmake"
ck_command "ck install package --quiet --tags=tool,cmake,src"

ck_command "ck install package --quiet --tags=mlperf,inference,src,r1.0"

ck_command "ck install package --tags=lib,python-package,absl"

ck_command "ck install package --tags=lib,python-package,numpy"

ck_command "ck install package --tags=lib,python-package,mlperf,loadgen"

ck_command "ck install package --tags=lib,python-package,matplotlib"

ck_command "ck install package --tags=lib,python-package,cython"

ck_command "ck install package --tags=lib,python-package,opencv-python-headless"

ck_command "ck install package --tags=tool,coco,api"

ck_command "ck show env"
