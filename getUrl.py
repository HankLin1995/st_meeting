import requests

def generate_google_maps_link(latitude, longitude):
    base_url = "https://www.google.com/maps/place/"
    return f"{base_url}{latitude},{longitude}"

def shorten_url(long_url, access_token):
    url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "long_url": long_url
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("link")
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None

# 替换为你的Bitly API访问令牌
BITLY_ACCESS_TOKEN = 'YOUR_BITLY_ACCESS_TOKEN'

# 斗六的坐标
latitude_douliou = 23.6901
longitude_douliou = 120.286

# 生成Google Maps的长链接
google_maps_link = generate_google_maps_link(latitude_douliou, longitude_douliou)
print(f"Google Maps Link: {google_maps_link}")

# 生成短链接
short_link = shorten_url(google_maps_link, BITLY_ACCESS_TOKEN)
print(f"Short Link: {short_link}")
