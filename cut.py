import argparse
import sys
import re
import io

parser = argparse.ArgumentParser(prog='cccut',
description='Print selected parts of lines from each FILE to standard output.',
epilog='Try cut --help for more information.')

# parser.add_argument('filename')
parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('-f','--flag')
parser.add_argument('-d','--spacer')

args = parser.parse_args()

def main():
    if(not args.flag):
        print("cut: you must specify a list of bytes, characters, or fields")
        print("Try 'cut --help' for more information.")
    else:
        path = args.file
        cols = []
        delim = ','
        spacer = '\t'
        try:
            data = args.file.read()
        except:
            print(f"cccut: {path} No file or directory")
            exit(1)
        if path.name.endswith('.tsv'):
            delim = '\t'
        data = data.split('\n')    
        try:
            cols = list(map(int,args.flag.split(",")))
        except:
            cols = list(map(int,args.flag.split(" ")))
        if(args.spacer):
            spacer = args.spacer
        else:
            spacer = "\t"
    
        for i in range(len(cols)):
            cols[i]-=1

        df = []
        for line in data:
            row = line.split(delim)
            df.append(row)

        for i in range(len(df)):
            for j in range(len(df[i])):
                if j in cols:
                    if(j==cols[len(cols)-1]):
                        print(df[i][j],end=" ")
                    else:
                        print(df[i][j],end=spacer)
            print()

        

if __name__ == "__main__":
    main()