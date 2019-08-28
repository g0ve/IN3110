#!/bin/bash -x

function climb (){
  declare -i n
  declare -i i

if [[ $# -gt 0 ]]; then
  n=$1
  i=0
  while [[ "$i" != "$n" ]]; do
    cd ../
    i=$i+1
  done
else
  cd ../
fi
}
