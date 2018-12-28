#!/usr/bin/env python
import rospy,cv2,cv_bridge,numpy
from sensor_msgs.msg import Image

class Follower:
  def __init__(self):
    self.bridge = cv_bridge.CvBridge()
    self.image_sub = rospy.Subscriber('camera/rgb/image_raw',Image,self.image_callback)
  def image_callback(self,msg):
    image = self.bridge.imgmsg_to_cv2(msg)
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower_yellow = numpy.array([50,50,165])
    upper_yellpw = numpy.array([255,255,190])
    mask = cv2.inRange(hsv,lower_yellow,upper_yellpw)
    masked = cv2.bitwise_and(image,image,mask=mask)

    cv2.namedWindow('window',2)
    cv2.imshow('window',mask)
    cv2.waitKey(3)

    cv2.namedWindow('window2',2)
    cv2.imshow('window2',hsv)
    cv2.waitKey(3)


rospy.init_node('follower')
follower = Follower()
rospy.spin()
