import os

def mkdir(_name):
	if os.path.exists(_name) == False:
		os.mkdir(_name)
		print "\nThe directory was created successfully."