import os, time


folder = '/home/emmanuel/Pictures/'

for f in os.listdir(folder):
    if f.startswith('emma'):
        print(time.ctime(os.path.getmtime(folder+f)))
        print(time.ctime(os.path.getatime(folder+f)))
        print(f)

