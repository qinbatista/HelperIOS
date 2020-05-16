import sys, os, platform
import shutil
def PythonLocation():
	return os.path.dirname(os.path.realpath(__file__))

def main():
	os.chdir(PythonLocation())
	with open(f"./CodeAddress.txt",encoding="utf8") as file_object:
		sdk_xml = file_object.readlines()
		for i in sdk_xml:
			if i.find("git clone ssh://")!=-1:
				print("downloading codes")
				os.system(i)

if __name__ == '__main__':
	main()