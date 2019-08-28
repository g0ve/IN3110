#!/bin/bash

function climb() {
  declare -i n
  declare -i i

if [ $# -gt 0 ]; then
  n=$1
  i=1
  while [ "$i" != "$n" ]; do
    cd ../
    i=$i+1
  done
fi
}
