# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:37:54 2020

@author: Andreas
"""

from task_simulator import plot_workload, make_taskset, sort_taskset

tasks = make_taskset([[50, 20, 60],
                      [80, 20, 50]])

tasks = sort_taskset(tasks, "RMA")
plot_workload(tasks)