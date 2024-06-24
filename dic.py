from datetime import datetime, timedelta

def generate_itinerary(data, start_time_str):
    # 將開始時間字串轉換為 datetime 物件
    start_time = datetime.strptime(start_time_str, '%H:%M')
    itinerary = []

    for i, entry in enumerate(data):
        # 如果不是第一個水路，先加入移動時間
        if i > 0:
            move_start_time = start_time
            move_end_time = move_start_time + timedelta(minutes=entry['移動時間'])
            itinerary.append([f"{move_start_time.strftime('%H:%M')}~{move_end_time.strftime('%H:%M')}", '移動時間'])
            start_time = move_end_time

        # 生成水路名稱的行程
        waterway_start_time = start_time
        waterway_end_time = waterway_start_time + timedelta(minutes=entry['停留時間'])
        itinerary.append([f"{waterway_start_time.strftime('%H:%M')}~{waterway_end_time.strftime('%H:%M')}", entry['水路名稱']])

        # 更新開始時間為水路停留結束時間
        start_time = waterway_end_time

    return itinerary
# 測試資料
data = [
    {'序號': 1, '水路名稱': '丘厝小排2-4', '經度': 120.2037, '緯度': 23.6724, '停留時間': 20.0, '移動時間': 0.0, '計算時間': 0.0},
    {'序號': 2, '水路名稱': '牛厝中排1', '經度': 120.2066, '緯度': 23.6667, '停留時間': 20.0, '移動時間': 5.0, ' 計算時間': 1.6849999999999998},
    {'序號': 3, '水路名稱': 'AAA', '經度': 120.261669, '緯度': 23.662764, '停留時間': 20.0, '移動時間': 10.0, '計算時間': 8.203333333333333},
    {'序號': 4, '水路名稱': '路利潭中排一', '經度': 120.2368, '緯度': 23.7008, '停留時間': 20.0, '移動時間': 10.0, '計算時間': 7.4366666666666665},
    {'序號': 5, '水路名稱': '北月眉小排2-1', '經度': 120.286, '緯度': 23.6901, '停留時間': 20.0, '移動時間': 15.0, '計算時間': 10.276666666666667}
]

print (data)

# 給定開始時間
start_time_str = "10:30"

# 生成行程表
itinerary = generate_itinerary(data, start_time_str)

# 輸出行程表
for item in itinerary:
    print(item)