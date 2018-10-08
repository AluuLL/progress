#!/usr/bin/python
#-*-coding:UTF-8 -*-

import sys
import re
import json

def myfunc(dictfile,infile,outfile):
	out = open(outfile,'w')
	with open(dictfile,'r') as reader:
		dict_list = []
		for line in reader:
			line = line.strip()
			dict_list.append(line)
	dict_list = json.dumps(dict_list,encoding="utf8",ensure_ascii=False)
	#print dict_list
	with open(infile,'r') as inputfile:
		for line in inputfile:
			line = line.strip()
			en_list = re.findall(r"[a-zA-Z]+",line)
			for word in en_list:
				if word.lower() not in dict_list:
					outwrite(word.lower()+"\n")
        out.close()

if __name__=='__main__':
	dictfile = sys.argv[1]
	inputfile = sys.argv[2]
	outfile = sys.argv[3]
	myfunc(dictfile,inputfile,outfile)
