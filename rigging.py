'''
Dean Slocum
rigging.py

Description:

	A tool kit window with all my rigging tools.

How to Run:

import rigging
reload(rigging)
rigging.gui()

'''

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
from functools import partial

win = 'Rigging Kit'
print 'Rigging Kit Activated'

w = 90
h = 180
w2 = 39
w3 = 45
h2 = 5
h3 = 6
b1 = [0,.5,0]
b2 = [0,.5,.5]
o1 = [0,0,0,.75]

def gui():

	global par_mo_box, pnt_mo_box, ori_mo_box, scl_mo_box, aim_mo_box, snap_box, sticky_box
	global grp_radio, flexi_radio, flexi_radio2, anim_radio, anim_field

	if(cmds.window(win , ex=1)):
		cmds.deleteUI(win)
	if (cmds.windowPref(win , ex=1)):
		cmds.windowPref(win , r=1)

	cmds.window(win , s=1, vis=1, w=w , h=h)
	
	cmds.rowColumnLayout()

	cmds.frameLayout(l='WINDOWS', bgc=[0,.5,0])
	cmds.rowColumnLayout(nc=7)

	cmds.iconTextButton(style='iconOnly',
	image='menuIconWindow', c=out, w=w2, iol='Outl', olb=o1)
	cmds.iconTextButton(style='iconOnly',
	image='menuIconWindow', c=att_win, w=w2, iol='ATTR', olb=o1)
	cmds.iconTextButton(style='iconOnly',
	image='menuIconWindow', c=script, w=w2, iol='Script', olb=o1)
	cmds.iconTextButton(style='iconOnly',
	image='menuIconWindow', c=con_edit, w=w2, iol='CE', olb=o1)
	cmds.iconTextButton(style='iconOnly',
	image='menuIconWindow', c=exp, w=w2, iol='EE', olb=o1)
	cmds.iconTextButton(style='iconOnly',
	image='menuIconWindow', c=node_edit, w=w2, iol='NE', olb=o1)
	cmds.iconTextButton(style='iconOnly',
	image='menuIconWindow', c=hyper_edit, w=w2, iol='Hyper', olb=o1)

	cmds.setParent('..')

	cmds.rowColumnLayout(nc=7)

	cmds.iconTextButton(style='iconOnly',
	image='menuIconWindow', c=comp_edit, w=w2, iol='CpEd', olb=o1)
	cmds.iconTextButton(style='iconOnly',
	image='menuIconWindow', c=chnl_ctrl, w=w2, iol='CC', olb=o1)
	cmds.iconTextButton(style='iconOnly',
	image='menuIconKeys', c=sdk, w=w2, iol='Set.', olb=o1)
	cmds.iconTextButton(style='iconOnly',
	image='menuIconDisplay', c=jnt_scale, w=w2, iol='JS', olb=o1)
	cmds.iconTextButton(style='iconOnly',
	image='menuIconModify', c=add_att, w=w2, iol='AA', olb=o1)
	cmds.iconTextButton(style='iconOnly',
	image='menuIconModify', c=edit_att, w=w2, iol='EA', olb=o1)
	cmds.iconTextButton(style='iconOnly',
	image='menuIconModify', c=del_att, w=w2, iol='DA', olb=o1)

	cmds.setParent('..')

	cmds.frameLayout(l='CONSTRAINTS', bgc=b1)
	cmds.rowColumnLayout(nc=7)

	cmds.text(' ', w=6)
	cmds.iconTextButton(style='iconOnly',
	image='parentConstraint.png', c=par_con, w=w3)
	par_mo_box = pm.checkBox(l='MO', v=1)
	cmds.iconTextButton(style='iconOnly',
	image='posConstraint.png', c=pnt_con, w=w3)
	pnt_mo_box = pm.checkBox(l='MO', v=1)
	cmds.iconTextButton(style='iconOnly',
	image='orientConstraint.png', c=ori_con, w=w3)
	ori_mo_box = pm.checkBox(l='MO', v=1)

	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	
	cmds.text(' ', w=6)
	cmds.iconTextButton(style='iconOnly',
	image='scaleConstraint.png', c=scl_con, w=w3)
	scl_mo_box = pm.checkBox(l='MO', v=1)
	cmds.iconTextButton(style='iconOnly',
	image='aimConstraint.png', c=aim_con, w=w3)
	aim_mo_box = pm.checkBox(l='MO', v=1)
	cmds.iconTextButton(style='iconOnly',
	image='poleVectorConstraint.png', c=pol_con, w=w3)

	cmds.setParent('..')

	cmds.separator(bgc=b1, st='in')

	form = cmds.formLayout()
	tabs = cmds.tabLayout(imw=5, imh=5, bs='none')
	cmds.formLayout(form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))

	# dropdown tabs
	child1 = cmds.rowColumnLayout(nc=1)

	cmds.columnLayout(adj=True)

	cmds.frameLayout(l='JOINT TOOLS', bgc=b1, w=265)
	cmds.rowColumnLayout(nc=5, co=([2,'both',20],[4,'both',20]))

	cmds.text(' ', w=4)
	cmds.iconTextButton(style='iconOnly',
	image='kinJoint', c=jnt_tool, w=w2)
	cmds.iconTextButton(style='iconOnly',
	image='kinMirrorJoint_S', c=mir_jnt_tool, w=w2)
	cmds.iconTextButton(style='iconOnly',
	image='kinInsert', c=insert_jnt_tool, w=w2)
	cmds.iconTextButton(style='iconOnly',
	image='kinRemove', c=remove_jnt_tool, w=w2)
	
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.setParent('..')

	cmds.frameLayout(l='IK HANDLE TOOLS', bgc=b1)
	cmds.rowColumnLayout(nc=5, co=([2,'both',15],[4,'both',15]))

	cmds.text(' ', w=4)
	cmds.iconTextButton(style='iconOnly', iol='RP', olb=o1,
	image='kinHandle', c=RP_IK_tool, w=w2)
	cmds.iconTextButton(style='iconOnly', iol='SC', olb=o1,
	image='kinHandle', c=SC_IK_tool, w=w2)
	snap_box = pm.checkBox(l='Snap', v=1)
	sticky_box = pm.checkBox(l='Sticky')

	cmds.setParent('..')
	cmds.setParent('..')

	cmds.frameLayout(l='IK SPLINE HANDLE TOOLS', bgc=b1)
	cmds.rowColumnLayout(nc=3, co=[2,'both',40])

	cmds.text(' ', w=35)
	cmds.iconTextButton(style='iconOnly',
	image='curveCV', c=cv_tool, w=w2)
	cmds.iconTextButton(style='iconOnly',
	image='kinSplineHandle', c=ik_spline_tool, w=w2)
	
	cmds.setParent('..')
	cmds.setParent('..')

	cmds.frameLayout(l='JOINT CHAIN GENERATORS', bgc=b1)
	cmds.rowColumnLayout(nc=5, co=([2,'both',20],[4,'both',20]))

	cmds.text(' ', w=4)
	cmds.iconTextButton(style='iconOnly', iol='5', olb=o1,
	image='kinJoint', c=five, w=w2)
	cmds.iconTextButton(style='iconOnly', iol='10', olb=o1,
	image='kinJoint', c=ten, w=w2)
	cmds.iconTextButton(style='iconOnly', iol='20', olb=o1,
	image='kinJoint', c=twenty, w=w2)
	cmds.iconTextButton(style='iconOnly', iol='50', olb=o1,
	image='kinJoint', c=fifty, w=w2)
	
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.setParent('..')

	# dropdown tabs
	child2 = cmds.rowColumnLayout(nc=1)

	cmds.frameLayout(l='ALIGNMENTS', bgc=b1)
	cmds.rowColumnLayout(nc=4, co=([1,'right',17],[3,'both',17]))

	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)
	cmds.button(l='MirrorCVs', c=mirCV, bgc=b2)
	cmds.button(l='PivFix', c=pivFix, bgc=b2)	
	cmds.button(l='ParSnap', c=parSnap, bgc=b2)
	cmds.button(l='PntSnap', c=pntSnap, bgc=b2)
	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)

	cmds.setParent('..')
	cmds.setParent('..')

	cmds.frameLayout(l='PADDING', bgc=b1)
	cmds.rowColumnLayout(nc=2, co=[1,'right',7])

	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)
	cmds.button(l='2x grp', bgc=b2, c=grouping)
	grp_radio = pm.radioButtonGrp(la3=['None', 'ParSnap', 'PntSnap'], nrb=3, cw3=[60,75,70], sl=2)
	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)

	cmds.setParent('..')
	cmds.setParent('..')

	cmds.frameLayout(l='ATTRIBUTES -- LOCK & HIDE', bgc=b1)
	cmds.rowColumnLayout(nc=4, co=([2,'both',16],[4,'left',16]))

	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)

	cmds.iconTextButton(st='textOnly', l=' Translates ', c=hide_trans, dcc=show_trans, bgc=b2)
	cmds.iconTextButton(st='textOnly', l=' Rotates ', c=hide_rots, dcc=show_rots, bgc=b2)
	cmds.iconTextButton(st='textOnly', l=' Scales ', c=hide_scales, dcc=show_scales, bgc=b2)
	cmds.iconTextButton(st='textOnly', l=' Visibility ', c=hide_vis, dcc=show_vis, bgc=b2)

	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)
	
	cmds.setParent('..')
	cmds.setParent('..')

	cmds.frameLayout(l='MISC', bgc=b1)
	cmds.rowColumnLayout(nc=2, co=[2,'left',10])

	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)

	cmds.button(l='Credits Icon', bgc=b2, c=credits)

	cmds.button(l='Master Icon with Credits', bgc=b2, c=master_icons)

	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)

	cmds.button(l='Annotation', bgc=b2, c=annotation)

	cmds.text('Select the joint, then icon.')

	cmds.setParent('..')
	cmds.setParent('..')
	cmds.setParent('..')

	# dropdown tabs
	child3 = cmds.rowColumnLayout(nc=1)

	cmds.frameLayout(l='ATTRIBUTE SETS', bgc=b1)
	cmds.rowColumnLayout(nc=3, co=([2,'both',16],[3,'right',28]))

	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)

	cmds.button(l='Biped Hand', c=b_hand_attrs, bgc=b2)
	cmds.button(l='Biped Foot', c=b_foot_attrs, bgc=b2)
	cmds.button(l='Quad Foot', c=q_foot_attrs, bgc=b2)
	
	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)

	cmds.setParent('..')
	cmds.setParent('..')

	cmds.frameLayout(l='SYSTEM TOOLS', bgc=b1)
	cmds.rowColumnLayout(nc=2, co=[2,'left',10])

	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)

	cmds.button(l='IK/FK Setup', c=ikfk_switch, bgc=b2)
	cmds.button(l='Pole Vector Locator', c=polVec, bgc=b2)

	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)

	cmds.button(l='IK/FK No Flip Leg Setup', c=b_foot_attrs, bgc=b2)
	cmds.button(l='RFL Foot Setup', c=q_foot_attrs, bgc=b2)

	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)

	# cmds.text('IK/FK LEG W/ NO FLIP')
	# cmds.text('RFL FEET')
	
	cmds.setParent('..')
	cmds.setParent('..')

	cmds.frameLayout(l='PREBUILT SYSTEMS', bgc=b1)
	cmds.rowColumnLayout(nc=2, co=[2,'left',10])

	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)

	cmds.button(l='Flexi Back', c=flexi_back, bgc=b2)
	flexi_radio = pm.radioButtonGrp(la2=['5 jnts', '9 jnts'], nrb=2, cw2=[60,75], sl=1)

	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)

	cmds.button(l='Flexi Arm', c=flexi_arm, bgc=b2)
	flexi_radio2 = pm.radioButtonGrp(la2=['5 jnts', '9 jnts'], nrb=2, cw2=[60,75], sl=1)
	
	cmds.text(' ', h=h3)
	cmds.text(' ', h=h3)

	cmds.button(l='IK Spline Tail/Neck', c=tail_spline, bgc=b2)

	# cmds.text('FLEXI ARM')
	
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.setParent('..')

	# # dropdown tabs
	# child4 = cmds.rowColumnLayout(nc=1)

	# cmds.frameLayout(l='ANIMATION TOOLS', bgc=b1)
	# cmds.rowColumnLayout(nc=2)

	# cmds.text(' ', h=h3)
	# cmds.text(' ', h=h3)

	# cmds.button(l='Create Shelf Button', c=anim_icon_gen, bgc=b2)
	# anim_radio = pm.radioButtonGrp(la2=['SEL', 'KEY'], nrb=2, cw2=[60,75], sl=1, cat=[1,'left',10], co2=[1,10])

	# cmds.text(' ', h=h3)
	# cmds.text(' ', h=h3)

	# cmds.text(l='Shelf Button Name:')
	# anim_field = pm.textField('anim_field', pht='Neck, Rleg, ALL')

	# cmds.text(' ', h=30)
	# cmds.text(' ', h=30)


	# cmds.button(l='Reset Icons', c=reset, bgc=b2)

	# # cmds.text('MEL shelf button generator')
	# # cmds.text('reset icon positions')
	
	# cmds.setParent('..')
	# cmds.setParent('..')
	# cmds.setParent('..')

	cmds.tabLayout(tabs, edit=True, tl=((child1, 'Joints'), (child2, 'Controls'), (child3, 'Building')))

	cmds.showWindow()

