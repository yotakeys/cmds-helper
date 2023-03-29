import sys
from cmds import Cmds

if __name__ == "__main__":
    CommandHelper = Cmds()
    CommandHelper.runCmd(sys.argv)