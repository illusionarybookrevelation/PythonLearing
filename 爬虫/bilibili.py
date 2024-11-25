import requests
from bs4 import BeautifulSoup
import json

# 视频的 BV 号
bv_id = "BV1Uk4y1Z7Xo"
url = f"https://www.bilibili.com/video/{bv_id}"

# 发送请求
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
response = requests.get(url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 解析网页
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取视频标题
    title = soup.find('h1').text.strip()
    print(f"视频标题: {title}")

    # 提取播放量
    stats = soup.find('div', class_='view')
    if stats:
        play_count = stats.text.strip()
        print(f"播放量: {play_count}")

    # 如果需要获取更详细的信息（如评论、弹幕等），可以进一步解析
else:
    print(f"请求失败，状态码: {response.status_code}")
