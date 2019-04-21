# -*- coding: utf-8 -*-

"""
Following python script calls a lengthy job function in a for loop hundred times.
Dynamic visualisation of the loop

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

#dynamic plotting of the predictions
import matplotlib.animation as an
from matplotlib.gridspec import GridSpec

gs = GridSpec(1,2,width_ratios=[10,1])

fig = plt.figure(figsize=(12,5))
fig.subplots_adjust(wspace=0.305)
ax = fig.add_subplot(gs[0,0])
ax2 = fig.add_subplot(gs[0,1])

lines = []
delay = 100

for i in range(len(real_time)): 
    line1, = ax.plot(real_time[:i],actual[:i],linewidth=5,linestyle="--",c="sandybrown")
    line2, = ax.plot(real_time[:i],ests[:i],linewidth=3,c="cornflowerblue")
    line3, = ax2.bar(0,job_sizes[i],color="cornflowerblue")
    lines.append([line1,line2,line3])
    
ax.grid(linestyle=":")
ax.set_xlabel("Time(s)")
ax.set_ylabel("Remaining Time(s)")
ax.set_title("Remaining Time Estimation",fontweight="bold")
ax.legend(["Actual","Predicted"])
ax2.tick_params(axis="x",labelbottom=False)
ax2.set_title("Job Size",fontweight="bold")
ax2.set_ylabel("For Loop: Number of Iterations")
anim = an.ArtistAnimation(fig,lines,interval = delay)

#use pillowWriters for saving gif files
anim.save("Remaining Time.gif",writer="pillow")
