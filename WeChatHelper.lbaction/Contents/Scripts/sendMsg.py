#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Vincent Duan
@contact: <vincent.duan95@outlook.com>
@file: sendMsg.py
@time: 08/27/18, 17:52
"""
import sys
import os
import subprocess as sp
import requests

# init
my_env = os.environ.copy()
items = []


for ag in sys.argv[1:]:
    # init
    userId = ""
    msgContent = ""
    baseUrl = 'http://127.0.0.1:52700/wechat-plugin/'

    if len(ag.split('/')) > 1:
        userId = ag.split('/')[0]
        msgContent = ag.split('/')[1]
    else:
        userId = ag

    if msgContent:
        url = baseUrl + 'send-message'
        data = {'userId': userId, 'content': msgContent}
    else:
        url = baseUrl + 'open-session'
        data = {'userId': userId}
        my_command = "open -a WeChat".split(' ')
        sp.call(my_command, env=my_env)
    req = requests.post(url=url, data=data)
