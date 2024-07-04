import requests
import streamlit as st

# 你的API金鑰
api_key = "CWA-02B2C065-5C62-4799-A27C-A48C3989F84D"
data_id="O-A0002-001"


base_url=f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/{data_id}?Authorization={api_key}&StationId=C0K400"#&RainfallElement=Past24hr"

print(base_url)

response = requests.get(base_url)

# 解析返回的JSON數據
data = response.json()

# 打印雨量資料

st.json(data)

st.write(data['records']['Station'][0]['RainfallElement']['Past24hr']['Precipitation'])

# print(data)
