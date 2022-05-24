
from urllib3 import Retry


def read_file(path): 
    with open(path, 'rt') as f: 
        lines = f.readlines() 
    return lines
 

def main(arguments):
    f_db = 'db.txt'
    lines = read_file(f_db)
    if len(arguments) == 0:
        for l in lines:      
            print(l.strip('\n'))
        
    elif len(arguments) == 1:
        for i in range(int(arguments[0])):      
            print(lines[i].strip('\n'))

    elif len(arguments) == 2:
        for i in range(int(arguments[0]), int(arguments[1])):      
            print(lines[i].strip('\n'))

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])