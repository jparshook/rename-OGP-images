import pathlib
import argparse
import json
from typing import List

# https://docs.python.org/3.8/howto/argparse.html#id1
# https://docs.python.org/3.8/library/pathlib.html?highlight=pathlib#module-pathlib


def main(dest_folder: pathlib.Path, new_names: List[str]) -> None:

    for name in new_names:
        print(name)

    # for name1, name2 in zip(new_names, new_names2):
    #     print(f"{name1}: {name2}.bmp")
    # for src, dest in zip(filter(lambda p: p.is_file(), dest_folder.iterdir()), new_names):
    # for src, dest in zip(dest_folder.iterdir(), new_names):
        # print(f"{src}:{dest}")
    # sorted()
    # for count, src in enumerate(dest_folder.iterdir()):
    #     if not src.is_file():
    #         continue
    #     dst = new_names[count] + src.suffix
    #     # dst =f"{name}.{src.suffix}"
    #     src.rename(dest_folder / dst)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--directory")
    arg_parser.add_argument("--names")
    arg_parser.add_argument("--key")
#    print(arg_parser.parse_args())
    args = arg_parser.parse_args()
    folder = pathlib.Path(args.directory)
    with open(args.names, "r") as f:
        names = json.load(f)
    #print(names)
    main(folder, names[args.key])