def out(*args):
	cmds.OutlinerWindow()

def con_edit(*args):
	cmds.ConnectionEditor()

def exp(*args):
	cmds.ExpressionEditor()

def script(*args):
	cmds.ScriptEditor()

def sdk(*args):
	cmds.SetDrivenKeyOptions()

def add_att(*args):
	cmds.AddAttribute()

def edit_att(*args):
	cmds.RenameAttribute()

def del_att(*args):
	cmds.DeleteAttribute()

def att_win(*args):
	cmds.AttributeEditor()

def node_edit(*args):
	cmds.NodeEditorWindow()

def hyper_edit(*args):
	cmds.HypergraphHierarchyWindow()

def comp_edit(*args):
	cmds.ComponentEditor()

def chnl_ctrl(*args):
	cmds.ChannelControlEditor()

def jnt_scale(*args):
	mel.eval("jdsWin;")

def par_con(*args):
	sel = cmds.ls(sl=1)

	if par_mo_box.getValue() == True:
		cmds.parentConstraint(sel[0], sel[1], mo=1)
	elif par_mo_box.getValue() == False:
		cmds.parentConstraint(sel[0], sel[1], mo=0)

def pnt_con(*args):
	sel = cmds.ls(sl=1)

	if pnt_mo_box.getValue() == True:
		cmds.pointConstraint(sel[0], sel[1], mo=1)
	elif pnt_mo_box.getValue() == False:
		cmds.pointConstraint(sel[0], sel[1], mo=0)

