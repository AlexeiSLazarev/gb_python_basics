def main(arguments):
    f_db = 'db.txt'
    with open(f_db, 'a') as f: 
        f.writelines(arguments[0]+'\n')

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])