#!/bin/bash
#OMEGA_HOME=/cave/omegalib/new/omegalib
#Omegalib_Dir=/cave/omegalib/new/omegalib

#python -m SimpleHTTPServer&
#PPID=$!
export OMEGA_HOME=/cave/omegalib/new/omegalib
export Omegalib_DIR=/cave/omegalib/new/omegalib
export PATH=${OMEGA_HOME}/bin:${PATH}

/cave/omegalib/new/omegalib/bin/orun -s mapview.py

#echo "Killing $PPID"
#kill $PPID
