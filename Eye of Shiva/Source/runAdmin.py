import ctypes, sys
import subprocess
import os


def is_admin(): # request run as admin
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    inicialize = subprocess.Popen("python interface_v3.py", shell=False)
    with open(".\\pid.txt", "w") as pid:
        inicialize_id = inicialize.pid
        pid.write(str(inicialize_id))
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

