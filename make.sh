#!/bin/bash

git submodule init
git submodule update

cd $OPENSHIFT_TMP_DIR
wget http://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz
tar xzf autoconf-2.69.tar.gz
cd autoconf-2.69.tar.gz
./configure --prefix=$OPENSHIFT_DATA_DIR