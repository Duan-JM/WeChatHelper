#!/usr/local/bin/python3
import sys
import json
import os
import requests
import search

items = []
for ag in sys.argv[1:]:
    # item = {}
    # init
    userId = ""
    msgContent = ""

    if len(ag.split('/')) > 1:
        userId = ag.split('/')[0]
        msgContent = ag.split('/')[1]
    else:
        userId = ag
    baseUrl = 'http://127.0.0.1:52700/wechat-plugin/'
    if msgContent:
        url = baseUrl + 'send-message'
        data = {'userId': userId, 'content': msgContent}
    else:
        url = baseUrl + 'open-session'
        data = {'userId': userId}
    req = requests.post(url=url, data=data)


#baseUrl = os.getenv('baseUrl')
    #userId = sys.argv[1]
    #url = baseUrl + 'open-session'
    #data = {'userId': userId}
    #r = web.post(url=url,data=data)

#import sys,os
#import requests

#msgContent = 'testFromMyScript'
#userId = 'wxid_xu27mjox3lcs12'
#baseUrl = 'http://127.0.0.1:52700/wechat-plugin/'
#url = baseUrl + 'send-message'
#data = {'userId':userId, 'content': msgContent}
#r = requests.post(url=url,data=data)
# r.raise_for_status()
