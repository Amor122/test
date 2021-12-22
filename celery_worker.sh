#!/bin/sh 
case $1 in                                        
   start) cd soo && celery multi start w1 -A  soo -l info;;
   stop) cd soo && celery multi stop w1 -A  soo  -l info;;
   *) echo "require start|stop" ;;     
esac