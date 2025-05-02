import sys
import os
from myKwargs import MyKwargs

if __name__ == "__main__":
    # Get the current file path
    current_file_path = os.path.abspath(__file__)

    # Get the directory of the current file
    current_dir = os.path.dirname(current_file_path)

    print(current_dir)

    sys.argv[0] = current_file_path

    # call kwargs removing filename
    args, kargs = MyKwargs(sys.argv[1:])

    print(args)
    print(kargs)