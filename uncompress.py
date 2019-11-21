from __future__ import print_function
import os

from collections import defaultdict
from unrar import rarfile
from zipfile import ZipFile
import json

public_data_path = '/Users/andrew/Desktop/andrewli/dzy/dzymap/data/'
url_base = 'http://localhost:5001/data/'
def uncompress_task_manager(path, name):
    res_name = name
    print('task_manager')
    #print(path[-4:]) 
    new_name = str(hash(name))
    if path[-4:] == '.zip':
        unzip_(path, name)
    if path[-4:] == '.rar':
        unrar_(path, name)
    
    dir = os.path.join(public_data_path, new_name)
    os.rename(os.path.join(public_data_path, name), os.path.join(public_data_path, new_name))
    #print(dir)
    res_path = dbf2json(dir)

    print(os.path.join((url_base+new_name+'/'), res_path))

    res_path = os.path.join((url_base+new_name+'/'), res_path)
    return res_name, res_path
    

    
    

def unrar_(path, name):
    rar = rarfile.RarFile(path)
    rar.extractall(public_data_path)

def unzip_(path, name):
    #print('zip')
    zf = ZipFile(path, 'r')
    print(zf.namelist()[0])
    zf.extractall(public_data_path)
    os.rename(os.path.join(public_data_path,zf.namelist()[0]), os.path.join(public_data_path, name))

def dbf2json(dir):
    dbf_file = ''
    
    for file in os.listdir(dir):
        if file.endswith(".dbf"):
            #print(os.path.join(dir, file))
            dbf_file = os.path.join(dir, file)
            res_file=file
    
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

    return res_file.replace('dbf','shp')