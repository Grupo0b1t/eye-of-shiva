from ransomware_behave_db import evaluate
from PublicMalware_detection import PublicMalware_Detection
import os
import pathlib
import psutil
import time
import subprocess
import regex as re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import AddRegistry as registry

data_list = [] #keeps log of file system changes
users_list = [] #get machine's users
username = os.getlogin() #get username

change_type = [0, 0, 0, 0, 0]
#created_files = 0 #count file system changes
#modified_files = 1 #count file system changes
#moved_files = 2 #count file system changes
#deleted_files = 3 #count file system changes 
#trapfiles_edited = 4 #count file system changes

last3minutes_processes = [] #stores processes created on the last 3 minutes

time_since_last_change = 100
last_shadow_backup = 0

#--------------------------------------------------------------------------------------------------------

def kill_proc_tree(): #kills process tree, parent and child processes
    
    global last3minutes_processes
    print("possible ransomware detected")

    pids = ""
    for pid in reversed(last3minutes_processes):
        if pid != os.getpid():
            pids += f"/PID {pid} "
    subprocess.run(f"taskkill {pids}/F /T", shell=True)
    last3minutes_processes.clear()

#--------------------------------------------------------------------------------------------------------

def extract_extensions(file: str):
    extensions = [".exe", ".dll"]
    file_extension = pathlib.Path(file).suffix
    if file_extension.lower() in extensions:
        return True
    else:
        return False

#--------------------------------------------------------------------------------------------------------

def start_protection(): #creates a folder that is going to be used as backup and gets machine's users

    global users_list
    global username
    procname = psutil.Process(os.getpid()).name()
    subprocess.run(f'wmic process where name="{procname}" CALL setpriority "above normal"', shell=True)
    subprocess.run("mkdir protected_backup", shell=True) #creating protected_folder
    subprocess.run("takeown /F C:\Windows\System32\\vssadmin.exe", shell=True)
    subprocess.run(f'icacls C:\Windows\System32\\vssadmin.exe /grant "{username}":F', shell=True)
    subprocess.run("ren C:\Windows\System32\\vssadmin.exe adminvss.exe", shell=True)
    get_users = subprocess.run("wmic useraccount get name", capture_output=True, shell=True) #getting machine's users
    users = get_users.stdout.decode()
    users = re.split("/W|Name|\r|\n", users)

    for user in list(users):

        user = user.strip()

        if user == '':
            pass
            
        else:
            users_list.append(user)


def trap_create(): #creates honeypot files

    for x in range(1, 100):
        with open(f"_trapfile{x}.txt", "w") as file:
            file.write("trap file for ransomware detection")
            os.system(f"attrib +h _trapfile{x}.txt")

        file.close()


def securing_files(folder): #forbid all users from accessing folder

    global users_list

    for user in users_list:

        subprocess.run(f'icacls "{folder}" /deny "{user}":R', shell=True) #removing all users's permissions from folder


def unlocking_files(folder): #allow users to accessing folder

    global users_list

    for user in users_list:

        subprocess.run(f'icacls "{folder}" /grant "{user}":R', shell=True) #giving all users's permissions from folder


def shadow_copy(): #creates shadowcopy every 1:30 hours 

    global last_shadow_backup
    global username
    now = time.time()

    if last_shadow_backup == 0:

        subprocess.run(f'xcopy "C:\\Users\\{username}\\Downloads" "C:\\Users\\{username}\\Downloads\\protected_backup" /Y', shell=True) #creating backup copy
        subprocess.run("wmic shadowcopy delete", shell=True) #deleting outdated shadowbackcup
        subprocess.run("wmic shadowcopy call create Volume='C:\\'", shell=True) #creating shadowbackup
        last_shadow_backup = time.time()

        securing_files(f"C:\\Users\\{username}\\Downloads\\protected_backup")

    if now - last_shadow_backup >= 5400:

        subprocess.run("wmic shadowcopy delete", shell=True) #deleting outdated shadowbackup
        subprocess.run("wmic shadowcopy call create Volume='C:\\'", shell=True) #creating shadowbackup

        last_shadow_backup = time.time()

#--------------------------------------------------------------------------------------------------------

def checking_new_processes(): #verifies processes created on the last 3 minutes and analyze theirs path 

    global last3minutes_processes

    for process in psutil.process_iter():
        now = int(time.time())

        processtime = abs(process.create_time() - now)

        if processtime < 61:
            
            if process.pid not in last3minutes_processes:

                last3minutes_processes.append(process.pid)

        else:

            if process.pid in last3minutes_processes:

                last3minutes_processes.remove(process.pid)

    for process in last3minutes_processes:

        if process not in psutil.process_iter():

            last3minutes_processes.remove(process)



#--------------------------------------------------------------------------------------------------------

class MonitorFolder(FileSystemEventHandler):

    def on_any_event(self, event):
        global data_list
        global change_type

        if evaluate(change_type[0], change_type[1], change_type[2], change_type[3], change_type[4]):
            kill_proc_tree()

        if "trapfile" in event.src_path:
            change_type[4] += 1

        last_change = time.time(), event.src_path, event.event_type
        data_list.append(last_change)

    def on_created(self, event):
        global change_type
        change_type[0] += 1
        if "decrypt" in event.src_path.lower() or "restore" in event.src_path.lower() or "recover" in event.src_path.lower():
            print("possible ransomware, recover files being created.")
            try:
                kill_proc_tree()
            except:
                pass

    def on_deleted(self, event):
        global change_type
        change_type[3] += 1

    def on_modified(self, event):
        global change_type
        change_type[1] += 1
        if extract_extensions(event.src_path):
            try:
                PublicMalware_Detection(event.src_path)
            except:
                pass

    def on_moved(self, event):
        global change_type
        change_type[3] += 1

#--------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    registry.AddToRegistry(name='0B1tRansomwareDetector')
    start_protection()
    shadow_copy()
    trap_create()
    src_path = f"C:\\Users\\{username}\\Downloads"
    
    event_handler= MonitorFolder()
    observer = Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while(True):

            try:

                if evaluate(change_type[0], change_type[1], change_type[2], change_type[3], change_type[4]):
                    kill_proc_tree()
                shadow_copy()
                checking_new_processes()
                time_since_last_change = abs(int(data_list[-1][0] - time.time()))
                

                if time_since_last_change > 10 or sum(change_type) > 20:

                    data_list.clear()
                    change_type = [0, 0, 0, 0, 0]

            except:

                pass

    except KeyboardInterrupt:
        observer.stop()
        observer.join()
