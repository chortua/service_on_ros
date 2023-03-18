#!/usr/bin/env python

from service_node.srv import AddTwoInts
from service_node.srv import AddTwoIntsRequest
from service_node.srv import AddTwoIntsResponse

import rospy
def handle_add_two_ints(req):
    print("Returning [%s + %s = %s]"%(req.a, req.b, ( req.a + req.b)))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin() #start and wait for incoming messages.

if __name__ == "__main__":
    add_two_ints_server()