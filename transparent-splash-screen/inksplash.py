#!/usr/bin/env python3
import sys
import shlex, subprocess
import time

application = "inkscape"
path = "/opt/Inksplash/init.py"
a = (len(sys.argv))

subprocess.Popen(["python2", path])
if a > 1:
	for i in range(1,a):
		subprocess.Popen([application, str(sys.argv[i])])
else:
	subprocess.Popen([application])


while True:
    time.sleep(0.5)
    try:
        pid = "Inkscape"
        w_list = subprocess.check_output(["wmctrl", "-lp"]).decode("utf-8")
        if pid in w_list:
            splashpid = [l.split()[2] for l in w_list.splitlines()\
                         if "inkscape-splash" in l][0]
            subprocess.Popen(["kill", splashpid])
            break
    except subprocess.CalledProcessError:
        pass	

