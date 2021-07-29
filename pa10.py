import requests

url="https://www.pearvideo.com/video_1736877"
contID=url.split("_")[1]
video_url=f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.9533524688816948"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
         "Referer": "https://www.pearvideo.com/video_1736877"#溯源，防盗链
         }
resp=requests.get(video_url,headers=headers)
dic=resp.json()
src=dic['videoInfo']['videos']['srcUrl']
systime=dic['systemTime']
src=src.replace(systime,f"cont-{contID}")
with open("img/a.mp4",mode='wb') as f:
    f.write(requests.get(src).content)
    print("over")

print(src)
# https://video.pearvideo.com/mp4/adshort/20210729/cont-1736877-15732719_adpkg-ad_hd.mp4
# https://video.pearvideo.com/mp4/adshort/20210729/1627559820983-15732719_adpkg-ad_hd.mp4
