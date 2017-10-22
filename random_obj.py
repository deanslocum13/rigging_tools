'''
Dean Slocum
random_obj.py

Description:

	Allows the user to create a randomized set of polygonal objects based on gui menu selections.
	
	Gives the user control over:
		-- Object type
		-- Number of objects
		-- Area scale
		-- Max object scale

How to Run:

import random_obj
reload(random_obj)
random_obj.gui()

'''

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel

import random

win = 'Random Object Tool Kit'
print 'Random Object Tool Kit Activated'

w = 270
h = 150

w2 = 40

def gui():

	if(cmds.window(win , ex=1)):
		cmds.deleteUI(win)
	if (cmds.windowPref(win , ex=1)):
		cmds.windowPref(win , r=1)

	global polygon_choice, obj_no, area_no, scale_no

	cmds.window(win , s=1, vis=1, w=w , h=h)

	cmds.rowColumnLayout(w=w,h=h)

	cmds.text(l='')

	polygon_choice = pm.radioButtonGrp(la4=['Cube', 'Sphere', 'Cylinder', 'plane'], nrb=4, cw4=[67,67,67,67], sl=1)

	cmds.text(l='', h=8)

	cmds.rowColumnLayout(nc=2)

	cmds.text(l='Number of Objects:')
	obj_no = pm.intField(v=10, w=w2)

	cmds.text(l='Area Scale:')
	area_no = pm.intField(v=11, w=w2)

	cmds.text(l='Max Object Scale:')
	scale_no = pm.intField(v=1, w=w2)

	cmds.text(l='')
	cmds.text(l='')

	cmds.button(l='do shit',c=do_shit)

	cmds.showWindow()

def do_shit(*args):

	obj_no_input = obj_no.getValue()
	area_no_input = area_no.getValue()
	scale_no_input = scale_no.getValue()

	if polygon_choice.getSelect() == 1:
		stuff = []
		for i in range(obj_no_input):
			result = cmds.polyCube()
			# cmds.xform(r=1, ro=(random_no1,random_no2,random_no3))
			stuff.append(result)
			for i in result:
				random_t_no1 = random.randint(-area_no_input,area_no_input)
				random_t_no2 = random.randint(-area_no_input,area_no_input)
				random_t_no3 = random.randint(-area_no_input,area_no_input)
				random_ro_no1 = random.randint(0,361)
				random_ro_no2 = random.randint(0,361)
				random_ro_no3 = random.randint(0,361)
				random_s_no1 = random.randint(1,scale_no_input)

				cmds.xform(a=1, t=(random_t_no1,random_t_no2,random_t_no3))
				cmds.xform(a=1, ro=(random_ro_no1,random_ro_no2,random_ro_no3))
				cmds.xform(a=1, s=(random_s_no1,random_s_no1,random_s_no1))

	if polygon_choice.getSelect() == 2:
		stuff = []
		for i in range(obj_no_input):
			result = cmds.polySphere()
			# cmds.xform(r=1, ro=(random_no1,random_no2,random_no3))
			stuff.append(result)
			for i in result:
				random_t_no1 = random.randint(-area_no_input,area_no_input)
				random_t_no2 = random.randint(-area_no_input,area_no_input)
				random_t_no3 = random.randint(-area_no_input,area_no_input)
				random_ro_no1 = random.randint(0,361)
				random_ro_no2 = random.randint(0,361)
				random_ro_no3 = random.randint(0,361)
				random_s_no1 = random.randint(1,scale_no_input)

				cmds.xform(a=1, t=(random_t_no1,random_t_no2,random_t_no3))
				cmds.xform(a=1, ro=(random_ro_no1,random_ro_no2,random_ro_no3))
				cmds.xform(a=1, s=(random_s_no1,random_s_no1,random_s_no1))
	if polygon_choice.getSelect() == 3:
		stuff = []
		for i in range(obj_no_input):
			result = cmds.polyCylinder()
			# cmds.xform(r=1, ro=(random_no1,random_no2,random_no3))
			stuff.append(result)
			for i in result:
				random_t_no1 = random.randint(-area_no_input,area_no_input)
				random_t_no2 = random.randint(-area_no_input,area_no_input)
				random_t_no3 = random.randint(-area_no_input,area_no_input)
				random_ro_no1 = random.randint(0,361)
				random_ro_no2 = random.randint(0,361)
				random_ro_no3 = random.randint(0,361)
				random_s_no1 = random.randint(1,scale_no_input)

				cmds.xform(a=1, t=(random_t_no1,random_t_no2,random_t_no3))
				cmds.xform(a=1, ro=(random_ro_no1,random_ro_no2,random_ro_no3))
				cmds.xform(a=1, s=(random_s_no1,random_s_no1,random_s_no1))
	elif polygon_choice.getSelect() == 4:
		stuff = []
		for i in range(obj_no_input):
			result = cmds.polyPlane()
			# cmds.xform(r=1, ro=(random_no1,random_no2,random_no3))
			stuff.append(result)
			for i in result:
				random_t_no1 = random.randint(-area_no_input,area_no_input)
				random_t_no2 = random.randint(-area_no_input,area_no_input)
				random_t_no3 = random.randint(-area_no_input,area_no_input)
				random_ro_no1 = random.randint(0,361)
				random_ro_no2 = random.randint(0,361)
				random_ro_no3 = random.randint(0,361)
				random_s_no1 = random.randint(1,scale_no_input)

				cmds.xform(a=1, t=(random_t_no1,random_t_no2,random_t_no3))
				cmds.xform(a=1, ro=(random_ro_no1,random_ro_no2,random_ro_no3))
				cmds.xform(a=1, s=(random_s_no1,random_s_no1,random_s_no1))

	cmds.select(cl=1)		










