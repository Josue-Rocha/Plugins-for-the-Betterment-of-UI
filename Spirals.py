# Spirals.py
import maya.cmds as cmds
import numpy as np
import MASH.api as mapi

#Global Variables
num_points_global=100
radius_global= 5
height_global= 15
turns_global = 5
num_obj_global = 50
step_size_global = 1

def makeSpiral(num_points, radius, height, turns, num_obj, step_size):
    #cmds.polySphere()
    mashNetwork = mapi.Network()
    mashNetwork.createNetwork(name="HelloWorld")
    mashNetwork.setPointCount(1)
    cmds.setAttr("HelloWorld_Distribute.amplitudeX", 0)

    points_list = []
    theta = np.linspace(0, 2*np.pi*turns, num_points)
    z = np.linspace(0, height, num_points)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    spiral_coordinates = list(zip(x, z, y))
    print(spiral_coordinates)
    cmds.curve(n='CurveNado', p=spiral_coordinates)


    mash_curve_node = mashNetwork.addNode("MASH_Curve")
    cmds.connectAttr("CurveNado" + ".worldSpace[0]", "HelloWorld_Curve" + ".inCurves[0]", force=1)
    mashNetwork.setPointCount(num_obj)
    cmds.setAttr("HelloWorld_Curve.timeStep", step_size)


def makeWindow(winName):
    
    if (cmds.window(winName, exists = 1)):
        cmds.deleteUI(winName)

    cmds.window(winName, menuBar=True, resizeToFitChildren=1, width=280, height=100, title=winName)

    cmds.frameLayout(lv = 0);
    cmds.columnLayout(adjustableColumn=True)
    
    
    num_points = cmds.intSliderGrp("Number of Points", l= "Number of Points", v=num_points_global, min=10, max=500, field=True) # int slider group to get the number of many objects
    radius = cmds.intSliderGrp("Radius", l= "Radius", v=radius_global, min=-1, max=100, field=True) # int slider group to get how spread out everything is
    height = cmds.floatSliderGrp("Height", l= "Height", v=height_global, min=1, max=100, pre=3, field=True) # float slider group to affect the wave length of the spiral
    turns = cmds.intSliderGrp("Turns", l= "Turns", v=turns_global, min=5, max=100, field=True) # float slider group to affect the wave length of the spiral
    num_obj = cmds.intSliderGrp("Number of Objects", l= "Number of Objects", v=num_obj_global, min=1, max=100, field=True) # float slider group to affect the wave length of the spiral
    step_size = cmds.floatSliderGrp("Step Size", l= "Step Size", v=step_size_global, min=0, max=1, pre=3, field=True) # float slider group to affect the wave length of the spiral

    
    cmds.separator(height=20,width=400)
    cmds.button(l="Create the Spiral", c=lambda x: makeSpiral(cmds.intSliderGrp(num_points, q=True, value=True), cmds.intSliderGrp(radius, q=True, value=True), cmds.floatSliderGrp(height, q=True, value=True), cmds.intSliderGrp(turns, q=True, value=True), cmds.intSliderGrp(num_obj, q=True, value=True), cmds.floatSliderGrp(step_size, q=True, value=True)))

    
    cmds.showWindow(winName)
    
makeWindow("Spirals")
