#!/bin/bash -x

function track() {
  #Get file, and check if it exists. If not end program.
  logfile="log.txt"
  if [[ -f $logfile ]]; then
    echo "File exists and is a regular file."
  else
    echo "Couldnt find file. Make sure it exixts, and try again"
    exit
  fi

  #Runs if there is more then 0 arguments
  command=$1
  label=$2
  lastLineInLogfile=$(tail -1 "$logfile")

  case "$command" in
    "start")
    if [[ $label == "" ]]; then
      echo "Function track start needs 2 parameters: -track start [label]"
    elif [[ $lastLineInLogfile == "" || $lastLineInLogfile == END* ]]; then
      echo "START $(date)" | tee -a $logfile
      echo "LABEL ${label}" | tee -a $logfile
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
      echo "STATUS ${lastLineInLogfile:6}"  | tee -a $logfile
    else
      echo "No active task"
    fi
    ;;

    "log")
    startDate=""
    endDate=""
    declare -i diffrence
    taskCounter=1

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
    echo "How to use track. You need to write 'track [command]'"
    echo "  -track start [label]: Start task with [label]."
    echo "  -track stop: Stops current task, if active."
    echo "  -track status: Shows label of active task."
    echo "  -track log: Shows time spent on each task."

  esac

}
