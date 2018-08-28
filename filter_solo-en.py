#! /usr/bin/python
#-*- coding: UTF-8 -*-
import sys
import re
##使用方法：python filter_solo-en.py inputfile outputfile
##功能介绍：现将英文资源是单词的权重降低到10；也可以更改下，使得是单词的资源不出现；
##需注意：inputfile：第一列是资源，第二列是权值；

def myfunc(infile,outfile):
	out = open(outfile,'w')
	out1 = open(infile+"en.list",'w')
	with open (infile,'r')as reader:
		for line in reader:
			line_list = line.strip().split('\t')
			word_list =str(line_list[0]).strip().split(' ')
			if len(word_list)!=1:
				#print line_list
				out.write('\t'.join(line_list)+"\n")
			else:
				#pass
				en=re.search('^[a-zA-Z]+$',str(line_list[0]))
				#print en
				if not (en):
					out.write('\t'.join(line_list)+"\n")
				if en:
					#line_list[1]=str(10)
					out1.write('\t'.join(line_list)+"\n")
	out.close()
	out1.close()
if __name__ =='__main__':
	infile = sys.argv[1]
	outfile = sys.argv[2]
	myfunc(infile,outfile)
