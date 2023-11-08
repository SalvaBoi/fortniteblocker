import os
import psutil
import signal
import datetime

# Setting two targets which are steam (GTA) and Epic Games (Fortnite)
target_one = 'steam.exe'
target_two = 'EpicGamesLauncher.exe'
running = True

def reporter():
    f = open("GOTCHA.txt", "a")
    f.write(str(datetime.datetime.now()) + '\n')
    f.close()

# Making the program never stop if running
while running:
    for proc in psutil.process_iter(attrs=['pid', 'name']):         # process iteration
            if target_one in proc.info['name']:
                reporter()
                try:
                    os.kill(proc.info['pid'], signal.SIGILL)                # Killing steam if he admin bypass, pc will close
                except PermissionError:
                    os.system('shutdown -s -t 0')
            elif target_two in proc.info['name']:
                reporter()
                try:
                    os.kill(proc.info['pid'], signal.SIGILL)                # Killing epic if he admin bypass, pc will close
                except PermissionError:
                    os.system('shutdown -s -t 0')
            else:
                pass