def ori_con(*args):
	sel = cmds.ls(sl=1)

	if ori_mo_box.getValue() == True:
		cmds.orientConstraint(sel[0], sel[1], mo=1)
	elif ori_mo_box.getValue() == False:
		cmds.orientConstraint(sel[0], sel[1], mo=0)

def scl_con(*args):
	sel = cmds.ls(sl=1)

	if scl_mo_box.getValue() == True:
		cmds.scaleConstraint(sel[0], sel[1], mo=1)
	elif scl_mo_box.getValue() == False:
		cmds.scaleConstraint(sel[0], sel[1], mo=0)

def aim_con(*args):
	sel = cmds.ls(sl=1)

	if aim_mo_box.getValue() == True:
		cmds.aimConstraint(sel[0], sel[1], mo=1)
	elif aim_mo_box.getValue() == False:
		cmds.aimConstraint(sel[0], sel[1], mo=0)

def pol_con(*args):
	sel = cmds.ls(sl=1)

	cmds.poleVectorConstraint(sel[0], sel[1])

def jnt_tool(*args):
	cmds.JointTool()

def mir_jnt_tool(*args):
	cmds.mirrorJoint(myz=1, mb=1, sr=['lt','rt'])

def insert_jnt_tool(*args):
	cmds.InsertJointTool()

def remove_jnt_tool(*args):
	cmds.RemoveJoint()

def cv_tool(*args):
	cmds.CVCurveTool()

def ik_spline_tool(*args):
	cmds.IKSplineHandleTool()

def RP_IK_tool(*args):
	sel = cmds.ls(sl=1)

	if snap_box.getValue() == True and sticky_box.getValue() == False:
		cmds.ikHandle(sol='ikRPsolver', s=0, shf=1, sj=sel[0], ee=sel[1])
	elif snap_box.getValue() == True and sticky_box.getValue() == True:
		cmds.ikHandle(sol='ikRPsolver', s='sticky', shf=1, sj=sel[0], ee=sel[1])
	elif snap_box.getValue() == False and sticky_box.getValue() == False:
		cmds.ikHandle(sol='ikRPsolver', s=0, shf=0, sj=sel[0], ee=sel[1])
	elif snap_box.getValue() == False and sticky_box.getValue() == True:
		cmds.ikHandle(sol='ikRPsolver', s='sticky', shf=0, sj=sel[0], ee=sel[1])

def SC_IK_tool(*args):
	sel = cmds.ls(sl=1)

	if snap_box.getValue() == True and sticky_box.getValue() == False:
		cmds.ikHandle(sol='ikSCsolver', s=0, shf=1, sj=sel[0], ee=sel[1])
	elif snap_box.getValue() == True and sticky_box.getValue() == True:
		cmds.ikHandle(sol='ikSCsolver', s='sticky', shf=1, sj=sel[0], ee=sel[1])
	elif snap_box.getValue() == False and sticky_box.getValue() == False:
		cmds.ikHandle(sol='ikSCsolver', s=0, shf=0, sj=sel[0], ee=sel[1])
	elif snap_box.getValue() == False and sticky_box.getValue() == True:
		cmds.ikHandle(sol='ikSCsolver', s='sticky', shf=0, sj=sel[0], ee=sel[1])

