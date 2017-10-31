#!/bin/bash

PREFIX='/root/nvidia-logger'

HOST=`cat /etc/hosts| grep -e 'gamma' -e 'digamma'| cut -f 3| sed -e 's/ //g'`
DATE=`date "+%Y%m%d-%H:%M.%S"`.xml
FNAME=${HOST}_${DATE}

FPATH=`echo $PREFIX/$FNAME| sed -e 's/ //g'`

/usr/bin/nvidia-smi -q -x > $FPATH
/usr/bin/python3 `echo $PREFIX/parse.py| sed -e 's/ //g'` $FPATH
rm $FPATH
