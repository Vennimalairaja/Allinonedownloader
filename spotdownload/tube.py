import yt_dlp
import os
def yt_download(url,category='video'):
    ydl_opts={'outtmpl':'%(title)s.mp4'}
    extension='mp4'
    if category=='audio':
        ydl_opts['extract_audio']=True
        ydl_opts['outtmpl']='%(title)s.mp3'
        ydl_opts['format']='bestaudio'
        extension='mp3'
    try:
        file=''
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
        for i in os.listdir('/home/raja/Documents/allinonedownloader'):
            if i[-3:]==extension:
                file=i
                break
        return file
    except Exception as e:
        return False

#download_audio('https://youtu.be/yvOh7vVqlaE?si=2iSSp0NuifB7746Q')
#print(yt_download('https://youtu.be/YyV2k8Almuk?si=i4_BFyZ0SrEwTZM_',audio=True))