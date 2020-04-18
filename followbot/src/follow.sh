#!/bin/bash -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.
export HOME=/home/suen
export TURTLEBOT3_MODEL=waffle pi
source /opt/ros/kinetic/setup.bash
source $HOME/catkin_ws/devel/setup.bash
roscore > $HOME/roscore.log 2>&1 &
sleep 30
roslaunch turtlebot3_slam turtlebot3_slam.launch  > $HOME/slam.log 2>&1 &
sleep 60
rosrun followbot FB.py > $HOME/followbot.log 2>&1 &
exit 0
