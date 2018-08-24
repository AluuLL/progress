#! /usr/bin/python
#-*- coding: UTF-8 -*-
import sys
import re
import json
##使用方法：python filter_ennotindict.py infile outfile
##功能介绍：infile每行资源中的英文单词有不在pplm.dict中的就删除整行资源，输出到outfile中；其中过滤出来的不符合条件的放到outfile.filted_notindict文件中
##需注意：inputfile：第一列是资源，第二列是权值；训练词典路径：/data/pengxy/env/pplm/pplm.dict_tofilter;即是带槽位的训练词典软链而成；

def myfunc(infile,outfile):
	out = open(outfile,'w')	#过滤后得到的符合条件的资源
	out_filter = open(outfile+".filted_notindict","w")	#过滤掉的不符合条件的资源
	with open("/data/pengxy/env/pplm/pplm.dict_tofilter","r") as dictfile:
		dict_list = []
		for line in dictfile:
			line = line.strip().decode('gbk')#完成全角/半角转换前需先进行编码转换
			line = strQ2B(line).encode('utf8')#完成转换后转换为utf8编码格式
			#print line
			line = re.sub(r'^[0-9]+\t','',line)
			dict_list.append(line)
		final_dictlist = json.dumps(dict_list,encoding="utf8",ensure_ascii=False)
		#print final_dictlist
	with open(infile,'r') as reader:
		for line in reader:
			line = line.strip()
			en_list = re.findall(r"([a-zA-Z]+)",line)
			#print en_list
			flag = 0 #用作表示该行中是否有不在词典中的英文单词，没有就是0；
			for word in en_list:
				if word.lower() not in final_dictlist:
					flag = 1
			if flag == 0:
				out.write(line+"\n")
			if flag == 1:
				out_filter.write(line+"\n")

##全角转半角
def strQ2B(ustring):
	rstring = ""
	for uchar in ustring:
		inside_code = ord(uchar)
		if inside_code == 12288:
			inside_code = 32
		elif (inside_code >= 65281 and inside_code <= 65374):
			inside_code -=65248
		rstring += unichr(inside_code)
		#print rstring
	return rstring

if __name__ =='__main__':
	infile = sys.argv[1]
	outfile = sys.argv[2]
	myfunc(infile,outfile)
