import sys
import subprocess
import os
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pytube'])
import pytube

if not os.path.exists('songs'):
    os.makedirs('songs')
    
links  = ["https://www.youtube.com/watch?v=32GZ3suxRn4"]


for i in range(len(links)):
    pytube.YouTube(links[i]).streams.filter(only_audio=True).first().download("songs/")
    progress = round((i+1) / len(links) * 100)
    sys.stdout.write("Download progress: %d%%   \r" % (progress) )
    sys.stdout.flush()
    if i == len(links)-1:
        print()