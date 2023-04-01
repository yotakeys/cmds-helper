from cmdshelper.helper import Helper
import sys

cmd = Helper()

# run using cli
cmd.run(sys.argv[1:])

# run using hardcode command
#cmd.run(["gitACP","feat: add something"])