import bge;
def placeRamp():
	print("Placing Ramp!");
	controller = bge.logic.getCurrentController(); # get the logic controller
	cube = controller.owner; # owner of controller
	Ramp = bge.logic.getCurrentScene().objects['Ramp'];
	Ramp.position = [13.73525,1.78098,3.51083]; # reposition back to up in the air
	
def hideWall():
	controller = bge.logic.getCurrentController(); # get the logic controller
	cube = controller.owner; # 
	BrickWall = bge.logic.getCurrentScene().objects['BrickWall'];
	BrickWall.position = [0,0,-13]; # Hide Brick Wall