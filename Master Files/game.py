"""This script is for the loading of game assets- levels, models, sounds, textures, and animations.
   Character movements can be in separate scripts. It is all based off of Dr. 0's code from the example.
"""

import bge; #imports the blender game engine
import bpy;
import os.path;
turtleCharacter = "../Models/turtle.blend"
rabbitCharacter = "../Models/rabbit.blend"
levelOne = "../Environments/level1withAddedForestAssets.blend" #this is the path for level one
levelTwo = "../Environments/level2roughsketch.blend" #this is the path for level two
levelThree = "../Environments/Cianna_CaveEnviro2.blend" #this is the path for level three
levelFour = "../Environments/level5sky.blend"

def startup():
	print("Game is starting up! Press the number keys to load different levels. Please only press in order, or the game may crash."); #verifies that game is running
	loadSoundbank();
	
def loadSoundbank():
	print("Soundbank loaded! Well, it will be when we make it");
	
def loadAsset(x):
	path = bge.logic.expandPath("//" + x); #the // chooses the directory the main blender file is in, the x is the rest of the path
	print ("loading asset" + path); #this prints what's being loaded in the console to let you know what's happening
	bge.logic.LibLoad(path,"Scene",load_actions=True); # I don't know what this does. This was taken from Dr. 0's code
	
def unloadAsset(x):
	path = bge.logic.expandPath("//" + x);
	print("unloading asset: " + path);
	y = bge.logic.LibFree(path);
	
def loadLevelOne():
	print("Load Level One");
	loadAsset(levelOne);
	loadAsset(turtleCharacter);
	loadAsset(rabbitCharacter);

#Now The parent of b is a
	#os.system("cameraParent.bindCamera");
	#Camera.position = [0,0,100]; # moveCamera
	
def unloadLevelOne():
	print("unloading level one");
	unloadAsset(levelOne);
	unloadAsset(turtleCharacter);
	unloadAsset(rabbitCharacter);

def loadLevelTwo(): #Loads level 2
	print("Load Level Two");
	unloadLevelOne();
	loadAsset(levelTwo);
	loadAsset(turtleCharacter);
	loadAsset(rabbitCharacter);
	
def unloadLevelTwo(): #unloads level 2
	print("unloading level two");
	unloadAsset(levelTwo);
	unloadAsset('turtleCharacter');
	unloadAsset(rabbitCharacter);

def loadLevelThree(): #loads level 3
	print("load Level Three");
	unloadLevelTwo();
	loadAsset(levelThree);
	loadAsset(turtleCharacter);
	loadAsset(rabbitCharacter);
	
def unloadLevelThree(): #unloads level 3
	print("unloading level three");
	unloadAsset(levelThree);
	unloadAsset('turtleCharacter');
	unloadAsset(rabbitCharacter);
	
def loadLevelFour():
	print("loading level four");
	unloadLevelThree();
	loadAsset(levelFour);
	loadAsset(turtleCharacter);
	loadAsset(rabbitCharacter);
	
def LoadRabbit():
	loadAsset(rabbitCharacter);
	

	
