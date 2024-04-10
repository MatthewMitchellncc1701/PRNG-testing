"""
@authors: Matthew Mitchell

A way of testing and designing different PRNG

For usage, run with the -h flag

"""

import argparse
from datetime import datetime
import DoomRNG
import StackSins


def parse_all_args():
    # Parses commandline arguments

    parser = argparse.ArgumentParser()

    parser.add_argument("type", type=str, help="The PRNG type that you would like to run", default="doom")
    parser.add_argument("-seed", type=int, help="The seed that the prng should use, default is the current timestamp",
                        default=int(datetime.now().timestamp()))

    return parser.parse_args()


def main():
    """ Main program """
    args = parse_all_args()

    compare = args.type.lower()
    seed = args.seed

    if compare == "doom":
        print(DoomRNG.random(seed))
    elif compare == "stack":
        print(StackSins.random(seed))
    else:
        print("invalid option")

    return 0


if __name__ == "__main__":
    main()
