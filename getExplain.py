#! /usr/bin/env python -tt
# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import sys
import commands
import os
import pandas as p

def ProcessCONTENTS(contents):
    soup = BeautifulSoup(contents, 'lxml')
    explain = ''
    for tag in soup.find_all('div', class_='section blurb'):
        explain = tag.get_text().encode('utf-8')    
    if explain == '':
        explain = 'no explain'
    return explain