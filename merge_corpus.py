#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File Name : merge_corpus.py
# @Purpose :
# @Creation Date : 2018-01-10 15:45:56
# @Last Modified : 2018-01-10 16:51:03
# @Created By :  chenjiang


import sys
reload(sys)
sys.setdefaultencoding('utf8')


def corpus_merge(f_in):
    word_dict = dict()
    with open(f_in, 'r') as reader:
        for line in reader:
            line = line.strip()
            if not line:
                continue
            li = line.split('\t')
            if len(li) < 2: continue
            word = li[0]
            weight = int(li[1])
            word_dict[word] = word_dict.get(word, 0) + weight
    sorted_word_dict = sorted(word_dict.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
    for (ww, we) in sorted_word_dict:
        msg = '%s\t%s' % (ww, we)
        print msg


if __name__ == '__main__':
    f_in = sys.argv[1]
    corpus_merge(f_in)
