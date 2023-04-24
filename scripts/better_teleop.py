#!/usr/bin/env python3

import pynput
from pynput.keyboard import Key

import rospy
from geometry_msgs.msg import Twist


class Teleop:

    directions = {
            Key.up: (1, 0),
            Key.down: (-1, 0),
            Key.left: (0, 1),
            Key.right: (0, -1)
    }

    def __init__(self):
        self._is_running = True
        self._listener = pynput.keyboard.Listener(
            on_press=self._on_press,
            on_release=self._on_release
        )
        self._listener.start()
        self._command = [0.0, 0.0]

        self._rates = {
                Key.up: rospy.get_param('~forward_rate', 2.0),
                Key.down: rospy.get_param('~backward_rate', 1.0),
                Key.left: rospy.get_param('~rotation_rate', 1.0),
                Key.right: rospy.get_param('~rotation_rate', 1.0)
        }
        
        self._cmd_topic = rospy.get_param("~cmd_topic", "/cmd_vel")
        self._cmd_pub = rospy.Publisher(self._cmd_topic, Twist, queue_size=10)

    def publish(self):
        msg = Twist()
        msg.linear.x = self._command[0]
        msg.angular.z = self._command[1]
        self._cmd_pub.publish(msg)

    def is_running(self):
        return self._is_running

    def _on_press(self, key):
        if key == Key.esc:
            self._is_running = False

        if key in Teleop.directions:
            cmd = Teleop.directions[key]
            for i in [0, 1]:
                if cmd[i] != 0:
                    self._command[i] = cmd[i] * self._rates[key]

    def _on_release(self, key):
        if key in Teleop.directions:
            cmd = Teleop.directions[key]
            for i in [0, 1]:
                if cmd[i] != 0:
                    self._command[i] = 0

    def __str__(self):
        return f"Forward: {self._command[0]}, Rotate: {self._command[1]}"


def main():
    rospy.init_node("better_teleop")
    teleop = Teleop()

    rate = rospy.Rate(20)
    while teleop.is_running():
        teleop.publish()
        rate.sleep()

    return 0


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
