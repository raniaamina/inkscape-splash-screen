#!/usr/bin/env python3
import subprocess
import time

application = "inkscape"
path = "/opt/Inksplash/init.py"

subprocess.Popen([application])
subprocess.Popen(["python", path])

while True:
    time.sleep(0.5)
    try:
        pid = subprocess.check_output(["pidof", application]).decode("utf-8").strip()
        w_list = subprocess.check_output(["wmctrl", "-lp"]).decode("utf-8")
        if pid in w_list:
            splashpid = [l.split()[2] for l in w_list.splitlines()\
                         if "inkscape-splash" in l][0]
            subprocess.Popen(["kill", splashpid])
            break
    except subprocess.CalledProcessError:
        pass	

