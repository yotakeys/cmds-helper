import subprocess as sp
import sys
import  json

with open("test.json") as json_file:
    command = sys.argv[1]
    list_command =  json.load(json_file)
    if command in list_command:
        for cmd in list_command[command]:
            cmd_split = cmd.split(",")
            out = sp.run(cmd_split, shell=True)
    else:
        print("Command not found")
    