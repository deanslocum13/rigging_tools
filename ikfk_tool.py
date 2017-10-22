'''
Dean Slocum
hybrid_face_control.py

Description:

	A fast and easy way to create an IK/FK arm or leg with auto switching.
	All you need to due is plug in the objects and run the code.

How to Run:

import ikfk_tool
reload(ikfk_tool)
ikfk_tool.gui()

'''

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel

win = 'IK/FK Tool Kit'
print 'IK/FK Tool Kit Activated'

w = 100
h = 200
w2 = 84
w3 = 5
w4 = 5
h2 = 6
b1 = [0,.5,0]
b2 = [0,.5,.5]
b3 = [.5,.6,.5]

def gui():

	if(cmds.window(win , ex=1)):
		cmds.deleteUI(win)
	if (cmds.windowPref(win , ex=1)):
		cmds.windowPref(win , r=1)

	global ik_field, polVec_field, fk_root_field, fk_mid_field, fk_end_field, switch_field, system_name_field

	cmds.window(win , s=1, vis=1, w=w , h=h)

	cmds.rowColumnLayout()

	cmds.frameLayout(l='IK', bgc=b1)
	cmds.rowColumnLayout(nc=5)

	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)

	cmds.text(l='IK Icon: ', al='right', w=w2)
	ik_field = pm.textField('ik_field', ed=0, bgc=b3)
	cmds.text(' ', w=w3)
	cmds.button(l='LOAD', c=pm.Callback(load_icon, 'ik_field', None), bgc=b2)
	cmds.text(' ', w=w4)

	cmds.text(l='Pole Vec Icon: ', al='right', w=w2)
	polVec_field = pm.textField('polVec_field', ed=0, bgc=b3)
	cmds.text(' ', w=w3)
	cmds.button(l='LOAD', c=pm.Callback(load_icon, 'polVec_field', None), bgc=b2)
	cmds.text(' ', w=w4)

	cmds.setParent('..')

	cmds.frameLayout(l='FK', bgc=b1)
	cmds.rowColumnLayout(nc=5)

	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)

	cmds.text(l='FK Root Icon: ', al='right', w=w2)
	fk_root_field = pm.textField('fk_root_field',ed=0, bgc=b3)
	cmds.text(' ', w=w3)
	cmds.button(l='LOAD', c=pm.Callback(load_icon, 'fk_root_field', None), bgc=b2)
	cmds.text(' ', w=w4)

	cmds.text(l='FK Mid Icon: ', al='right', w=w2)
	fk_mid_field = pm.textField('fk_mid_field',ed=0, bgc=b3)
	cmds.text(' ', w=w3)
	cmds.button(l='LOAD', c=pm.Callback(load_icon, 'fk_mid_field', None), bgc=b2)
	cmds.text(' ', w=w4)

	cmds.text(l='FK End Icon: ', al='right', w=w2)
	fk_end_field = pm.textField('fk_end_field',ed=0, bgc=b3)
	cmds.text(' ', w=w3)
	cmds.button(l='LOAD', c=pm.Callback(load_icon, 'fk_end_field', None), bgc=b2)
	cmds.text(' ', w=w4)

	cmds.setParent('..')

	cmds.frameLayout(l='SWITCH', bgc=b1)
	cmds.rowColumnLayout(nc=5)

	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)

	cmds.text(l='Switch Icon: ', al='right', w=w2)
	switch_field = pm.textField('switch_field',ed=0, bgc=b3)
	cmds.text(' ', w=w3)
	cmds.button(l='LOAD', c=pm.Callback(load_icon, 'switch_field', None), bgc=b2)
	cmds.text(' ', w=w4)

	cmds.setParent('..')

	cmds.frameLayout(l='SYSTEM NAME', bgc=b1)
	cmds.rowColumnLayout(nc=3)

	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)

	cmds.text(l='System Name: ', al='right', w=w2)
	system_name_field = pm.textField('name_field',ed=1, bgc=[.5,.5,.7], pht='lt_arm, etc.')

	cmds.text(' ', h=h2)

	cmds.text(' ', h=20)
	cmds.text(' ', h=20)
	cmds.text(' ', h=20)

	cmds.text(' ', h=h2)

	cmds.button(l='CREATE', c=create, bgc=b2)

	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)
	cmds.text(' ', h=h2)

	cmds.setParent('..')

	cmds.showWindow()

