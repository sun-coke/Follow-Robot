# followbot
The basic steps of the project :
1.Collcet the image information and pass it to Opencv
2.Filter the image to find the center of line
3.Manipulate the robot to keep running in the center of line



# Followbot Demo

## A、Install

### 1. First, you should clone the repository and compile workspace with catkin_make:

```
$ cd catkin_ws/src
$ git clone https://github.com/sun-coke/follow-bot.git
$ cd .. && catkin_make
```

## B、Run

### 1. running the followbot demo in gazebo:

```
$ cd catkin_ws/src/followbot/src && chmod +x follower_p.py
$ roslaunch followbot course.launch  
$ rosrun followbot follower_p.py
```
