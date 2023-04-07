import os
import json
import re
import subprocess as sp


class Helper:

    list_command = dict()

    def __init__(self, abs_path='.'):
        self.list_command = dict()
        self.readAllCmd(abs_path)

    # def changeParams(self, params: list, cmds: list) -> list:
    #     for index in range(len(params)):
    #         id = "%{i}".format(i=index+1)
    #         for cmd in range(len(cmds)):
    #             cmds[cmd] = cmds[cmd].replace(id, "\"{params[index]}\"")

    #         return cmds

    def changeParams(self, params: list, cmds: list) -> list:
        for i in range(len(params)):
            cmds = list(
                map(lambda cmd: [params[i] if val == f'%{i+1}' else val for val in cmd], cmds))

        return cmds

    def readAllCmd(self, abs_path):
        for root, dirs, files in os.walk(abs_path):
            for file in files:
                if file.endswith("cmd.json"):
                    with open(os.path.join(root, file)) as json_file:
                        new_read = json.load(json_file)
                        self.list_command.update(new_read)

    def extract_command(string):
        pattern = r'(?<!\\)(?:"[^"]*"|[^\s"]+)'
        args = re.findall(pattern, string)
        command = args.pop(0)
        command = re.sub(r'\\(.)', r'\1', command)
        allin = [command] + args
        return allin

    def run(self, cmd: list):
        command = cmd.pop(0)
        if command in self.list_command:
            if len(cmd):
                cmds_list = list(map(Helper.extract_command,
                                 self.list_command[command]))
                cmds = self.changeParams(cmd, cmds_list)

            for cmd in cmds:
                sp.run(cmd, shell=True)
        else:
            print("Command not found")
