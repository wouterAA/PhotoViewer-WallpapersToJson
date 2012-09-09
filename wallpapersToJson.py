import os
import json
from random import choice

path = "C:/Users/Wouter/Desktop/wallpapers/"

with open("dates.txt") as f:
		dates = f.readlines()

with open("names.txt") as f:
		names = f.readlines()

jsonList = list()
for wallpaper in os.listdir(path):
	wallpaperDict = dict()

	try:
		id = wallpaper.rsplit("-")[1]
		wallpaperDict["id"] = int(id.rsplit(".")[0])
	except:
		print "Wrong ID: " + wallpaper

	wallpaperDict["photolocation"] = "http://static.woutervanderaa.nl/images/cria/wallpapers/{0}".format(wallpaper)
	wallpaperDict["landscape"] = True
	wallpaperDict["description"] = ""
	wallpaperDict["date"] = choice(dates).strip()
	wallpaperDict["photographer"] = choice(names).strip()

	jsonList.append(wallpaperDict)


json = json.dumps(jsonList)

with open("wallpapersjson.txt", "w") as f:
	f.write(json)