def five(*args):
	sel = cmds.ls(sl=True)

	cmds.select(d=True)
	jnt1 = cmds.joint(p=(0, 0, 0))
	jnt2 = cmds.joint(p=(2, 0, 0))
	cmds.joint(jnt1, e=True, zso=True, oj='xyz')
	jnt3 = cmds.joint(p=(4, 0, 0))
	cmds.joint(jnt2, e=True, zso=True, oj='xyz')
	jnt4 = cmds.joint(p=(6, 0, 0))
	cmds.joint(jnt3, e=True, zso=True, oj='xyz')
	jnt5 = cmds.joint(p=(8, 0, 0))
	cmds.joint(jnt4, e=True, zso=True, oj='xyz')
	jnt6 = cmds.joint(p=(10, 0, 0))
	cmds.joint(jnt5, e=True, zso=True, oj='xyz')

	cmds.delete(jnt6)

def ten(*args):
	sel = cmds.ls(sl=True)

	cmds.select(d=True)
	jnt1 = cmds.joint(p=(0, 0, 0))
	jnt2 = cmds.joint(p=(2, 0, 0))
	cmds.joint(jnt1, e=True, zso=True, oj='xyz')
	jnt3 = cmds.joint(p=(4, 0, 0))
	cmds.joint(jnt2, e=True, zso=True, oj='xyz')
	jnt4 = cmds.joint(p=(6, 0, 0))
	cmds.joint(jnt3, e=True, zso=True, oj='xyz')
	jnt5 = cmds.joint(p=(8, 0, 0))
	cmds.joint(jnt4, e=True, zso=True, oj='xyz')
	jnt6 = cmds.joint(p=(10, 0, 0))
	cmds.joint(jnt5, e=True, zso=True, oj='xyz')
	jnt7 = cmds.joint(p=(12, 0, 0))
	cmds.joint(jnt6, e=True, zso=True, oj='xyz')
	jnt8 = cmds.joint(p=(14, 0, 0))
	cmds.joint(jnt7, e=True, zso=True, oj='xyz')
	jnt9 = cmds.joint(p=(16, 0, 0))
	cmds.joint(jnt8, e=True, zso=True, oj='xyz')
	jnt10 = cmds.joint(p=(18, 0, 0))
	cmds.joint(jnt9, e=True, zso=True, oj='xyz')
	jnt11 = cmds.joint(p=(20, 0, 0))
	cmds.joint(jnt10, e=True, zso=True, oj='xyz')

	cmds.delete(jnt11)

def twenty(*args):
	sel = cmds.ls(sl=True)

	cmds.select(d=True)
	jnt1 = cmds.joint(p=(0, 0, 0))
	jnt2 = cmds.joint(p=(2, 0, 0))
	cmds.joint(jnt1, e=True, zso=True, oj='xyz')
	jnt3 = cmds.joint(p=(4, 0, 0))
	cmds.joint(jnt2, e=True, zso=True, oj='xyz')
	jnt4 = cmds.joint(p=(6, 0, 0))
	cmds.joint(jnt3, e=True, zso=True, oj='xyz')
	jnt5 = cmds.joint(p=(8, 0, 0))
	cmds.joint(jnt4, e=True, zso=True, oj='xyz')
	jnt6 = cmds.joint(p=(10, 0, 0))
	cmds.joint(jnt5, e=True, zso=True, oj='xyz')
	jnt7 = cmds.joint(p=(12, 0, 0))
	cmds.joint(jnt6, e=True, zso=True, oj='xyz')
	jnt8 = cmds.joint(p=(14, 0, 0))
	cmds.joint(jnt7, e=True, zso=True, oj='xyz')
	jnt9 = cmds.joint(p=(16, 0, 0))
	cmds.joint(jnt8, e=True, zso=True, oj='xyz')
	jnt10 = cmds.joint(p=(18, 0, 0))
	cmds.joint(jnt9, e=True, zso=True, oj='xyz')
	jnt11 = cmds.joint(p=(20, 0, 0))
	cmds.joint(jnt10, e=True, zso=True, oj='xyz')
	jnt12 = cmds.joint(p=(22, 0, 0))
	cmds.joint(jnt11, e=True, zso=True, oj='xyz')
	jnt13 = cmds.joint(p=(24, 0, 0))
	cmds.joint(jnt12, e=True, zso=True, oj='xyz')
	jnt14 = cmds.joint(p=(26, 0, 0))
	cmds.joint(jnt13, e=True, zso=True, oj='xyz')
	jnt15 = cmds.joint(p=(28, 0, 0))
	cmds.joint(jnt14, e=True, zso=True, oj='xyz')
	jnt16 = cmds.joint(p=(30, 0, 0))
	cmds.joint(jnt15, e=True, zso=True, oj='xyz')
	jnt17 = cmds.joint(p=(32, 0, 0))
	cmds.joint(jnt16, e=True, zso=True, oj='xyz')
	jnt18 = cmds.joint(p=(34, 0, 0))
	cmds.joint(jnt17, e=True, zso=True, oj='xyz')
	jnt19 = cmds.joint(p=(36, 0, 0))
	cmds.joint(jnt18, e=True, zso=True, oj='xyz')
	jnt20 = cmds.joint(p=(38, 0, 0))
	cmds.joint(jnt19, e=True, zso=True, oj='xyz')
	jnt21 = cmds.joint(p=(40, 0, 0))
	cmds.joint(jnt20, e=True, zso=True, oj='xyz')

	cmds.delete(jnt21)

