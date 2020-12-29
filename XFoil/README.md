# How I did the 2D sims in XFoil 
## init
1) Download and install XFoil
2) Learn how to use it
3) Load 642015 airfoil into it
4) cmd_RDEF_ to get my XFoil settings

## setup
4) Increase the panelling to reduce the max panel angle
    - use cmd _PANE_
    - then use cmd _PPAR_ and hit enter to verify that the panelling changed
5) Enter simulation by using cmd _OPER_
6) cmd _v_ to begin viscous mode 
7) cmd _Re_ _800000_ to set the Reynolds number

## simulate
6) cmd _Re_ _800000_ to set the Reynolds number 
7) cmd _p_ to enter polar accumulation mode
8) cmd _as_ -3 20 .5 to track data over a sequence of alphas
9) cmd _p_ to disable polar accumulation mode
10) cmd _pp_ to display the polar 
11) use _ppax_ to change the axis limits if necessary
