import subprocess as sp
import sys
import os
import json

def changeParams(params, cmds):
    
    for index in range(len(params)):
        id = "%{i}".format(i=index+1)
        for cmd in range(len(cmds)):
            cmds[cmd] = cmds[cmd].replace(id,params[index])
        
        return cmds
       
       
def readAllCmd():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith("cmd.json"):
                with open(os.path.join(root, file)) as json_file :
                    new_read =  json.load(json_file)
                    list_command.update(new_read) 


list_command = dict()
readAllCmd()
command = sys.argv[1]
if command in list_command:
    if len(sys.argv) > 2:
        cmds = changeParams(sys.argv[2:], list_command[command])
        
    for cmd in cmds:
        cmd_split = cmd.split(",")
        out = sp.run(cmd_split, shell=True)
else:
    print("Command not found")


