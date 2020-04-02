from PIL import Image
import os
import sys
import re

def	ListFolder(path):
	List = []
	for i in os.listdir(path):
		List.append(i)
	return List

def PythonLocation():
	return os.path.dirname(os.path.realpath(__file__))

def SignatureCommond(_APKLocation):
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	# foldername=APKname[:PointCount]
	APKname[:PointCount]
	if os.path.exists(PythonLocation()+"/__pycache__/META-INF")==False:
		print("Your APK don't have META-INF folder")
		return
	MySignature = ListFolder(PythonLocation()+"/__pycache__/META-INF")
	for name in MySignature:
		if ".RSA" in name:
			os.system("keytool -printcert -file "+PythonLocation()+"/__pycache__/META-INF/"+name)
if __name__=='__main__':
	game_name = input("input game id:")
	SignatureCommond(game_name)