import sys
import os
import argparse

def GetFromPrefix(path, prefix):
    entries = os.listdir(path)
    output = []
    for entry in entries:
        if entry.startswith(prefix):
            output.append(path + entry)
    return output

def GetFromPrefixes(path, prefixes):
    outputs = []
    for prefix in prefixes:
        output = GetFromPrefix(path, prefix)
        outputs.append(output)
    return outputs

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    parser.add_argument('prefixes', type=str, nargs='+')
    args = parser.parse_args()

    outputs = GetFromPrefixes(args.path, args.prefixes)
    for output in outputs:
        for name in output:
            print(name)
        print("\n")



