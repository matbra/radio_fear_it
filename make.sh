#!/bin/bash

git submodule init
git submodule update

# install autoconf
cd $OPENSHIFT_TMP_DIR
wget http://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz
tar xzf autoconf-2.69.tar.gz
cd autoconf-2.69
./configure --prefix=$OPENSHIFT_DATA_DIR
make
make install DESTDIR=$OPENSHIFT_DATA_DIR

# install automake
cd $OPENSHIFT_TMP_DIR
wget http://ftp.gnu.org/gnu/automake/automake-1.15.tar.gz
tar xzf automake-1.15.tar.gz
cd automake-1.15
./configure --prefix=$OPENSHIFT_DATA_DIR
make
make install DESTDIR=$OPENSHIFT_DATA_DIR

# libtool
cd $OPENSHIFT_TMP_DIR
wget http://ftp.gnu.org/gnu/libtool/libtool-2.4.6.tar.gz
tar xzf libtool-2.4.6.tar.gz
cd libtool-2.4.6
./configure --prefix=$OPENSHIFT_DATA_DIR
make
make install DESTDIR=$OPENSHIFT_DATA_DIR

# install bison
