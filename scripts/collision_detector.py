#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Empty, Bool, Int32
from jsk_rviz_plugins.msg import OverlayText

num_collisions = 0
collision_pub = rospy.Publisher('/viz/collision', OverlayText, queue_size=10)
num_collision_pub = rospy.Publisher('/viz/num_collisions', OverlayText, queue_size=10, latch=True)
def collision_callback(data):
    global num_collisions
    num_collisions = num_collisions + 1
    has_collided = OverlayText(text=str('True'))
    collision_pub.publish(has_collided)
    text_collisions = OverlayText(text=str(num_collisions) + ' collision(s)')
    num_collision_pub.publish(text_collisions)

if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/uav/collision", Empty, collision_callback)
    rate = rospy.Rate(10)
    rospy.spin()