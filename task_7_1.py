'''
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

'''

import yaml

def mk_dir(dir_path):
    import os
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    else:
        print('directory already exists')

def main():
    
    base_dir = './my_project'
    mk_dir(base_dir)

    level1_dirs = ['settings', 'mainapp', 'adminapp', 'authapp']


    for d in level1_dirs:
        dir_path = base_dir + '/' + d
        mk_dir(dir_path)
        print(dir_path)

if __name__ == '__main__':
    main()