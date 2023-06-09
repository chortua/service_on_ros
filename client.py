#!/usr/bin/env python

import sys
import rospy
from service_node.srv import AddTwoInts
from service_node.srv import AddTwoIntsRequest
from service_node.srv import AddTwoIntsResponse

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        respl = add_two_ints(x, y)
        print(x, y)
        return respl.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x, y]" %sys.argv[0]
if __name__=="__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s+%s"%(x, y))
    print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))