def fifty(*args):
	sel = cmds.ls(sl=True)

	cmds.select(d=True)
	jnt1 = cmds.joint(p=(0, 0, 0))
	jnt2 = cmds.joint(p=(2, 0, 0))
	cmds.joint(jnt1, e=True, zso=True, oj='xyz')
	jnt3 = cmds.joint(p=(4, 0, 0))
	cmds.joint(jnt2, e=True, zso=True, oj='xyz')
	jnt4 = cmds.joint(p=(6, 0, 0))
	cmds.joint(jnt3, e=True, zso=True, oj='xyz')
	jnt5 = cmds.joint(p=(8, 0, 0))
	cmds.joint(jnt4, e=True, zso=True, oj='xyz')
	jnt6 = cmds.joint(p=(10, 0, 0))
	cmds.joint(jnt5, e=True, zso=True, oj='xyz')
	jnt7 = cmds.joint(p=(12, 0, 0))
	cmds.joint(jnt6, e=True, zso=True, oj='xyz')
	jnt8 = cmds.joint(p=(14, 0, 0))
	cmds.joint(jnt7, e=True, zso=True, oj='xyz')
	jnt9 = cmds.joint(p=(16, 0, 0))
	cmds.joint(jnt8, e=True, zso=True, oj='xyz')
	jnt10 = cmds.joint(p=(18, 0, 0))
	cmds.joint(jnt9, e=True, zso=True, oj='xyz')
	jnt11 = cmds.joint(p=(20, 0, 0))
	cmds.joint(jnt10, e=True, zso=True, oj='xyz')
	jnt12 = cmds.joint(p=(22, 0, 0))
	cmds.joint(jnt11, e=True, zso=True, oj='xyz')
	jnt13 = cmds.joint(p=(24, 0, 0))
	cmds.joint(jnt12, e=True, zso=True, oj='xyz')
	jnt14 = cmds.joint(p=(26, 0, 0))
	cmds.joint(jnt13, e=True, zso=True, oj='xyz')
	jnt15 = cmds.joint(p=(28, 0, 0))
	cmds.joint(jnt14, e=True, zso=True, oj='xyz')
	jnt16 = cmds.joint(p=(30, 0, 0))
	cmds.joint(jnt15, e=True, zso=True, oj='xyz')
	jnt17 = cmds.joint(p=(32, 0, 0))
	cmds.joint(jnt16, e=True, zso=True, oj='xyz')
	jnt18 = cmds.joint(p=(34, 0, 0))
	cmds.joint(jnt17, e=True, zso=True, oj='xyz')
	jnt19 = cmds.joint(p=(36, 0, 0))
	cmds.joint(jnt18, e=True, zso=True, oj='xyz')
	jnt20 = cmds.joint(p=(38, 0, 0))
	cmds.joint(jnt19, e=True, zso=True, oj='xyz')
	jnt21 = cmds.joint(p=(40, 0, 0))
	cmds.joint(jnt20, e=True, zso=True, oj='xyz')
	jnt22 = cmds.joint(p=(42, 0, 0))
	cmds.joint(jnt21, e=True, zso=True, oj='xyz')
	jnt23 = cmds.joint(p=(44, 0, 0))
	cmds.joint(jnt22, e=True, zso=True, oj='xyz')
	jnt24 = cmds.joint(p=(46, 0, 0))
	cmds.joint(jnt23, e=True, zso=True, oj='xyz')
	jnt25 = cmds.joint(p=(48, 0, 0))
	cmds.joint(jnt24, e=True, zso=True, oj='xyz')
	jnt26 = cmds.joint(p=(50, 0, 0))
	cmds.joint(jnt25, e=True, zso=True, oj='xyz')
	jnt27 = cmds.joint(p=(52, 0, 0))
	cmds.joint(jnt26, e=True, zso=True, oj='xyz')
	jnt28 = cmds.joint(p=(54, 0, 0))
	cmds.joint(jnt27, e=True, zso=True, oj='xyz')
	jnt29 = cmds.joint(p=(56, 0, 0))
	cmds.joint(jnt28, e=True, zso=True, oj='xyz')
	jnt30 = cmds.joint(p=(58, 0, 0))
	cmds.joint(jnt29, e=True, zso=True, oj='xyz')
	jnt31 = cmds.joint(p=(60, 0, 0))
	cmds.joint(jnt30, e=True, zso=True, oj='xyz')
	jnt32 = cmds.joint(p=(62, 0, 0))
	cmds.joint(jnt31, e=True, zso=True, oj='xyz')
	jnt33 = cmds.joint(p=(64, 0, 0))
	cmds.joint(jnt32, e=True, zso=True, oj='xyz')
	jnt34 = cmds.joint(p=(66, 0, 0))
	cmds.joint(jnt33, e=True, zso=True, oj='xyz')
	jnt35 = cmds.joint(p=(68, 0, 0))
	cmds.joint(jnt34, e=True, zso=True, oj='xyz')
	jnt36 = cmds.joint(p=(70, 0, 0))
	cmds.joint(jnt35, e=True, zso=True, oj='xyz')
	jnt37 = cmds.joint(p=(72, 0, 0))
	cmds.joint(jnt36, e=True, zso=True, oj='xyz')
	jnt38 = cmds.joint(p=(74, 0, 0))
	cmds.joint(jnt37, e=True, zso=True, oj='xyz')
	jnt39 = cmds.joint(p=(76, 0, 0))
	cmds.joint(jnt38, e=True, zso=True, oj='xyz')
	jnt40 = cmds.joint(p=(78, 0, 0))
	cmds.joint(jnt39, e=True, zso=True, oj='xyz')
	jnt41 = cmds.joint(p=(80, 0, 0))
	cmds.joint(jnt40, e=True, zso=True, oj='xyz')
	jnt42 = cmds.joint(p=(82, 0, 0))
	cmds.joint(jnt41, e=True, zso=True, oj='xyz')
	jnt43 = cmds.joint(p=(84, 0, 0))
	cmds.joint(jnt42, e=True, zso=True, oj='xyz')
	jnt44 = cmds.joint(p=(86, 0, 0))
	cmds.joint(jnt43, e=True, zso=True, oj='xyz')
	jnt45 = cmds.joint(p=(88, 0, 0))
	cmds.joint(jnt44, e=True, zso=True, oj='xyz')
	jnt46 = cmds.joint(p=(90, 0, 0))
	cmds.joint(jnt45, e=True, zso=True, oj='xyz')
	jnt47 = cmds.joint(p=(92, 0, 0))
	cmds.joint(jnt46, e=True, zso=True, oj='xyz')
	jnt48 = cmds.joint(p=(94, 0, 0))
	cmds.joint(jnt47, e=True, zso=True, oj='xyz')
	jnt49 = cmds.joint(p=(96, 0, 0))
	cmds.joint(jnt48, e=True, zso=True, oj='xyz')
	jnt50 = cmds.joint(p=(98, 0, 0))
	cmds.joint(jnt49, e=True, zso=True, oj='xyz')
	jnt51 = cmds.joint(p=(100, 0, 0))
	cmds.joint(jnt50, e=True, zso=True, oj='xyz')

	cmds.delete(jnt51)

