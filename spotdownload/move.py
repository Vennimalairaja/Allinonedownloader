import shutil
def move_file(file):
    try:
        shutil.move(f'/home/raja/Documents/allinonedownloader/{file}','/home/raja/Documents/allinonedownloader/static/Music')
        return True
    except Exception as e:
        return False
#print(move_file("G. V. Prakash, Yogi. B, Kaviyarasu Kannadasan, Yugabharathi, S. P. Balasubrahmanyam, Sunitha Sarathy - Engeyum Eppothum - From 'Polladhavan'.mp3"))