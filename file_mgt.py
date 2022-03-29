import os, time

folder = '/home/emmanuel/Pictures'

for f in os.listdir(folder):
    if f.startswith('Screenshot'):
        #print(time.ctime(os.path.getatime(f)))
        print(time.ctime(os.path.getctime(f)))