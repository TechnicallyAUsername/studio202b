#Grabbed this code from stackoverflow, credit to lucblender
#The goal of this code is to parent the camera to the turtle character

import bpy
def bindCamera():
	a = bpy.data.objects['Camera']
	b = bpy.data.objects['metarig']

	bpy.ops.object.select_all(action='DESELECT') #deselect all object

	a.select = True
	b.select = True     #select the object for the 'parenting'

	bpy.context.scene.objects.active = a    #the active object will be the parent of all selected object

	bpy.ops.object.parent_set()

	#Now The parent of b is a