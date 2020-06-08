# Task simulator

This module is written to enable the feasibility check of a set of tasks on an embedded system processor. The module is capable of calculating the outstanding work, that a CPU may experience under a critical instant where all tasks are ready at once, and as such the module *simulates* a critical instant. The module is also capable of finding the first idle instant where the amount of outstanding work is 0. Lastly the module may plot this in a graph like the one below:

![A graph produced by this module](https://i.imgur.com/1Ho30ky.png)

The green line represents the outstanding work created by the taskset in seconds. The black line is the amount of work the CPU is capable  of (exactly 1 s/s). The grey dashed line represents a critical instant. The red dashed line represents the deadline of a task. An example *example.py* is included which produces the image shown above.