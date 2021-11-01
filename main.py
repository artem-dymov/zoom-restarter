import psutil
import time


while True:

    try:
        flag = False
        p = psutil.pids()

        for i in p:
            if psutil.Process(i).name() == 'Zoom.exe':
                flag = True

        print(flag)

        time.sleep(10)

    except Exception:
        print("Error")
