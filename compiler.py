# This will only run if you have python installed and run in macos(Bcause i don't have multiple computers :v)
import subprocess
import os

#Clear the terminal before run code
subprocess.run("clear")

#Split the name and extension that users type in
name = input("Enter file name and extension: ")
name = name.split(".")
dir = name[0]
type = name[1]
type = type.lower()
commands = []

#Explain: Type anything in and it will use the current directory that contain the compiler.py
directory = input("Enter file directory(Default: current file directory)\n> ")
try:
	os.chdir(directory)
except FileNotFoundError:
	directory2 = os.getcwd()
	os.chdir(directory2)

#Code to insert different commands base on extension type
if type == "java":
	commands = [["echo",""],["javac",f"{dir}.java"],["java",f"{dir}"],["rm",f"{dir}.class"]]
elif type == "py":
	commands = [["echo",""],["python3",f"{dir}.py"]]
elif type == "c":
	commands = [["echo",""],["gcc",f"{dir}.c","-o","Output"],["./Output"],["rm","Output"]]

for command in commands:
	subprocess.run(command, check=True)
