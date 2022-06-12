'''
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); 
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; 
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
2.* (вместо 1)Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
'''

# !/usr/bin/env python

import os
import sys
import yaml


def dict_to_dir(data, path=str()):

    dest = os.path.join(os.getcwd(), path)

    if isinstance(data, dict):
        for k, v in data.items():
            os.makedirs(os.path.join(dest, k))
            dict_to_dir(v, os.path.join(path, str(k)))

    elif isinstance(data, list):
        for i in data:
            if isinstance(i, dict):
                dict_to_dir(i, path)
            else:
                with open(os.path.join(dest, i), "a"):
                    os.utime(os.path.join(dest, i), None)

    if isinstance(data, dict):
        return list(data.keys())[0]

try:
    y = './config.yaml'
    p = './'
    with open(y, "r") as f:
        try:
            d = yaml.load(f)
            dest = dict_to_dir(data=d, path=p)
            print("Directory created at {}".format(p if p else os.path.join(os.getcwd(), dest)))
        except Exception as e:
            print(e)
except Exception as e:
    print(e)