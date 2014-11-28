import bge; #imports the blender game engine
import os.path;

def startup():
	print("Game is starting up"); #verifies that game is running
	loadSoundbank();
	#loadLevelOne();
	
def loadSoundbank():
	print("Soundbank loaded! Well, it will be when we make it");
	
def loadAsset(x):
	path = bge.logic.expandPath("//" + x);
	print ("loading asset" + path);
	bge.logic.LibLoad(path,"Scene",load_actions=True);
	
def unloadAsset(x):
	path = bge.logic.expandPath("//" + x);
	print("unloading asset: " + path);
	y = bge.logic.LibFree(path);
	
def loadLevelOne():
	print("Load Level One");
	loadAsset('testLevel.blend');
	
def unloadLevelOne():
	print("unloading level one");
	unloadAsset('testLevel.blend');

def loadLevelTwo():
	print("Load Level Two");
	unloadLevelOne();
	loadAsset('TestFolder/red.blend');
	
def loadLevelThree():
	print("load Level Three");
	loadAsset('../Cianna_CaveEnviro2.blend');

	
