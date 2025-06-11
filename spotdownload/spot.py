import subprocess
def spot_download(url):
    try:
        result=subprocess.run(['spotdl',url],capture_output=True,text=True,check=True)
        return True
    except Exception as e:
        return False
#print(spot_download('https://open.spotify.com/track/0nrJ7jsUFR0pDHV6NvKJje?si=b10c9df40de54fd3'))