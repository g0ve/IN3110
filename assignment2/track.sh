#!/bin/bash -x

function track() {
  logfile="LOGFILE.txt"
  command=$1
  label=$2
  lastLineInLogfile=$(tail -1 "$logfile")

  startDate=""
  endDate=""
  declare -i diffrence
  taskCounter=1

  #Get file, and check if it exists. If not end program.
  if [[ -f $logfile ]]; then
    echo "File exists and is a regular file."
  else
    echo "Didnt find file...File made."
    touch $logfile
  fi

  #Runs if there is more then 0 arguments

  case "$command" in
    "start")
    if [[ $label == "" ]]; then
      echo "Function track start needs 2 parameters: -track start [label]"
    elif [[ $lastLineInLogfile == "" || $lastLineInLogfile == END* ]]; then
      echo "START $(date)" | tee -a $logfile
      echo "LABEL This is: ${label}" | tee -a $logfile
    else
      echo "Another task is runnig. Stop it first with: track stop."
    fi
    ;;

    "stop")
    if [[ $lastLineInLogfile == LABEL* ]]; then
      echo "END $(date)" | tee -a $logfile
      echo "" | tee -a $logfile
    else
      echo "No task is running."
    fi
    ;;

    "status")
    if [[ $lastLineInLogfile == LABEL* ]]; then
      echo "STATUS ${lastLineInLogfile:6}"  #| tee -a $logfile
    else
      echo "No active task"
    fi
    ;;

    "log")

    while read lines; do
      if [[ $lines == START* ]]; then
        start="$(echo $lines | grep "START")"
        startDate=${start:6}
        startSec=$(date -d "$startDate" +%s)

      elif [[ $lines == END* ]]; then
        end="$(echo $lines | grep "END")"
        endDate=${end:4}
        endSec=$(date -d "$endDate" +%s)

        diffrence=endSec-startSec
        convertedDiff=$(date -u -d @${diffrence} +%T)
        echo "Task ${taskCounter}: ${convertedDiff}"
        ((taskCounter++))
      fi


    done < $logfile
    ;;

    *)

    echo "$(<README.md)"

  esac

}
