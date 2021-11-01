import psutil

flag = False

p = psutil.pids()

for i in p:
    if psutil.Process(i).name() == 'Zoom.exe':
        flag = True

print(flag)