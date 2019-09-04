#!/bin/bash -x

function track() {
  #All varibels used declared
  logfile="LOGFILE.txt"
  command=$1
  label=$2
  lastLineInLogfile=$(tail -1 "$logfile")

  startDate=""
  endDate=""
  declare -i diffrence
  taskCounter=1

  #Get file, and check if it exists. If not creates logfil for you
  if [[ -f $logfile ]]; then
    echo "File exists and is a regular file."
  else
    echo "Didnt find file...File made."
    touch $logfile
  fi

  #I wanted to try and use case instead of if-sentences
  #If command(first argument) is "start" then do a task, same goes with stop, status and log
  case "$command" in

    "start") #track start [label]
    if [[ $label == "" ]]; then #If there is no label, ask user to add a second parameter
      echo "Function track start needs 2 parameters: -track start [label]"
    elif [[ $lastLineInLogfile == "" || $lastLineInLogfile == END* ]]; then #elif last line in LOGFILE is an empty line or it starts with END, you can run a task
      echo "START $(date)" | tee -a $logfile
      echo "LABEL This is: ${label}" | tee -a $logfile
    else
      echo "Another task is runnig. Stop it first with: track stop."
    fi
    ;;

    "stop") #track stop
    if [[ $lastLineInLogfile == LABEL* ]]; then #if last line in LOGFILE starts with label means a task is running and you can stop it
      echo "END $(date)" | tee -a $logfile
      echo "" | tee -a $logfile
    else
      echo "No task is running."
    fi
    ;;

    "status")
    if [[ $lastLineInLogfile == LABEL* ]]; then #same has "stop", but here it removes the 6 first characters in the last line
      echo "STATUS ${lastLineInLogfile:6}"  #| tee -a $logfile
    else
      echo "No active task"
    fi
    ;;

    "log")
    while read lines; do #Reads the LOGFILE

      if [[ $lines == START* ]]; then #If a line starts with START, remove 6 first characters and declare rest of line to a varibel
        start="$(echo $lines | grep "START")"
        startDate=${start:6}
        startSec=$(date -d "$startDate" +%s) #With %s we can convert a "date" type to seconds.

      elif [[ $lines == END* ]]; then
        end="$(echo $lines | grep "END")" #Does the same has START first, but it gets the END date instead
        endDate=${end:4}
        endSec=$(date -d "$endDate" +%s)

        #Calculate the diffrence in seconds between end and start
        diffrence=endSec-startSec
        convertedDiff=$(date -u -d @${diffrence} +%T) #With %T we can convert a "date" type to this format: HH:MM:SS
        echo "Task ${taskCounter}: ${convertedDiff}"
        ((taskCounter++))
      fi

    done < $logfile
    ;;

    *) #If none of the cases work this runs.
    echo "$(<README.md)" #Prints out how to use the program to user from README file
    ;;
    
  esac
}
