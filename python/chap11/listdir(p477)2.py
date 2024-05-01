import os

cwd = os.getcwd()
print(cwd)
files = os.listdir()
print(files)
for name in files :
	if os.path.isfile(name) :
		if name.endswith(".txt") :
			print(name)
