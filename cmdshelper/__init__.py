from .helper import Helper
import argparse
import os


def main():
    """Main program entrypoint."""

    # Get command arguments
    parser = argparse.ArgumentParser(
        description="Check every single imported python module(s) on your project and install it automatically"
    )
    parser.add_argument(
        "cmd",
        metavar="cmd",
        type=str,
        help="The command that want to execute"
    )

    parser.add_argument(
        "args",
        metavar="args",
        type=str,
        nargs="+",
        help="Arguments to the command",
    )

    # parser.add_argument(
    #     "-i",
    #     "--install",
    #     action="store_true",
    #     help="Install the missing dist"
    # )

    cmd = Helper(os.getcwd())

    args = parser.parse_args()

    if args.cmd != "":
        cmd_and_args = [args.cmd] + args.args
        cmd.run(cmd_and_args)

    else:
        print('Give the command!')
        print('~ python -m cmds-helper [cmd] [args_1] [args_2] ... [args_n]')


if __name__ == "__main__":
    main()