def grouping(*args):
	sel = cmds.ls(sl=1)

	for each in sel:

		if grp_radio.getSelect() == 1:
			grp1 = cmds.group(each, name='local#')
			grp2 = cmds.group(grp1, name='pad#')
			cmds.select(cl=1)
		elif grp_radio.getSelect() == 2:
			grp1 = cmds.group(em=1, name='local#')
			grp2 = cmds.group(grp1, name='pad#')
			cmds.delete(cmds.parentConstraint(each, grp2))
			cmds.parent(each, grp1)
			cmds.select(cl=1)
		elif grp_radio.getSelect() == 3:
			grp1 = cmds.group(em=1, name='local#')
			grp2 = cmds.group(grp1, name='pad#')
			cmds.delete(cmds.pointConstraint(each, grp2))
			cmds.parent(each, grp1)
			cmds.select(cl=1)

def parSnap(*args):
	sel = cmds.ls(sl=True)

	cmds.delete(cmds.parentConstraint(sel[0], sel[1]))

def pntSnap(*args):
	sel = cmds.ls(sl=True)

	cmds.delete(cmds.pointConstraint(sel[0], sel[1]))

def mirCV(*args):
	sel = cmds.ls(sl=1)

	grp1 = cmds.group(em=1)
	cmds.rename(grp1, 'orig')
	dup_sel = cmds.duplicate(sel)
	cmds.parent(dup_sel, 'orig')
	cmds.xform('orig', s=(-1,1,1))
	cmds.parent(dup_sel, w=1)
	cmds.delete('orig')
	cmds.xform(dup_sel, s=(1,1,1))

def hide_trans(*args):
	selected_items = pm.ls(selection=True)
	for obj in selected_items:
		obj.tx.set(lock=True, keyable=False)
		obj.ty.set(lock=True, keyable=False)
		obj.tz.set(lock=True, keyable=False)
	print ('Translations Locked and Hidden on Seleced')

def hide_rots(*args):
	selected_items = pm.ls(selection=True)
	for obj in selected_items:
		obj.rx.set(lock=True, keyable=False)
		obj.ry.set(lock=True, keyable=False)
		obj.rz.set(lock=True, keyable=False)
		print ('Rotates Locked and Hidden on Seleced')

def hide_scales(*args):
	selected_items = pm.ls(selection=True)
	for obj in selected_items:
		obj.sx.set(lock=True, keyable=False)
		obj.sy.set(lock=True, keyable=False)
		obj.sz.set(lock=True, keyable=False)
		print ('Scales Locked and Hidden on Seleced')

def hide_vis(*args):
	selected_items = pm.ls(selection=True)
	for obj in selected_items:
		obj.v.set(lock=True, keyable=False)
		print ('Visability Locked and Hidden on Seleced')

def show_trans(*args):
	selected_items = pm.ls(selection=True)
	for obj in selected_items:
		obj.tx.set(lock=False, keyable=True)
		obj.ty.set(lock=False, keyable=True)
		obj.tz.set(lock=False, keyable=True)
		print ('Translates Unlocked and Shown on Seleced')

def show_rots(*args):
	selected_items = pm.ls(selection=True)
	for obj in selected_items:
		obj.rx.set(lock=False, keyable=True)
		obj.ry.set(lock=False, keyable=True)
		obj.rz.set(lock=False, keyable=True)
		print ('Rotates Unlocked and Shown on Seleced')

def show_scales(*args):
	selected_items = pm.ls(selection=True)
	for obj in selected_items:
		obj.sx.set(lock=False, keyable=True)
		obj.sy.set(lock=False, keyable=True)
		obj.sz.set(lock=False, keyable=True)
		print ('Scales Unlocked and Shown on Seleced')

def show_vis(*args):
	selected_items = pm.ls(selection=True)
	for obj in selected_items:
		obj.v.set(lock=False, keyable=True)
		print ('Visability Unlocked and Shown on Seleced')

def credits(*args):
	cmds.file('/Users/dean_13/Library/Preferences/Autodesk/maya/import_rigs/credits.mb', i=1)

def master_icons(*args):
	cmds.file('/Users/dean_13/Library/Preferences/Autodesk/maya/import_rigs/master_icons.mb', i=1)

