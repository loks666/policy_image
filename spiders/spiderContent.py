import requests
import csv
import numpy as np
import os
import time
from datetime import datetime

def init():
    if not os.path.exists('./articleData.csv'):
        with open('./articleData', 'w', encoding='utf-8', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([#写入的writerow参数，需要重新改
                'id',
                'likeNum',
                'commentsLen',
                'reposts_count',
                'region',
                'content',
                'contentLen',
                'created_at',
                'type',
                'detailUrl',# followBtnCode>uid t mblogid
                'authorAvatar',
                'authorName',
                'authorDetail',
                'isVip'  # v_plus
                # 'attitudes_count',
                # 'source',
                # 'textLength',
                # 'text_raw',
                # 'id',
                # 'idstr'
            ])

def writerRow(row):
    if not os.path.exists('./articleData.csv'):
        with open('./articleData', 'a', encoding='utf-8', newline='') as csvFile:# 记得写入文件
            writer = csv.writer(csvFile)
            writer.writerow(row)

def get_data(url, params):
    headers ={
        'Cookie': 'XSRF-TOKEN=y6rt3qs92v6mAhqws-7Zeksy; SUB=_2AkMRexBAf8NxqwFRmfsRy2_ha49zzwzEieKnJ-GbJRMxHRl-yT9kqk8dtRB6Ovs-r4IzzvEH1iRNuz0__OhilubE31oU; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhvoxsGmuxOY3O2Gc.oO_6d; WBPSESS=gJ7ElPMf_3q2cdj5JUfmvJt2D0Ue2VcdkylWpNF5P6c6y8xBYL1YH1Il5VVUKISp9oKo1KfX8v0K-BikOacwPJk0_EpaDzsnss9EjC6iRSQZs0tjRE2x2HNjW6ZUOJj5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    params = {
        'is_new_segment': 1,
        'fetch_hot': 1
    }
    response = requests.get(url, headers=headers, params=params)
    # print(response.json())
    if response.status_code == 200:
        return response.json()
    else:
        return None

def getAllTypeList():
    typelist = []
    with open('./navData', 'r', encoding='utf-8', newline='') as reader:
        readerCsv = csv.reader(reader)
        next(reader)
        for nav in readerCsv:
            typelist.append(nav)
    return typelist

def parse_json(response):
    print(response)

def start(typeNum = 3, pageNum = 2):
    articleUrl = 'https://weibo.com/ajax/feed/hottimeline'
    init()
    typelist = getAllTypeList()
    # print(typelist)

    typeNumCount = 0
    for type in typelist:
        if typeNumCount > typeNum: return
        for page in range(0, pageNum):
            print('正在爬取的类型：%s 中的第%s页文章数据' %(type[0], page + 1))
            params = {
                'group_id':type[1],
                'containerid':type[2],
                'max_id':page,
                'count':10,
                'extparam':'discover|new_feed'
            }
            response = get_data(articleUrl, params)
            parse_json(response)
            break
        break

if __name__ == "__main__":
    start()