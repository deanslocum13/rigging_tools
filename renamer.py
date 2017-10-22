'''
Dean Slocum
renamer.py

Description:

	A tool kit window with all my renaming tools.

How to Run:

import renamer
reload(renamer)
renamer.gui()

'''

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
from functools import partial

win = 'Renaming Kit'
print 'Renaming Kit Activated'

w = 90
h = 180
h2 = 8
b1 = [0,.5,0]
b2 = [0,.5,.5]

def gui():

	global prefix_input, name_input, number_input, suffix_input
	global sel_box, waste_box, sel_box_2, search_input, replace_input

	if(cmds.window(win , ex=1)):
		cmds.deleteUI(win)
	if (cmds.windowPref(win , ex=1)):
		cmds.windowPref(win , r=1)

	cmds.window(win , s=0, vis=1, w=w , h=h)
	
	cmds.rowColumnLayout()

	cmds.frameLayout(l='RENAME', bgc=b1)

	cmds.rowColumnLayout(co=[1,'both',16])
	cmds.rowColumnLayout(nc=4)
	cmds.text('Prefix')
	cmds.text('Name')
	cmds.text('#')
	cmds.text('Suffix')
	prefix_input = pm.textField(w=50)
	name_input = pm.textField(w=75)
	number_input = pm.textField(w=40, en=0)
	suffix_input = pm.textField(w=75)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)

	cmds.setParent('..')

	cmds.rowColumnLayout(nc=2, co=[1,'both',9])

	sel_box = pm.checkBox(l='Switch to Selected', onc=partial(enableNumber, number_input), ofc=partial(disableNumber, number_input))
	waste_box = pm.checkBox(l='Include Waste')

	cmds.setParent('..')

	cmds.rowColumnLayout(nc=2, co=[1,'both',9])

	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.button(l='Rename', c=rename, bgc=b2)
	cmds.text('Default is set to Hierarchy.', en=0)

	cmds.setParent('..')

	cmds.text(' ', h=h2)
	cmds.text('Suffix can be: geo, icon, pad, local, bind', en=0)

	cmds.setParent('..')

	cmds.rowColumnLayout()

	cmds.setParent('..')
	cmds.setParent('..')

	cmds.frameLayout(l='SEARCH & REPLACE', bgc=b1)

	cmds.rowColumnLayout(co=[1,'both',16])
	cmds.rowColumnLayout(nc=2)
	cmds.text('Search for:')
	cmds.text('Replace with:')
	search_input = pm.textField(w=120)
	replace_input = pm.textField(w=120)

	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)

	cmds.setParent('..')

	cmds.rowColumnLayout(nc=1, co=[1,'both',50])

	sel_box_2 = pm.checkBox(l='Switch to Selected')

	cmds.setParent('..')

	cmds.rowColumnLayout(nc=2, co=[1,'both',9])

	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.button(l='Replace', c=replace, bgc=b2)
	cmds.text('Default is set to Hierarchy.', en=0)
	cmds.text(' ', h=h2)

	cmds.setParent('..')

	cmds.showWindow()

def enableNumber(number_field, *args):
    #enable the text field
    cmds.textField(number_field, e=1, en=1)

def disableNumber(number_field, *args):
    #disable the text field
    cmds.textField(number_field, e=1, en=0)

def rename(*args):
	# 'if (something)' is the same as 'if something =='

	if suffix_input.getText() == 'geo' and sel_box.getValue() == True:
		geo_sel()
	elif suffix_input.getText() == 'geo' and sel_box.getValue() == False:
		geo_hier()

	elif suffix_input.getText() == 'icon' and sel_box.getValue() == True:
		icon_sel()
	elif suffix_input.getText() == 'icon' and sel_box.getValue() == False:
		icon_hier()

	elif suffix_input.getText() == 'pad' and sel_box.getValue() == True and waste_box.getValue() == True:
		pad_sel_waste()
	elif suffix_input.getText() == 'pad' and sel_box.getValue() == True and waste_box.getValue() == False:
		pad_sel()
	elif suffix_input.getText() == 'pad' and sel_box.getValue() == False and waste_box.getValue() == True:
		pad_hier_waste()
	elif suffix_input.getText() == 'pad' and sel_box.getValue() == False and waste_box.getValue() == False:
		pad_hier()

	elif suffix_input.getText() == 'local' and sel_box.getValue() == True and waste_box.getValue() == True:
		local_sel_waste()
	elif suffix_input.getText() == 'local' and sel_box.getValue() == True and waste_box.getValue() == False:
		local_sel()
	elif suffix_input.getText() == 'local' and sel_box.getValue() == False and waste_box.getValue() == True:
		local_hier_waste()
	elif suffix_input.getText() == 'local' and sel_box.getValue() == False and waste_box.getValue() == False:
		local_hier()

	elif suffix_input.getText() == 'bind' and sel_box.getValue() == True and waste_box.getValue() == True:
		bind_sel_waste()
	elif suffix_input.getText() == 'bind' and sel_box.getValue() == True and waste_box.getValue() == False:
		bind_sel()
	elif suffix_input.getText() == 'bind' and sel_box.getValue() == False and waste_box.getValue() == True:
		bind_hier_waste()
	elif suffix_input.getText() == 'bind' and sel_box.getValue() == False and waste_box.getValue() == False:
		bind_hier()

	elif suffix_input.getText() != 'geo' and suffix_input.getText() != 'icon' and suffix_input.getText() != 'pad' and suffix_input.getText() != 'local' and suffix_input.getText() != 'bind':
		wrong_spelling()

