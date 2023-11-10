
import os
import psutil
import signal
import datetime

# Setting two targets which are steam (GTA) and Epic Games (Fortnite)
targets = ['steam.exe','EpicGamesLauncher.exe']
running = True

def reporter():
    f = open("GOTCHA.txt", "a")
    f.write(str(datetime.datetime.now()) + '\n')
    f.close()

# Making the program never stop if running
while running:
    for proc in psutil.process_iter(attrs=['pid', 'name']):         # process iteration of each element in targets
        for targ in targets: 
            if targ in proc.info['name']:
                reporter()
                try:
                    os.kill(proc.info['pid'], signal.SIGILL)                # Killing targ if he admin bypass, pc will close
                except PermissionError:
                    os.system('shutdown -s -t 0')
            
