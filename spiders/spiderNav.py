import requests
import csv
import numpy as np
import os

def init():
    if not os.path.exists('./navData.csv'):
        with open('./navData', 'w', encoding='utf-8', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([
                'typeName',
                'gid',
                'containerid'
            ])

def writerRow(row):
    if not os.path.exists('./navData.csv'):
        with open('./navData', 'a', encoding='utf-8', newline='') as csvFile:# 记得写入文件
            writer = csv.writer(csvFile)
            writer.writerow(row)

def get_data(url):
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

def parse_json(response):
    navList = np.append(response['groups'][3]['group'], response['groups'][4]['group'])
    # print(navList)
    for nav in navList:
        navName = nav['title']
        gid = nav['gid']
        containerid = nav['containerid']
        writerRow([
            navName,
            gid,
            containerid
        ])

if __name__ == "__main__":
    init()
    url = 'https://weibo.com/ajax/feed/allGroups'
    response = get_data(url)
    parse_json(response)