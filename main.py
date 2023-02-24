import subprocess as sp
import sys

cmd = sys.argv[1]

if(cmd == "git"):
    out = sp.run(["git","add","."], shell=True)
    out = sp.run(["git","commit","-m",'"feat: add simple logic"'], shell=True)
    out = sp.run(["git","push"], shell=True)
    