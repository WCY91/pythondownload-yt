from pytube import Playlist 
import os

#挑選影片清晰度
def chooseRes(p,mode,path = os.getcwd()):
    print("loading...")
    if mode == 2:
        for video in p.videos: #p.videos會回傳由Youtube物件構成的陣列
            video.streams.get_by_itag("18").download(path) # 清晰度 360p
    elif mode == 1:
        for video in p.videos:
            video.streams.get_by_itag("22").download(path) # 清晰度 720p

# 下載播放清單
def install(p,resolution,path = os.getcwd()): 
    print('Number of videos in playlist: %s' % len(p.video_urls))
    chooseRes(p,resolution,path)
    print("finish!")
    return len(p.video_urls)


def download_playlist(url,resolution,path = os.getcwd()): # 清晰度 (1)360p (2)720p    
    if path=='':
        path = os.getcwd()
    p = Playlist(url) # 建立playlist物件
    num = install(p,resolution,path)
    return num



if __name__ == '__main__':
    url = str(input("請輸入清單網址\n>> "))
    resolution=int(input('請挑選欲下載的清晰度 (1)720p (2)360p  \n>> '))
    download_playlist(url,resolution)