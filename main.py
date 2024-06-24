import openrouteservice

# 替换为你的OpenRouteService API密钥
API_KEY = '5b3ce3597851110001cf6248fa6ab9549f3740f3bc50db83029c37a1'

# 初始化OpenRouteService客户端
client = openrouteservice.Client(key=API_KEY)

# 定义斗六和斗南的经纬度坐标
coordinates = [[120.286, 23.6901], [120.2368, 23.7008]]

# 请求路由信息
routes = client.directions(coordinates, profile='driving-car')

# 提取并打印距离和时间信息
if routes and 'routes' in routes and routes['routes']:
    route = routes['routes'][0]
    distance = route['summary']['distance'] / 1000  # 转换为公里
    duration = route['summary']['duration'] / 60  # 转换为小时

    print(f"Distance: {distance:.2f} km")
    print(f"Duration: {duration:.2f} mins")
else:
    print("Error with the request or no routes found.")

