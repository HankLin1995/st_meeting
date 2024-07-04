import requests
import json
import streamlit as st
from datetime import datetime
import pandas as pd

def format_date(timestamp):
        return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")

@st.cache_data
def getOriginData():

    url = 'https://script.google.com/macros/s/AKfycbz6CWS_HnAATXAMwJBJhIELbAoWsgcYJFkNxpgldA96m1SkWVeEgy4l1EyXeyW60gmK/exec'

    #    发送GET请求
    response = requests.get(url)

    # 检查响应状态
    if response.status_code == 200:
        # 解析JSON数据
        data = json.loads(response.text)
        
        # 处理数据
        headers = data[0]  # 标题行
        records = data[1:]  # 数据行
        

        desired_headers = [
        "id",
        "inf.work_place2",
        "inf.work_place_detail",
        "inf.work_place_water",
        "inf.work_station",
        "inf.work_name",
        "inf.work_start_date",
        "inf.work_end_date",
        "inf.job_length",
        "inf.job_cost",
        "coords.2.lat",
        "coords.2.lon", 
        ]

        # mycolumns = ['安排','編號','工作站','水路名稱','施工期起','施工期終','水路長度','概估經費','位置N','位置E']
        
        # 找到需要的表头的索引
        indices = [headers.index(header) for header in desired_headers]
        
        filtered_records = []
        for record in records:
            filtered_record = {'meeting':False}
            for header, index in zip(desired_headers, indices):
                if header in ["inf.work_start_date", "inf.work_end_date"]:
                    filtered_record[header] = format_date(record[index])
                else:
                    filtered_record[header] = record[index]
            filtered_records.append(filtered_record)

        return pd.DataFrame(filtered_records)#,columns=mycolumns)


    else:
        print(f"Failed to retrieve data: {response.status_code}")
