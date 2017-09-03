#! /usr/bin/env python -tt
# -*- coding:utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import sys
import os
from selenium import webdriver
import commands


def getExample(URL,WORD):
    phantomjs_path = u"/Users/JawieZhu/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs"
        
    file_path = 'dictionary/'+WORD+'_example'
    if os.path.exists(file_path):
        contents_file = commands.getoutput('cat '+file_path)
        print contents_file
        return 
    else:
        
        driver = webdriver.PhantomJS(executable_path=phantomjs_path)
        driver.get(URL)

    #html1 = driver.page_source

    #print html1

    #html2 = driver.execute_script("return document.documentElement.innerHTML;")
    

        for i in range(0,4):
            next = driver.find_element_by_xpath("//a[@class='next ss-navigateright right']")
            next.click()
       # i = i + 1    
        
        example = driver.find_element_by_xpath("//div[@class='section examples']")
        example = example.get_attribute('innerHTML') 

    #print example 

    
        FILE = open(file_path, 'w+')
        #FILE.write(contents)
        #print contents
        #FILE.close() 

        soup = BeautifulSoup(example,'lxml')
        cnt = 1
        for tag in soup.find_all('li'):
            example = tag.find('div',class_='sentence').get_text().encode('utf-8')
            source = tag.find('span',class_='corpus').get_text().encode('utf-8')
            #url = None
            tmp = tag.find('a',class_='source',href=True)
            if tmp is not None:
                url = tmp['href']
            else:
                url = 'no source'
            date = tag.find('span',class_='date').get_text().encode('utf-8')
            
            FILE.write( str(cnt) + '  ' +example )
            FILE.write('\n')
            FILE.write( source + '\t' +'['+ url +']' + '\t' + date) 
            FILE.write('\n')
            cnt = cnt + 1
            #print url
            #print date
            if example == '':
                example = 'no example'

        
        FILE.close()
        return