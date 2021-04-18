#! /bin/bash

#
# Installation script for Python
#
# See CK LICENSE for licensing details.
# See CK COPYRIGHT for copyright details.
#
# Developer(s):
# - Grigori Fursin, 2021
#

# PACKAGE_DIR
# INSTALL_DIR

cd ${INSTALL_DIR}

mkdir -p "install"

PACKAGE_NAME="Python-${PACKAGE_VERSION}"
PACKAGE_FILE="${PACKAGE_NAME}.tgz"

wget ${PACKAGE_URL}/${PACKAGE_VERSION}/${PACKAGE_FILE}

tar xvf ${PACKAGE_FILE}

rm -f ${PACKAGE_FILE}

cd $PACKAGE_NAME


echo "======================================================"
echo "Configuring (${CONFIGURATION_FLAGS}) ..."
echo ""
./configure ${CONFIGURATION_FLAGS} --prefix=${INSTALL_DIR}/install
if [ "${?}" != "0" ] ; then
  echo "Error: making failed!"
  exit 1
fi

echo "======================================================"
echo "Building ..."
echo ""
make -j ${CK_HOST_CPU_NUMBER_OF_PROCESSORS}
if [ "${?}" != "0" ] ; then
  echo "Error: building failed!"
  exit 1
fi

echo "======================================================"
echo "Installing to '${INSTALL_DIR}/install' ..."
echo ""
make install
if [ "${?}" != "0" ] ; then
  echo "Error: installing failed!"
  exit 1
fi

echo "======================================================"
echo "Installed Python to ${INSTALL_DIR}/install"

