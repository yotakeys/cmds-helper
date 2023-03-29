import os
import json
import sys
import subprocess as sp

class Cmds:
    
    list_command = dict()
    
    def __init__(self):
        self.list_command = dict()
        self.readAllCmd()
    
    def changeParams(self, params:list, cmds:list) -> list :
    
        for index in range(len(params)):
            id = "%{i}".format(i=index+1)
            for cmd in range(len(cmds)):
                cmds[cmd] = cmds[cmd].replace(id,params[index])
            
            return cmds
       
       
    def readAllCmd(self):
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith("cmd.json"):
                    with open(os.path.join(root, file)) as json_file :
                        new_read =  json.load(json_file)
                        self.list_command.update(new_read) 
                        
    def runCmd(self, cmd:list):
        command = sys.argv[1]
        if command in self.list_command:
            if len(sys.argv) > 2:
                cmds = self.changeParams(sys.argv[2:], self.list_command[command])
                
            for cmd in cmds:
                cmd_split = cmd.split(",")
                sp.run(cmd_split, shell=True)
        else:
            print("Command not found")