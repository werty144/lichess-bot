#!/bin/bash
pip install -r requirements.txt

#The following code is for running a make file for stockfish
#
#MACHINE_TYPE=$(uname -m)
#if [ "${MACHINE_TYPE}" == 'x86_64' ]; then
#  (cd "engine/stockfish-11-linux/src" || exit ; make build ARCH=x86-64)
#else
#  (cd "engine/stockfish-11-linux/src" || exit ; make build ARCH=x86-32)
#fi

