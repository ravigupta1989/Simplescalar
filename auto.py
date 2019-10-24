###!/usr/bin/python

def run_command(cmd, result_l):
    output = subprocess.check_output(cmd, shell=True)
    result_l.append(output)
    print cmd+" finished"

###Insert Python code
import os
import time
import subprocess

bench_list=["gcc","perl"]
simulator="~/project_RRIP/simplescalar_kalla/simulator/ss3/sim-outorder"
cache_p=["l","S","B"]

from multiprocessing import Process, Manager
result_l=Manager().list()
procs = []

# instantiating process with arguments
for bench in bench_list:
    # print(name)
    cmdline='./Run.pl -db ./bench.db -dir results/'+ bench +'1 -benchmark '+ bench +' -sim '+ simulator +' -args " -cache:dl1 dl1:512:16:2:B -cache:dl2 ul2:1024:32:16:B -fastfwd 50000000 -max:inst 20000000" 2>&1 | grep IPC'
    proc = Process(target=run_command, args=(cmdline,result_l))
    procs.append(proc)
    proc.start()

# complete the processes
for proc in procs:
    proc.join()
