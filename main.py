import subprocess as sp
import sys
import  json

def changeParams(params, cmds):
    
    for index in range(len(params)):
        id = "%{i}".format(i=index+1)
        for cmd in range(len(cmds)):
            cmds[cmd] = cmds[cmd].replace(id,params[index])
        
        return cmds
        

with open("test.json") as json_file:
    command = sys.argv[1]
    list_command =  json.load(json_file)
    if command in list_command:
        if len(sys.argv) > 2:
            cmds = changeParams(sys.argv[2:], list_command[command])
        
        for cmd in cmds:
            cmd_split = cmd.split(",")
            out = sp.run(cmd_split, shell=True)
    else:
        print("Command not found")
    