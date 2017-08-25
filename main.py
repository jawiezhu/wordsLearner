#! /usr/bin/env python -tt
# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import sys
import commands
import os
import pandas as pd
import getExplain



def getHtmlContents(url):
    HEADER = {'User-Agent':'Mozilla/5.0(Windows;U;Windows NT 6.1;en-US;rv:1.9.1.6) \
                Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url, headers=HEADER)
    page = urllib2.urlopen(req, timeout=60)
    contents = page.read()

    return contents

def writeToLocal(contents,WORD):
    file_path = 'dictionary/'+WORD+'_explanation'
    if os.path.exists(file_path):
        contents_file = commands.getoutput('cat '+file_path)
        print contents_file
    else:
        FILE = open(file_path, 'w+')
        FILE.write(contents)
        print contents
        FILE.close()

def main():
    if len(sys.argv) != 2:
        print 'usuage: python ./main.py {words you want to know}'
        sys.exit(1)

    WORD = sys.argv[1]
#    if WORD == 'checklocalfile':
#        WORDS_DF = pd.read_csv('/Users/JawieZhu/Desktop/words.csv')
#        print WORDS_DF 

    URL = 'https://www.vocabulary.com/dictionary/'+WORD
    CONTENTS = getHtmlContents(URL)
    EXPLAIN = getExplain.ProcessCONTENTS(CONTENTS)
    writeToLocal(EXPLAIN, WORD)

if __name__ == '__main__':
    main()
    