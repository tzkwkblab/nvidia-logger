#!/bin/bash

PREFIX='/home/himkt/nvidia-logger'

HOST=`cat /etc/hosts| grep -e 'gamma' -e 'digamma'| cut -f 3| sed -e 's/ //g'`
DATE=`date "+%Y%m%d"`
DATETIME=`date "+%Y%m%d-%H:%M"`

FNAME=${HOST}_${DATE}.xml
FPATH=`echo $PREFIX/$FNAME| sed -e 's/ //g'`

/usr/bin/nvidia-smi -q -x > $FPATH
/usr/bin/python3 `echo $PREFIX/parse.py| sed -e 's/ //g'` $FPATH $DATETIME
rm $FPATH
