import sys

def read_files(f_users, f_hobby):
    with open(f_users) as f1, open(f_hobby) as f2: 
        while True: 
            line1 = f1.readline() 
            line2 = f2.readline() 
            if line1: 
                yield line1, line2 
            else: 
                return

def extract_data(line):
    usr_info = {}

    a,b,c = line[0].strip('\n').split(',')
    usr_info['Фамилия'] = a
    usr_info['Имя'] = b
    usr_info['Отчество'] = c

    for i, h in enumerate(line[1].strip('\n').split(',')):
        key = 'Хобби '+str(i+1)
        usr_info[key] = h

    return usr_info

def save_output(f_output, usrs_info):
    import json
    with open(f_output, 'w', encoding='UTF-8') as fp:
        json.dump(usrs_info, fp, ensure_ascii=False)

def main(arguments):
    # count = len(arguments)
    # f_users = arguments[0]
    # f_hobby = arguments[1]
    # f_output = arguments[2]
    f_users = 'users.csv'
    f_hobby = 'hobby.csv'
    f_output = 'output.json'
    usrs_info = {}

    for i,line in enumerate(read_files(f_users, f_hobby)):
        usr_info = extract_data(line)
        key = 'Пользователь '+str(i+1)
        usrs_info[key] = usr_info
        # print(usrs_info)

    save_output(f_output, usrs_info)
    z = 1

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