def wrong_spelling(*args):
	cmds.inViewMessage(amg='You spelled the SUFFIX wrong!', pos='midCenter', fade=True, fts=35 ,fst=3000, bkc=0x00990000, a=1, ta=1)
	# cmds.error('YOU SPELLED THE SUFFIX WRONG!', n=0)

def geo_hier(*args):
	sel = pm.ls(selection=True, dag=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = -1
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2:02d}_{3}'.format(prefix, name, count, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

def geo_sel(*args):
	sel = pm.ls(selection=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = -1
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2}_{3}'.format(prefix, name, number, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

def icon_hier(*args):
	sel = pm.ls(selection=True, dag=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = 1
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2:02d}_{3}'.format(prefix, name, count, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

def icon_sel(*args):
	sel = pm.ls(selection=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = 1
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2}_{3}'.format(prefix, name, number, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

def pad_hier(*args):
	sel = pm.ls(selection=True, dag=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = -1
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2:02d}_{3}'.format(prefix, name, count, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

def pad_sel(*args):
	sel = pm.ls(selection=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = -1
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2}_{3}'.format(prefix, name, number, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

def pad_hier_waste(*args):
	sel = pm.ls(selection=True, dag=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = -1
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2:02d}_{3}'.format(prefix, name, count, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

	new_name = '{0}_{1}_{2:02d}_{3}'.format(prefix, name, count, 'waste')
	each.rename(new_name)

def pad_sel_waste(*args):
	sel = pm.ls(selection=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = -1
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2}_{3}'.format(prefix, name, number, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

	new_name = '{0}_{1}_{2:02d}_{3}'.format(prefix, name, count, 'waste')
	each.rename(new_name)

def local_hier(*args):
	sel = pm.ls(selection=True, dag=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = 0
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2:02d}_{3}'.format(prefix, name, count, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

def local_sel(*args):
	sel = pm.ls(selection=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = 0
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2}_{3}'.format(prefix, name, number, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

def local_hier_waste(*args):
	sel = pm.ls(selection=True, dag=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = 0
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2:02d}_{3}'.format(prefix, name, count, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

	new_name = '{0}_{1}_{2:02d}_{3}'.format(prefix, name, count, 'waste')
	each.rename(new_name)

def local_sel_waste(*args):
	sel = pm.ls(selection=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = 0
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2}_{3}'.format(prefix, name, number, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

	new_name = '{0}_{1}_{2:02d}_{3}'.format(prefix, name, count, 'waste')
	each.rename(new_name)

def bind_hier(*args):
	sel = pm.ls(selection=True, dag=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = 1
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2:02d}_{3}'.format(prefix, name, count, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

def bind_sel(*args):
	sel = pm.ls(selection=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = 1
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2}_{3}'.format(prefix, name, number, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

def bind_hier_waste(*args):
	sel = pm.ls(selection=True, dag=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = 1
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2:02d}_{3}'.format(prefix, name, count, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

	new_name = '{0}_{1}_{2:02d}_{3}'.format(prefix, name, count, 'waste')
	each.rename(new_name)

def bind_sel_waste(*args):
	sel = pm.ls(selection=True)

	prefix = prefix_input.getText()
	name = name_input.getText()
	number = number_input.getText()
	count = 1
	suffix = suffix_input.getText()

	for each in sel:
		count = count + 1
		new_name = '{0}_{1}_{2}_{3}'.format(prefix, name, number, suffix)
		print 'New Name:', new_name

		each.rename(new_name)

	new_name = '{0}_{1}_{2:02d}_{3}'.format(prefix, name, count, 'waste')
	each.rename(new_name)

def replace(*args):

	if sel_box_2.getValue() == True:
		# Hierarchy
		# sel = pm.ls(selection=True, dag=True)
		# Selected
		sel = pm.ls(selection=True)

		search = search_input.getText()
		replace = replace_input.getText()


		for each in sel:
			new_name = each.replace(search, replace)
			pm.rename(each, new_name)

	elif sel_box_2.getValue() == False:
		# Hierarchy
		sel = pm.ls(selection=True, dag=True)
		# Selected
		# sel = pm.ls(selection=True)

		search = search_input.getText()
		replace = replace_input.getText()


		for each in sel:
			new_name = each.replace(search, replace)
			pm.rename(each, new_name)







