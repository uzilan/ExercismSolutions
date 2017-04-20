from os import path, getcwd, sep, system, listdir, remove
from sys import argv, exit
from shutil import copy2

def printUsage():
	print('Usage:')
	print('    From exercise directory: update.py')
	print('    From track directory: update.py <exercise>')
	print('    From root directory: update.py <track> <exercise>')
	
if __name__ == '__main__':
	cwd = getcwd()
	parts = cwd.split(sep)
	exercise = parts[-1]
	track = parts[-2]
	if track == 'ExercismSolutions':
		track = exercise
		if len(argv) < 2:
			printUsage()
			exit(1)
		exercise = argv[1]
		cwd = path.join(cwd,exercise)
	elif exercise == 'ExercismSolutions':
		if len(argv) < 3:
			if len(argv) == 2 and path.isdir(argv[1]):
				track,exercise = argv[1].split(sep)
			else:
				printUsage()
				exit(1)
		else:
			track = argv[1]
			exercise = argv[2]
		cwd = path.join(cwd,track,exercise)
	print('Track: {}'.format(track))
	print('Exercise: {}'.format(exercise))
	print(cwd)
	for item in listdir(cwd):
		name = path.join(cwd,item)
		if not path.isfile(name): continue
		if name.endswith('Test.cs'):
			print('Removing test file "{}"...'.format(item))
			remove(name)
		elif name.endswith('.csproj'):
			print('Removing project file "{}"...'.format(item))
			remove(name)
		elif name.endswith('.cs'):
			print('Backing up source file "{}"...'.format(item))
			copy2(name, name + '.bak')
	system('exercism f {} {}'.format(track, exercise))
	for item in listdir(cwd):
		name = path.join(cwd,item)
		if not path.isfile(name): continue
		if name.endswith('.bak'):
			print('Restoring backed up source file "{}"...'.format(item))
			copy2(name,name.replace('.bak',''))
			remove(name)
	print('Done.')