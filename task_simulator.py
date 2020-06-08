# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:26:32 2020

@author: Andreas
"""

import numpy as np
import matplotlib.pyplot as plt

class Task:
    """Class for tasks"""
    def __init__(self, period, computation_time, deadline = None,
                 blocking_time = 0):
        """Initializes the task with various properties.

        period              -- period of the task
        computation_time    -- computation time of task
        deadline            -- deadline of task. If left at None the deadline
                               is sat equal to the period
        blocking_time       -- maximum blocking time of a task. (default 0)
        """
        self.T = period
        self.c = computation_time
        self.b = blocking_time
        self.d = [deadline, self.T][deadline is None]
        self.b = blocking_time

def make_taskset(arr):
    """Creates a taskset from an array consisting of arrays of arguments for
    the initialization of a Task.

    As an example if
        arr = [[50,20,60], [80,30,100]]
    A taskset consisting of T1:
        Period 50, Computation time 20, Deadline 60
    and a the task
        Period 80, Computation time 30, Deadline 100
    will be created
    """
    task_list = []
    for task_array in arr:
        task_list.append(Task(*task_array))
    return task_list

def sort_taskset(tasks, assignment):
    """Sorts tasks based on specific assignment"""
    if assignment == "RMA":
        return sorted(tasks, key=lambda t: t.T)
    elif assignment == "DMA":
        return sorted(tasks, key=lambda t: t.d)

def compute_critical_workload(task, prio_tasks):
    """Compute the critical workload of a task where prio_tasks is a taskset
    with tasks which have higher priority."""
    t = np.arange(1, task.d + 10)
    work = task.c + task.b
    if len(prio_tasks) == 0:
        work = np.full(task.d + 10, work)
    else:
        for prio_task in prio_tasks:
            work += np.ceil(t / prio_task.T) * prio_task.c
    return work

def compute_critical_workload_taskset(taskset):
    """The same as compute_critical_workload but for a complete taskset."""
    works = []
    for i, task in enumerate(taskset):
        priority = taskset[:i]
        works.append(compute_critical_workload(task, priority))
    return works

def find_first_idle(work):
    """Finds the first occurence of an idle instant for the work of one
    task."""
    t = 0
    while work[t] > t:
        t += 1
        if t >= len(work):
            return -1
    return t

def find_first_idles(works):
    """Finds the first occurence of an idle instant for each work array of a
    taskset."""
    idles = []
    for work in works:
        idles.append(find_first_idle(work))
    return idles

def plot_workload(taskset):
    """Creates a complete plot over critical workload, idle instants and
    the deadlines of a taskset."""
    works = compute_critical_workload_taskset(taskset)
    fig, axes = plt.subplots(len(works), 1)
    fig.set_size_inches(5,3.5 * len(works))
    for i, x in enumerate(works):
        t = np.arange(0, len(x))
        axes[i].axvline(find_first_idle(x), c="k", alpha=0.4, ls="--")
        axes[i].axvline(taskset[i].d, c="r", alpha=0.4, ls="--")
        axes[i].plot(t,t, "k")
        axes[i].plot(x, "g-")
        axes[i].set_title("Task #{}".format(i+1))

#tasks = make_taskset([[80, 20, 50], [50, 20, 60]])
#tasks = sort_taskset(tasks, "RMA")
#plot_workload(tasks)

#tasks = []
#tasks.append(Task(100, 10, 100))
#tasks.append(Task(1000*60*10, 10, 200))
#tasks.append(Task(1000, 10, 1000))
#tasks.append(Task(1000*10, 20, 1000*10))
#tasks.append(Task(1000*2, 10, 100))
#tasks.append(Task(1000*10, 30, 1000*2))
#
#plot_workload(tasks)