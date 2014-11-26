import bge;
def placement():
	print("This is new code from outside!");
	controller = bge.logic.getCurrentController(); # get the logic controller 
	sphere = controller.owner; # it's parent is the Sphere object we created
	sphere.position = [0,-7,10]; # reposition back to up in the air

	Stair1 = bge.logic.getCurrentScene().objects['Stair1'];
	Stair2 = bge.logic.getCurrentScene().objects['Stair2'];
	Stair1.position = [-12.45472,3.90876,-1.75446]; # Place Stair1
	Stair2.position = [-12.45472,8.17876,0.06554]; # Place Stair2
	
def hiding():
	print("our code is running!");
	controller = bge.logic.getCurrentController(); # get the logic controller 
	sphere = controller.owner; # it's parent is the Sphere object we created
	Stair1 = bge.logic.getCurrentScene().objects['Stair1'];
	Stair2 = bge.logic.getCurrentScene().objects['Stair2'];
	Stair1.position = [0,0,-5]; # Hide Stair 1
	Stair2.position = [0,0,-5]; # Hide Stair 2