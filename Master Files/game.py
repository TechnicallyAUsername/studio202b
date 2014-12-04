"""This script is for the loading of game assets- levels, models, sounds, textures, and animations.
   Character movements can be in separate scripts. 
"""

# Connect both game.py and audio.py to the blender keyboard sensor

import bge; # Imports the blender game engine
import bpy;
import os.path;

import aud;
import audio; # Imports audio.py

device = aud.device();
# Use device.play(audio.drumloop1) to play sound

# Path for Characters
turtleCharacter = "../Models/turtle.blend"
rabbitCharacter = "../Models/rabbit.blend"

# Path for Levels
levelOne = "../Environments/level1withAddedForestAssets.blend" 
levelTwo = "../Environments/level2roughsketch.blend" 
levelThree = "../Environments/Cianna_CaveEnviro2.blend" 
levelFour = "../Environments/level5sky.blend"

# Variable for current level
currentLevel = 0;
  
co = bge.logic.getCurrentController()
sensor = co.sensors["Keyboard"]

	
def loadSoundbank():
    print ("sound loaded as global variables")

# This function is unnecessary, since it would be saved as global variables in audio.py
# Play sounds using the function "device.play(audio.drumloop1)"
# Audio files should be loaded into audio.py with variable name audio.soundName
# Make sure audio.py is connected to the same sensor as game.py controller

def loadAsset(x):
    path = bge.logic.expandPath("//" + x);
    print ("loading asset" + path);
    bge.logic.LibLoad(path,"Scene",load_actions=True);
	
def unloadAsset(x):
	path = bge.logic.expandPath("//" + x);
	print("unloading asset: " + path);
	bge.logic.LibFree(path);

# Need to load levels in order: 1, 2, 3, and 4
# Upon level load audio files load
def loadLevel(lvl):
    print("Load Level" + str(lvl));
    if lvl == 1:
        currentLevel = 1;
        device.play(audio.drumloop1)
        loadAsset(levelOne);
    if lvl == 2:
        unloadLevel(1);
        currentLevel = 2;
        device.play(audio.drumloop2)
        loadAsset(levelTwo);
    if lvl == 3:
        unloadLevel(2);
        currentLevel = 3;
        device.play(audio.drumloop3)
        loadAsset(levelThree);
    if lvl == 4:
        unloadLevel(3);
        currentLevel = 4;
        device.play(audio.drumloop4)
        loadAsset(levelFour);
    loadAsset(turtleCharacter);
    loadAsset(rabbitCharacter);

def unloadLevel(lvl):
    unloadAsset(turtleCharacter);
    unloadAsset(rabbitCharacter);
    if lvl == 1:
        unloadAsset(levelOne);
    if lvl == 2:
        unloadAsset(levelTwo);
    if lvl == 3:
        unloadAsset(levelThree);
    if lvl == 4:
        unloadAsset(levelFour);

def startup():
    print("Game is starting up! Press the number keys to load different levels."); #verifies that game is running
    currentLevel = 0;
    loadLevel(1);

for key,status in sensor.events:
    if status == bge.logic.KX_INPUT_JUST_ACTIVATED:
        # Use 1,2,3,4 keys to load different levels
        if key == bge.events.ONEKEY:
            loadLevel(1);
        if key == bge.events.TWOKEY:
            loadLevel(2);
        if key == bge.events.THREEKEY:
            loadLevel(3);
        if key == bge.events.FOURKEY:
            loadLevel(4);

