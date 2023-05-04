#!/bin/sh

file="time.out"
echo -n > $file
date=`cat time.log|cut -c 8-|rev|cut -c 8-|rev`
declare -a ary=(); declare -a ary=($date)

size=`expr ${#ary[*]} - 1`

for i in `seq 0 2 $size`
do
  echo $i $size
  j=`expr $i + 1`
  logdate=`echo ${ary[$i]} ${ary[$j]}`
  if [ $j -eq $size ]; then
    echo $logdate 1 >> $file
    break
  fi
  k=`expr $j + 2`
  t_old=`date -d "${ary[$i]} ${ary[$j]}" +%s`
  t_new=`date -d "${ary[$i]} ${ary[$k]}" +%s`
  diff=`expr $t_new - $t_old`

  echo $logdate 1 >> $file
  for l in `seq 2 $diff`
  do
    t=`expr $t_old + $l - 1`
    datetime=`date -d @$t +"%Y-%m-%d %H:%M:%S"`
    if [ $diff -gt 10 ]; then
      echo $datetime 0 >> $file
    else
      echo $datetime 1 >> $file
    fi
  done
done