import pathlib
import argparse

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--input")
    #print(arg_parser.parse_args())
    args = arg_parser.parse_args()
    print(args)
    print(args.input)
    #folder = pathlib.Path(args.directory)
    #with open(args.names, "r") as f:
    #    names = json.load(f)
    #print(names)
    ## folder = "CERN1/frontside inspection/before bonding"
    #main(folder, names[args.key])