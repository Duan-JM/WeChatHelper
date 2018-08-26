#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Vincent Duan
@contact: <vincent.duan95@outlook.com>
@file: search.py
@time: 08/26/18, 21:44
"""
import sys
import json
import os
import requests

# set def


def CreateItem(title="", subtitle="", label="", icon="", action="", actionParam=""):
    """
    This function is to create item
    :title<string>
    :subtitle<string>
    :lable<string>
    :icon<string>
    :action<string>
    :actionParam<string>
    :return item<dict>
    """
    item = {}
    item['title'] = title
    item['subtitle'] = subtitle
    item['lable'] = label
    item['icon'] = icon
    item['action'] = action
    item['actionArgument'] = actionParam
    return item


# init
items = []
for query in sys.argv[1:]:
    baseUrl = 'http://127.0.0.1:52700/wechat-plugin/'
    url = baseUrl + 'user?keyword=' + query.split('/')[0]
    item = {}
    result = requests.get(url=url)
    result.encoding = 'utf-8'
    resp = result.text
    userList = json.loads(resp)

    for user in userList:
        # init param
        title = ""
        subtitle = ""
        icon = ""
        action = "sendMsg.py"
        actionArgument = ""
        displayMessage = ""
        item = {}

        # get the param
        title = user['title']
        subtitle = user['subTitle']
        if user['title'][0] == '[':
            icon = 'font-awesome:fa-group'
        else:
            icon = 'font-awesome:fa-address-book'
        if len(query.split('/')) > 1:
            actionArgument = user['userId']+'/'+query.split('/')[1]
            displayMessage = query.split('/')[1]
        else:
            actionArgument = user['userId']
        # generate Item
        item = \
            CreateItem(title=title, subtitle=subtitle, icon=icon,
                       action=action, actionParam=actionArgument)
        items.append(item)
        if displayMessage:
            item = {}
            item = CreateItem(title=displayMessage,
                              icon="font-awesome:fa-comment", subtitle="信息内容")
            items.append(item)

print(json.dumps(items))
