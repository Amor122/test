#!/bin/sh
case $1 in  
   start) cd soo && celery -A soo beat -l info >  out.file  2>&1  & ;;
   stop) su root beat_stop.sh start ;; # 关闭beat(根据beat_stop.sh脚本的路径适当变化)
   *) echo "require start|stop" ;;
esac