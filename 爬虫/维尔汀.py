import requests
from moviepy.editor import VideoFileClip

# Bilibili视频的BV号
bv_id = "BV1Uk4y1Z7Xo"

# 构造Bilibili视频的下载链接
video_url = f"https://www.bilibili.com/video/{bv_id}"

# 使用requests获取视频内容
response = requests.get(video_url)
video_content = response.content

# 保存视频内容到文件
with open("video.mp4", "wb") as f:
    f.write(video_content)

# 使用moviepy提取音频
clip = VideoFileClip("video.mp4")
clip.audio.write_audiofile("audio.mp3")

# 删除临时视频文件
import os
os.remove("video.mp4")

print("音频提取完成，保存为audio.mp3")