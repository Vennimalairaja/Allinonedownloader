import subprocess
import os
import shutil
def spot_download(url):
    try:
        result=subprocess.run(['spotdl',url],capture_output=True,text=True,check=True)
        file=''
        for i in os.listdir('/home/raja/Documents/allinonedownloader'):
            if i[-3:]=='mp3':
                file=i
                break
        #shutil.move(f'/home/raja/Documents/allinonedownloader/{file}','/home/raja/Documents/allinonedownloader/static/Music')
        return file 
    except Exception as e:
        return False

#print(spot_download('https://open.spotify.com/track/2pUpNOgJBIBCcjyQZQ00qU?si=8a35de59a5ed435b'))