def b_hand_attrs(*args):
	sel = pm.ls(sl=1)

	for obj in sel:

		obj.addAttr('CURLS', at='enum', en='--------:', k=1)
		obj.CURLS.set(cb=1)

		obj.addAttr('index_curl', k=1)
		obj.addAttr('middle_curl', k=1)
		obj.addAttr('ring_curl', k=1)
		obj.addAttr('pinky_curl', k=1)
		obj.addAttr('thumb_curl', k=1)

		obj.addAttr('SPREADS', at='enum', en='--------:', k=1)
		obj.SPREADS.set(cb=1)

		obj.addAttr('index_spread', k=1)
		obj.addAttr('middle_spread', k=1)
		obj.addAttr('ring_spread', k=1)
		obj.addAttr('pinky_spread', k=1)
		obj.addAttr('thumb_spread', k=1)

		obj.addAttr('TWISTS', at='enum', en='--------:', k=1)
		obj.TWISTS.set(cb=1)

		obj.addAttr('index_twist', k=1)
		obj.addAttr('middle_twist', k=1)
		obj.addAttr('ring_twist', k=1)
		obj.addAttr('pinky_twist', k=1)
		obj.addAttr('thumb_twist', k=1)

		obj.addAttr('MISC', at='enum', en='--------:', k=1)
		obj.MISC.set(cb=1)

		obj.addAttr('thumb_drop', k=1)
		obj.addAttr('fist', k=1, min=-10, max=10)
		obj.addAttr('spread', k=1, min=-10, max=10)
		obj.addAttr('Finger_icon_vis', k=1, at='enum', en='OFF:ON:')

def b_foot_attrs(*args):
	sel = pm.ls(sl=1)

	for obj in sel:

		obj.addAttr('FOOT', at='enum', en='--------:', k=1)
		obj.FOOT.set(cb=1)

		obj.addAttr('Heel', k=1)
		obj.addAttr('InnerBank', k=1)
		obj.addAttr('OuterBank', k=1)
		obj.addAttr('Toe', k=1)
		obj.addAttr('Ball', k=1)

		obj.addAttr('AUTO', at='enum', en='--------:', k=1)
		obj.AUTO.set(cb=1)

		obj.addAttr('Foot_bank', k=1, min=-10, max=10)
		obj.addAttr('Foot_roll', k=1, min=-10, max=10)

		obj.addAttr('MISC', at='enum', en='--------:', k=1)
		obj.MISC.set(cb=1)

		obj.addAttr('Foot_icon_vis', k=1, at='enum', en='OFF:ON:')
		obj.addAttr('Follow', k=1, at='enum', en='MASTER:WORLD:COG:ICON:')

def pivFix(*args):
	#reset icon orientaion with 2 groups for when mirroring doesn't always work correctly

	sel=cmds.ls(sl=1)

	loc = cmds.spaceLocator()

	cmds.delete(cmds.parentConstraint(sel[0], loc))

	grp1 = cmds.group(em=1, name='local#')
	grp2 = cmds.group(grp1, name='pad#')
	cmds.delete(cmds.parentConstraint(loc, grp2))
	cmds.parent(loc, grp1)
	cmds.select(cl=1)

	cmds.parent(sel[1], grp1)

	cmds.makeIdentity(sel[1], apply=True, t=1, r=1, s=1, n=0)

	cmds.delete(loc)

def q_foot_attrs(*args):
	sel = pm.ls(sl=1)

	for obj in sel:

		obj.addAttr('INDEX', at='enum', en='--------:', k=1)
		obj.INDEX.set(cb=1)

		obj.addAttr('index_root', k=1, min=-10, max=10)
		obj.addAttr('index_2', k=1, min=-10, max=10)
		obj.addAttr('index_3', k=1, min=-10, max=10)
		obj.addAttr('index_twist', k=1, min=-10, max=10)

		obj.addAttr('MIDDLE', at='enum', en='--------:', k=1)
		obj.MIDDLE.set(cb=1)

		obj.addAttr('middle_root', k=1, min=-10, max=10)
		obj.addAttr('middle_2', k=1, min=-10, max=10)
		obj.addAttr('middle_3', k=1, min=-10, max=10)
		obj.addAttr('middle_twist', k=1, min=-10, max=10)

		obj.addAttr('RING', at='enum', en='--------:', k=1)
		obj.RING.set(cb=1)

		obj.addAttr('ring_root', k=1, min=-10, max=10)
		obj.addAttr('ring_2', k=1, min=-10, max=10)
		obj.addAttr('ring_3', k=1, min=-10, max=10)
		obj.addAttr('ring_twist', k=1, min=-10, max=10)

		obj.addAttr('PINKY', at='enum', en='--------:', k=1)
		obj.PINKY.set(cb=1)

		obj.addAttr('pinky_root', k=1, min=-10, max=10)
		obj.addAttr('pinky_2', k=1, min=-10, max=10)
		obj.addAttr('pinky_3', k=1, min=-10, max=10)
		obj.addAttr('pinky_twist', k=1, min=-10, max=10)

		obj.addAttr('THUMB', at='enum', en='--------:', k=1)
		obj.THUMB.set(cb=1)

		obj.addAttr('thumb_root', k=1, min=-10, max=10)
		obj.addAttr('thumb_2', k=1, min=-10, max=10)
		obj.addAttr('thumb_3', k=1, min=-10, max=10)
		obj.addAttr('thumb_twist', k=1, min=-10, max=10)
		obj.addAttr('thumb_drop', k=1, min=-10, max=10)

		obj.addAttr('DEWCLAW', at='enum', en='--------:', k=1)
		obj.DEWCLAW.set(cb=1)

		obj.addAttr('dewclaw_root', k=1, min=-10, max=10)
		obj.addAttr('dewclaw_2', k=1, min=-10, max=10)
		obj.addAttr('dewclaw_3', k=1, min=-10, max=10)
		obj.addAttr('dewclaw_twist', k=1, min=-10, max=10)
		obj.addAttr('dewclaw_drop', k=1, min=-10, max=10)

		obj.addAttr('CURLS', at='enum', en='--------:', k=1)
		obj.CURLS.set(cb=1)

		obj.addAttr('index_curl', k=1, min=-10, max=10)
		obj.addAttr('middle_curl', k=1, min=-10, max=10)
		obj.addAttr('ring_curl', k=1, min=-10, max=10)
		obj.addAttr('pinky_curl', k=1, min=-10, max=10)
		obj.addAttr('thumb_curl', k=1, min=-10, max=10)
		obj.addAttr('dewclaw_curl', k=1, min=-10, max=10)

		obj.addAttr('SPREADS', at='enum', en='--------:', k=1)
		obj.SPREADS.set(cb=1)

		obj.addAttr('index_spread', k=1, min=-10, max=10)
		obj.addAttr('middle_spread', k=1, min=-10, max=10)
		obj.addAttr('ring_spread', k=1, min=-10, max=10)
		obj.addAttr('pinky_spread', k=1, min=-10, max=10)
		obj.addAttr('thumb_spread', k=1, min=-10, max=10)
		obj.addAttr('dewclaw_spread', k=1, min=-10, max=10)

		obj.addAttr('MISC', at='enum', en='--------:', k=1)
		obj.MISC.set(cb=1)

		obj.addAttr('fist', k=1, min=-10, max=10)
		obj.addAttr('spread', k=1, min=-10, max=10)
		obj.addAttr('Finger_icon_vis', k=1, at='enum', en='OFF:ON:')
		obj.addAttr('Knee_Pivot_vis', keyable=True , at='enum' , en='ON:OFF:')

