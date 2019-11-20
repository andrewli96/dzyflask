from __future__ import print_function
import os

from collections import defaultdict
from unrar import rarfile
from zipfile import ZipFile
import json

new_path = ''

def uncompress_task_manager(path, name):
    print('task_manager')
    print(path[-4:]) 
    dir = os.path.join(new_path,name)
    if path[-4:] == '.zip':
        unzip_(path, name)
        dbf2json(dir)
    if path[-4:] == '.rar':
        unrar_(path, name)

def unrar_(path, name):
    rar = rarfile.RarFile(path)
    rar.namelist()

def unzip_(path, name):
    print('zip')
    zf = ZipFile(path, 'r')
    zf.extractall(new_path)

def dbf2json(dir):
    dbf_file = ''

    
    for file in os.listdir(dir):
        if file.endswith(".dbf"):
            print(os.path.join(dir, file))
            dbf_file = os.path.join(dir, file)
    
    f1 = open(dbf_file.replace('dbf','json'), 'w')
    
    x = []

    from dbfread import DBF 
    for record in DBF(dbf_file, encoding='utf-8'):
        x.append(record)

    dbf = {}
    for xx in x:
        temp = {}
        for key, value in xx.items():
            temp[key]=value
        dbf[xx[u'OBJECTID']]=temp
    json.dump(dbf,f1,ensure_ascii=False)