#!/usr/bin/env python3
import subprocess
import datetime

file = "time.out"
open(file, 'w').close()

date = subprocess.check_output("cut -c 8- time.log | rev | cut -c 8- | rev", shell=True)
ary = date.decode().split()
size = len(ary) - 1

for i in range(0, size, 2):
    print(i, size)
    j = i + 1
    logdate = f"{ary[i]} {ary[j]}"
    if j == size:
        with open(file, 'a') as f:
            f.write(f"{logdate} 1\n")
        break
    k = j + 2
    t_old = datetime.datetime.strptime(logdate, "%Y-%m-%d %H:%M:%S").timestamp()
    t_new = datetime.datetime.strptime(f"{ary[i]} {ary[k]}", "%Y-%m-%d %H:%M:%S").timestamp()
    diff = int(t_new - t_old)

    with open(file, "a") as f:
        f.write(f"{logdate} 1\n")
        for l in range(2, diff + 1):
            t = int(t_old + l - 1)
            dt = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")
            if diff > 10:
                f.write(f"{dt} 0\n")
            else:
                f.write(f"{dt} 1\n")