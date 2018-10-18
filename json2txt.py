#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File Name : json2txt.py
# @Purpose :
# @Creation Date : 2018-09-20 10:22:00
# @Last Modified : 2018-09-27 15:36:46
# @Created By :  chenjiang
# @Modified By :  chenjiang


from os import sys, path
reload(sys)
sys.setdefaultencoding('utf8')

import json


def json2txt(fin, fout):
    outer = open(fout, 'w')
    with open(fin, 'r') as reader:
        for line in reader:
            doc = json.loads(line.strip())
            title = doc['title'].strip()
            play_count = int(doc['play_count'])
            if play_count == 0:
                play_count = 1
            msg = '%s\t%s\n' % (title, play_count)
            outer.write(msg)
    outer.close()


if __name__ == '__main__':
    fin = sys.argv[1]
    fout = sys.argv[2]
    json2txt(fin, fout)





