'''
3. Создать структуру файлов и папок, как написано в задании 2 
(при помощи скрипта или «руками» в проводнике). Написать скрипт, 
который собирает все шаблоны в одну папку templates, 
например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
'''

import os

os.chdir('./my_project')

import shutil
if os.path.isdir('./templates'):
    shutil.rmtree('./templates')

templates_dirs = []

def copy_templates(src):
    import shutil
    dst = './templates' + '/' + src.split('/')[-2:-1][0]
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

for root, dirs, subdirs in os.walk('./'):
    for d in dirs:
        p = os.path.join(root, d)
        z = p.find('templates')
        if p.find('templates') != -1:
            tmp_list = p.split('/')
            templates_dirs.append('/'.join(tmp_list[:tmp_list.index('templates')+1]))

templates_dirs = set(templates_dirs)
print(templates_dirs)

for src in templates_dirs:
    copy_templates(src)



