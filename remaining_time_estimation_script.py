# -*- coding: utf-8 -*-

"""
Following python script calls a lengthy job function in a for loop hundred times.

"""

import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from lenghty_job import lenghty_job

plt.style.use("seaborn-pastel")
plt.close("all")

loop_size = 100
durs, ests, job_sizes = [], [], []

t1 = time.time()
for i in range(loop_size):
    #do a lengthy job to make some delay
    t1_loop = time.time()
    job_size =lenghty_job()
    t2_loop = time.time()
    
    durs.append(t2_loop-t1_loop)
    job_sizes.append(job_size)
    
    #calculate remaining time dynamically
    est = mean(durs)*(loop_size-i-1)
    
    ests.append(est)
    print("Loop: %d Dur: %.2fs Remaining: %.2fs"%(i,t2_loop-t1_loop,est))
t2 = time.time()
print("Total Dur: %.2f sec"%(t2-t1))

cumsum_durs = pd.Series(durs).cumsum()
actual = np.linspace(t2-t1,0,loop_size)
real_time = np.linspace(0,sum(durs),loop_size)

plt.plot(real_time,actual,linewidth=5,linestyle="--")
plt.plot(real_time,ests,linewidth=3)
plt.xlabel("Time(s)")
plt.ylabel("Remaining Time(s)")
plt.title("Remaining Time Estimation",fontweight="bold")
plt.legend(["Actual","Predicted"])
plt.grid(linestyle=":")