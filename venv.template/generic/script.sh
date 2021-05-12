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

ck_command "ck pull repo:ck-ml"

# Install packages to CK env entries
ck_command "ck setup kernel --var.install_to_env=yes"

ck_command "ck detect platform.os --platform_init_uoa=generic-linux-dummy"

ck_command "ck detect soft:compiler.python --full_path=${CK_VENV_PYTHON_BIN}"

ck_command "ck detect soft:compiler.gcc --full_path=`which gcc`"

ck_command "ck show env"