def ikfk_switch(*args):

	import ikfk_tool
	reload(ikfk_tool)
	ikfk_tool.gui()

def polVec(*args):
	# jntChn = store joint chain working with
	jntChn=cmds.ls(selection=True , long=True , dag=True)

	# loc1 = create locator 1
	loc1=cmds.spaceLocator()[0]

	# grp2 = group locator 1
	grp1=cmds.group()

	# loc2 = create locator 2
	loc2=cmds.spaceLocator()[0]

	# grp1 = group locator 2
	grp2=cmds.group()

	# point constrain group 1 between root joint (jntChn) and end joint (jntChn) without offset
	cmds.pointConstraint(jntChn[0] , grp1 , mo=False)
	cmds.pointConstraint(jntChn[2] , grp1 , mo=False)

	# aim contrain group 1 from root joint
	cmds.aimConstraint(jntChn[0] , grp1 , wut='scene' , aim=(0,1,0) , u=(0,1,0))

	# point constrain locator 1 from center joint without offset (Y axis) 
	cmds.pointConstraint(jntChn[1] , loc1 , mo=False , sk=('x','z'))

	# point constrain group 2 (grp2) from center joint without offset
	cmds.pointConstraint(jntChn[1] , grp2 , mo=False)

	# aim constrain group 2 (grp2) from locator 1
	cmds.aimConstraint(loc1 , grp2 , wut='scene' , aim=(0,0,1) , u=(0,1,0))

	# trasnlate locator 2 to position
	cmds.xform(loc2 , t=(0,0,-5))

	# organiztion
	grp3=cmds.group(grp1 , grp2, n='polVec_loc')

def flexi_back(*args):
	if flexi_radio.getSelect() == 1:
		cmds.file('/Users/dean_13/Library/Preferences/Autodesk/maya/import_rigs/flexi_plane_spine_5jnt.mb', i=1)

	elif flexi_radio.getSelect() == 2:	
		cmds.file('/Users/dean_13/Library/Preferences/Autodesk/maya/import_rigs/flexi_plane_spine_9jnt.mb', i=1)

def annotation(*args):
	# select the joint, then the poleVec control

	sel = cmds.ls(sl=1)

	loc_1 = cmds.spaceLocator()
	loc_2 = cmds.spaceLocator()

	cmds.parentConstraint(sel[0], loc_1)
	cmds.parentConstraint(sel[1], loc_2)

	anno = cmds.annotate(loc_1, tx='', p=[0,0,0])

	anno_grp = cmds.group(anno)
	   
	cmds.parent(anno_grp, loc_2)

	cmds.xform(t=(0,0,0))

	cmds.group(loc_1, loc_2, n='annotation_grp_0#')

	cmds.select(cl=1)

	for obj in loc_1:
		shapeNodes=cmds.listRelatives(obj, shapes=1)
		for shape in shapeNodes:
			# locator visability
			cmds.setAttr("{0}.visibility".format(shape), 0)

	for obj in loc_2:
		shapeNodes=cmds.listRelatives(obj, shapes=1)
		for shape in shapeNodes:
			# locator visability
			cmds.setAttr("{0}.visibility".format(shape), 0)

	# for obj in anno:
	# 	shapeNodes=cmds.listRelatives(obj, shapes=1)
	# 	for shape in shapeNodes:
			
	# 		# annoation display as reference
	# 		cmds.setAttr("{0}.overrideEnabled".format(shape), 1)
	# 		cmds.setAttr("{0}.overrideDisplayType".format(shape), 2)

def reset(*args):
	print 'icon reset'

def flexi_arm(*args):
	if flexi_radio2.getSelect() == 1:
		cmds.file('/Users/dean_13/Library/Preferences/Autodesk/maya/import_rigs/flexi_plane_arm_5jnt.mb', i=1)

	elif flexi_radio2.getSelect() == 2:	
		cmds.file('/Users/dean_13/Library/Preferences/Autodesk/maya/import_rigs/flexi_plane_arm_9jnt.mb', i=1)
		print 'arm with more joints'

def tail_spline(*args):
	cmds.file('/Users/dean_13/Library/Preferences/Autodesk/maya/import_rigs/IK_spline_tail.mb', i=1)

def anim_icon_gen(*args):
	# select -cl  ;
	# select -r lt_back_knee_PV ;
	# select -tgl lt_front_knee_PV ;
	# setKeyframe -breakdown 0 -hierarchy none -controlPoints 0 -shape 0 {"lt_back_knee_PV", "lt_front_knee_PV"};
	# // Result: 24 //

	sel = cmds.ls(sl=1)
	anim_name = anim_field.getText()

	# mel.eval('$anim_name = circle()')
	
	if anim_radio.getSelect() == 1:
		print 'selct the given obj'

		# shelf_button = mel.eval('scriptToShelf("anim_name", $anim_name, false);')

		cmds.shelfButton(annotation='Create a cone.', image1='cone.png', command='cmds.cone()', imageOverlayLabel='4th')

		# cmds.shelfButton(i='sphere.png', c='cmds.sphere()')

		# python ("python goes here as a string");

	elif anim_radio.getSelect() == 2:
		print 'key the given attrs on the given obj'


