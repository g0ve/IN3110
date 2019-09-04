#!/bin/bash -x

function climb (){
  declare -i n
  declare -i i

if [[ $# -gt 0 ]]; then #If number of arguments are greater then 0...run
  n=$1 #Number of climbs
  i=0 #Counter
  while [[ "$i" != "$n" ]]; do #While counter is not equal to number of climbs. Then cd ../
    cd ../
    i=$i+1
  done
else #If there is no arguments climb just 1 time
  cd ../
fi
}