def load_icon(load_field, set_field):
	icon = cmds.ls(sl=1)[0]
	pm.textField(load_field, e=True, tx=icon)
	set_textFieldFocus(set_field)
	cmds.select(cl=1)

def set_textFieldFocus(text_field):
	pm.setFocus(text_field)

def create(*args):
	ik_icon = ik_field.getText()
	polVec_icon = polVec_field.getText()
	fk_root_icon = fk_root_field.getText()
	fk_mid_icon = fk_mid_field.getText()
	fk_end_icon = fk_end_field.getText()
	switch_icon = switch_field.getText()
	system_name = system_name_field.getText()

	baseArm = cmds.ls(sl=1, dag=1)

	FKArm=cmds.duplicate(baseArm[0], rc=1)

	IKArm=cmds.duplicate(baseArm[0], rc=1)

	#create a blendColors node	shadingnode -asUtility blendColors;
	rootCBlend=cmds.shadingNode('blendColors', asUtility=1, n=baseArm[0]+'IKFKCB')
	midCBlend=cmds.shadingNode('blendColors', asUtility=1, n=baseArm[1]+'IKFKCB')
	endCBlend=cmds.shadingNode('blendColors', asUtility=1, n=baseArm[2]+'IKFKCB')

	#use connection editor for the blendColors
	cmds.connectAttr((FKArm[0]+'.rotate'), (rootCBlend+'.color1'), f=1)
	cmds.connectAttr((IKArm[0]+'.rotate'), (rootCBlend+'.color2'), f=1)
	cmds.connectAttr((rootCBlend+'.output'), (baseArm[0]+'.rotate'), f=1)

	cmds.connectAttr((FKArm[1]+'.rotate') , (midCBlend+'.color1') , f=1)
	cmds.connectAttr((IKArm[1]+'.rotate') , (midCBlend+'.color2') , f=1)
	cmds.connectAttr((midCBlend+'.output') , (baseArm[1]+'.rotate') , f=1)

	cmds.connectAttr((FKArm[1]+'.rotate') , (endCBlend+'.color1') , f=1)
	cmds.connectAttr((IKArm[1]+'.rotate') , (endCBlend+'.color2') , f=1)
	cmds.connectAttr((endCBlend+'.output') , (baseArm[1]+'.rotate') , f=1)

	#make an attribute
	cmds.addAttr(switch_icon, ln='IKFK', at='double', min=0, max=10, k=1)
	cmds.addAttr(switch_icon, ln='IK_icon_vis', at='enum', en='ON:OFF:', k=1)
	cmds.addAttr(switch_icon, ln='FK_icon_vis', at='enum', en='OFF:ON:', k=1)

	#sdk for switch
	cmds.setDrivenKeyframe((rootCBlend+'.blender'), v=0 , cd=(switch_icon+'.IKFK'), dv=0)
	cmds.setDrivenKeyframe((rootCBlend+'.blender'), v=1 , cd=(switch_icon+'.IKFK'), dv=10)

	cmds.setDrivenKeyframe((midCBlend+'.blender'), v=0 , cd=(switch_icon+'.IKFK'), dv=0)
	cmds.setDrivenKeyframe((midCBlend+'.blender'), v=1 , cd=(switch_icon+'.IKFK'), dv=10)

	cmds.setDrivenKeyframe((endCBlend+'.blender'), v=0 , cd=(switch_icon+'.IKFK'), dv=0)
	cmds.setDrivenKeyframe((endCBlend+'.blender'), v=1 , cd=(switch_icon+'.IKFK'), dv=10)

	switch_local = cmds.group(em=1, n=switch_icon+'_local')
	switch_pad = cmds.group(switch_local, n=switch_icon+'_pad')

	cmds.delete(cmds.parentConstraint(baseArm[2], switch_pad))

	cmds.parent(switch_icon, switch_local)

	cmds.parentConstraint(baseArm[2], switch_pad, mo=1, w=1)

	cmds.makeIdentity(switch_icon, apply=1, t=1, r=1, s=1, n=0)

	#add the ikHandle
	ARMIK=cmds.ikHandle(sj=IKArm[0], ee=IKArm[2], sol='ikRPsolver', n=IKArm[0]+'_IKHandle')

	cmds.pointConstraint(ik_icon, ARMIK[0], mo=0, w=1)

	ik_icon_local = cmds.group(em=1, n=ik_icon+'_local')
	ik_icon_pad = cmds.group(ik_icon_local, n=ik_icon+'_pad')

	cmds.delete(cmds.parentConstraint(baseArm[2], ik_icon_pad))

	cmds.parent(ik_icon, ik_icon_local)
	
	#freeze
	cmds.makeIdentity(ik_icon, apply=1, t=1, r=1, s=1, n=0)

	#parent the joint
	cmds.parent(fk_root_icon, FKArm[0])

	#double group
	cmds.group(n=fk_root_field.getText()+'_local')
	cmds.group(n=fk_root_field.getText()+'_pad')

	#unparent
	cmds.parent(w=1)

	#freeze
	cmds.makeIdentity(fk_root_icon, apply=1, t=1, r=1, s=1, n=0)

	#orient constrain back to the joints
	cmds.orientConstraint(fk_root_icon, FKArm[0], mo=0)

	#parent the joint
	cmds.parent(fk_mid_icon, FKArm[1])

	#double group
	cmds.group(n=fk_mid_field.getText()+'_local')
	midTrashPad=cmds.group(n=fk_mid_field.getText()+'_pad')

	#unparent
	cmds.parent(w=1)

	#freeze
	cmds.makeIdentity(fk_mid_icon, apply=1, t=1, r=1, s=1, n=0)

	#orient constrain back to the joints
	cmds.orientConstraint(fk_mid_icon, FKArm[1], mo=0)

	#parent elbow trash pad to shoulder control
	cmds.parent(midTrashPad, fk_root_icon)

	#parent the joint
	cmds.parent(fk_end_icon, FKArm[2])

	#double group
	cmds.group(n=fk_end_field.getText()+'_local')
	endTrashPad=cmds.group(n=fk_end_field.getText()+'_pad')

	#unparent
	cmds.parent(w=1)

	#freeze
	cmds.makeIdentity(fk_end_icon, apply=1, t=1, r=1, s=1, n=0)

	#orient constrain back to the joints
	cmds.orientConstraint(fk_end_icon, FKArm[2], mo=0)

	#parent elbow trash pad to shoulder control
	cmds.parent(endTrashPad, fk_mid_icon)

	#sdk for FK icon visability
	cmds.setDrivenKeyframe((fk_root_icon+'.visibility'), v=0, cd=(switch_icon+'.FK_icon_vis'), dv=0)
	cmds.setDrivenKeyframe((fk_root_icon+'.visibility'), v=1, cd=(switch_icon+'.FK_icon_vis'), dv=1)

	cmds.setDrivenKeyframe((fk_mid_icon+'.visibility'), v=0, cd=(switch_icon+'.FK_icon_vis'), dv=0)
	cmds.setDrivenKeyframe((fk_mid_icon+'.visibility'), v=1, cd=(switch_icon+'.FK_icon_vis'), dv=1)

	cmds.setDrivenKeyframe((fk_end_icon+'.visibility'), v=0, cd=(switch_icon+'.FK_icon_vis'), dv=0)
	cmds.setDrivenKeyframe((fk_end_icon+'.visibility'), v=1, cd=(switch_icon+'.FK_icon_vis'), dv=1)

	cmds.setDrivenKeyframe((ik_icon+'.visibility'), v=1, cd=(switch_icon+'.IK_icon_vis'), dv=0)
	cmds.setDrivenKeyframe((ik_icon+'.visibility'), v=0, cd=(switch_icon+'.IK_icon_vis'), dv=1)

	cmds.poleVectorConstraint(polVec_icon, ARMIK[0])

	cmds.hide(ARMIK)

	#rename for FK
	count2 = 1
	
	for each in FKArm:
		count2 = count2 + 1
		newFKName = '{0}_{1:02d}_{2}'.format(system_name, count2, 'FK')
		cmds.rename(each, newFKName)
		
	#rename for IK	
	count3 = 1
	
	for each in IKArm:
		count3 = count3 + 1
		newIKName = '{0}_{1:02d}_{2}'.format(system_name, count3, 'IK')
		cmds.rename(each, newIKName)

	cmds.select(cl=1)

	cmds.rename(ik_icon, 'ik_icon')
	cmds.rename(switch_icon, 'IK_FK_switch_icon')
	cmds.rename(fk_root_icon, 'fk_root_icon')
	cmds.rename(fk_mid_icon, 'fk_mid_icon')
	cmds.rename(fk_end_icon, 'fk_end_icon')
	cmds.rename(polVec_icon, 'polVec_icon')

	cmds.setAttr('ik_icon.scaleX', l=1, k=0)
	cmds.setAttr('ik_icon.scaleY', l=1, k=0)
	cmds.setAttr('ik_icon.scaleZ', l=1, k=0)
	cmds.setAttr('ik_icon.visibility', l=1, k=0)

	cmds.setAttr('IK_FK_switch_icon.translateX', l=1, k=0)
	cmds.setAttr('IK_FK_switch_icon.translateY', l=1, k=0)
	cmds.setAttr('IK_FK_switch_icon.translateZ', l=1, k=0)
	cmds.setAttr('IK_FK_switch_icon.rotateX', l=1, k=0)
	cmds.setAttr('IK_FK_switch_icon.rotateY', l=1, k=0)
	cmds.setAttr('IK_FK_switch_icon.rotateZ', l=1, k=0)
	cmds.setAttr('IK_FK_switch_icon.scaleX', l=1, k=0)
	cmds.setAttr('IK_FK_switch_icon.scaleY', l=1, k=0)
	cmds.setAttr('IK_FK_switch_icon.scaleZ', l=1, k=0)
	cmds.setAttr('IK_FK_switch_icon.visibility', l=1, k=0)

	cmds.setAttr('fk_root_icon.translateX', l=1, k=0)
	cmds.setAttr('fk_root_icon.translateY', l=1, k=0)
	cmds.setAttr('fk_root_icon.translateZ', l=1, k=0)
	cmds.setAttr('fk_root_icon.scaleX', l=1, k=0)
	cmds.setAttr('fk_root_icon.scaleY', l=1, k=0)
	cmds.setAttr('fk_root_icon.scaleZ', l=1, k=0)
	cmds.setAttr('fk_root_icon.visibility', l=1, k=0)

	cmds.setAttr('fk_mid_icon.translateX', l=1, k=0)
	cmds.setAttr('fk_mid_icon.translateY', l=1, k=0)
	cmds.setAttr('fk_mid_icon.translateZ', l=1, k=0)
	cmds.setAttr('fk_mid_icon.scaleX', l=1, k=0)
	cmds.setAttr('fk_mid_icon.scaleY', l=1, k=0)
	cmds.setAttr('fk_mid_icon.scaleZ', l=1, k=0)
	cmds.setAttr('fk_mid_icon.visibility', l=1, k=0)

	cmds.setAttr('fk_end_icon.translateX', l=1, k=0)
	cmds.setAttr('fk_end_icon.translateY', l=1, k=0)
	cmds.setAttr('fk_end_icon.translateZ', l=1, k=0)
	cmds.setAttr('fk_end_icon.scaleX', l=1, k=0)
	cmds.setAttr('fk_end_icon.scaleY', l=1, k=0)
	cmds.setAttr('fk_end_icon.scaleZ', l=1, k=0)
	cmds.setAttr('fk_end_icon.visibility', l=1, k=0)

	cmds.setAttr('polVec_icon.scaleX', l=1, k=0)
	cmds.setAttr('polVec_icon.scaleY', l=1, k=0)
	cmds.setAttr('polVec_icon.scaleZ', l=1, k=0)
	cmds.setAttr('polVec_icon.visibility', l=1, k=0)

	cmds.rename('ik_icon', ik_field.getText())
	cmds.rename('IK_FK_switch_icon', switch_field.getText())
	cmds.rename('fk_root_icon', fk_root_field.getText())
	cmds.rename('fk_mid_icon', fk_mid_field.getText())
	cmds.rename('fk_end_icon', fk_end_field.getText())
	cmds.rename('polVec_icon', polVec_field.getText())

















