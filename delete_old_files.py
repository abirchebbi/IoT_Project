import datetime
import glob
import os
from time import sleep

PATH_I = '../images/'
PATH_V = '../videos/'
Format = "%Y.%m.%d-%H:%M:%S"

while True:
	sleep(5) 

	files = glob.glob(PATH_I +'*')

	minute_ago = datetime.datetime.now() - datetime.timedelta(minutes=1)
	for file in files:

		# get and cast the name to retreive the date
		name = str.split(file, '/')[-1]
		name = str.split(name, '.')[:-1]
		time = datetime.datetime.strptime(name[0] + '.' + name[1] + '.' + name[2], Format)

		# si l'image a ete prise il y'a plus d'une minute
		if(time < minute_ago):
		    os.remove(file)
		    print(file, " is deleted")

	files = glob.glob(PATH_V +'*')
		    
	for file in files:

		# get and cast the name to retreive the date
		name = str.split(file, '/')[-1]
		name = str.split(name, '.')[:-1]
		time = datetime.datetime.strptime(name[0] + '.' + name[1] + '.' + name[2], Format)

		# si l'image a ete prise il y'a plus d'une minute
		if(time < minute_ago):
		    os.remove(file)
		    print(file, " is deleted")



