import os
import sys

def trim_object(data, n, filename, dest):
    if os.path.exists(dest):
        print(f"will remove & overwrite the last result of {dest}")
        status = input("are you sure to continue & replace? y/n : ")
        if status.lower() not in ("y", "yes"):
            sys.exit(1)

    viewsource = data[:int(n)]
    remove = []
    with open(dest, "w") as f:
        for out in viewsource:
            print(out, end='')
            remove.append(out)
            f.write(out)

    with open(filename, "w") as f:
        for out in data:
            if out not in remove:
                f.write(out)

def open_file(path: str):
    filename = os.path.expanduser(path)
    if os.path.exists(filename):
        with open(filename, "r+") as f:
            return f.readlines()
    sys.exit(f"{filename}: No such file or directory")

def main():
    info = "Usage: cutl [list] [line] [output]\ncutl - take N lines from a file list and automatically trim them from the source"
    if len(sys.argv) <= 3:
        sys.exit(info)
    path, lines, destination = sys.argv[1], sys.argv[2], sys.argv[3]
    file = open_file(path)
    trim_object(file, lines, path, destination)

