# -*- coding: utf-8 -*-

""" 
Данный скрипт предназначен для парсинга логов. Предполагаем что все логи имеют формат *.gz

Задача:
Нужно собрать статистику получения предмета 1101 из файла "items_full.log.gz":
1.  выбрать только записи с поступлением предметов,
2.  сгруппировать по типу действия и дате,
3.  посчитать количество поступлений в каждой группе.
Можно использовать инструменты окружения (grep, gzip и т.д.)

"""

import os, gzip

def ungzip_logs(os):
    print "Ungzip log files"
    for file in os.listdir(os.getcwd()):
        print "File:", file
        with gzip.open(file, 'rb') as gz:
           file_content = gz.read()
           with open(file[:-3], "w") as out:
                #for line in file_content:
                out.writelines(file_content)
           analize_content(file[:-3])
        os.remove(file[:-3])

def analize_content(file_content):
    info = {}
    with open(file_content, 'r') as data:
        for line in data:
            if 'itemID=1101' in line:
                if (('collection_compile' in line) or ('decor_click' in line) or ('gift_from' in line) or 
                   ('item_buy' in line) or ('item_use' in line) or ('quest_complete' in line)):
                    day = line.split("context=")[0].split(" ")[0]
                    arg = line.split("context=")[1].split(", ")[0][6:]
                    d = info.setdefault(day, {})
                    val = d.setdefault(arg, 0)
                    d[arg] = val + 1
                    info[day] = d
    print_info(info)

def print_info(info):
    for k, v in info.iteritems():
        print "[", k, "]"
        for key, value in v.iteritems():
            print '%-20s:%s' % (key, value)

if __name__ == '__main__':
    print "Start log parser"
    print "Work dir:", os.getcwd()
    if os.path.exists("logs"):
        os.chdir("logs")
        print "Current dir:", os.getcwd()
    ungzip_logs(os)
    print "Stop log parser"
