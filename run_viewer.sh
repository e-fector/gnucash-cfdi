#!/bin/bash

archivo="$1"

variable=`which evince`
if [[  $variable == "" ]]
then
   echo "EVINCE NO INSTALADO"
else
   nohup evince $archivo
fi


variable=`which atril`
if [[  $variable == "" ]]
then
   echo "ATRIL NO INSTALADO"
else
   nohup atril $archivo
fi
