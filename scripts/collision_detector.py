#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Empty, Bool, Int32

num_collisions = 0
collision_pub = rospy.Publisher('/viz/collision', Bool, queue_size=10)
num_collision_pub = rospy.Publisher('/viz/num_collisions', Int32, queue_size=10, latch=True)
def collision_callback(data):
    global num_collisions
    num_collisions = num_collisions + 1
    collision_pub.publish(Bool(True))
    num_collision_pub.publish(Int32(num_collisions))

if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/uav/collision", Empty, collision_callback)
    rate = rospy.Rate(10)
    rospy.spin()