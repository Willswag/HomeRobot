#!/usr/bin/env python

"""
playing with generating initial approach points for robotic home assistant.
we need to know
1. the location of the appliance
2. number of approach able sides
3. the directions that the approach faces
4. distance to start approach from
"""

import PIL.Image
import rospy
from geometry_msgs.msg import Pose2D


example_appliance =  {
    "name":"refrigerator",
    "sides":4,
    "appro_dist":1.0,
    "location":{
        "x":0.0,
        "y":0.0,
        "az":0.0
        }
    }

class map:

    def __init__(self):
        self.map_image = PIL.Image.new(mode = "RGB", size = (200, 200)
        self.robot_poses = Pose2D[]

    def route_Planner(self, start_pose, end_pose ):
        # find optimal route
        pass

    def save_map_file(self,path):
        #write map file and poses to file
        pass

    def open_map(self,path):
        #open file for editing
        pass



class approach:

    def __init__(self,name):
        #define approach pyhthon object
        self.name = name
        self.pose = Pose2D()

    def create_approach(self,app_pose,dist):
        #generate an approach fix based on defined example_appliance
        self.pose.x = app_pose.x + cos(app_pose.x)*dist
        self.pose.y = app_pose.y + sin(app_pose.y)*dist

    def save_approach()
        #append poses list
        pass


main():
    pass


if __name__ == '__main__'
    main()
