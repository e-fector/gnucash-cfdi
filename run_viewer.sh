#!/bin/bash

archivo="$1"

variable=`which evince`
if [[  $variable == "" ]]
then
   sleep 0
   #echo "EVINCE NO INSTALADO"
else
   nohup evince $archivo &
fi


variable=`which atril`
if [[  $variable == "" ]]
then
   sleep 0
   #echo "ATRIL NO INSTALADO"
else
   nohup atril $archivo &
fi
