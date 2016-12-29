#!/bin/bash

git submodule init
git submodule update

# determine whether we're on openshift
DIR_OUTPUT=${OPENSHIFT_DATA_DIR:?"./src/build"}
DIR_TEMP=${OPENSHIFT_DATA_DIR:?"./tmp"}

# install autoconf
cd $DIR_TEMP
wget http://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz
tar xzf autoconf-2.69.tar.gz
cd autoconf-2.69
./configure --prefix=$DIR_OUTPUT
make
make install DESTDIR=$DIR_OUTPUT

export PATH=$DIR_OUTPUT/usr/local/bin:$PATH
export LD_LIBRARY_PATH=$DIR_OUTPUT/var/lib

# install automake
cd $DIR_TEMP
wget http://ftp.gnu.org/gnu/automake/automake-1.15.tar.gz
tar xzf automake-1.15.tar.gz
cd automake-1.15
./configure --prefix=$DIR_OUTPUT
make
make install DESTDIR=$DIR_OUTPUT

# libtool
cd $DIR_TEMP
wget http://ftp.gnu.org/gnu/libtool/libtool-2.4.6.tar.gz
tar xzf libtool-2.4.6.tar.gz
cd libtool-2.4.6
./configure --prefix=$DIR_OUTPUT
make
make install DESTDIR=$DIR_OUTPUT

# install python

#alias aclocal-1.15='aclocal'

#ln -s /usr/bin/aclocal ${$DIR_OUTPUT}bin/aclocal-1.15

# install bison
