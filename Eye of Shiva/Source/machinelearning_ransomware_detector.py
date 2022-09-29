from PublicMalware_detection import PublicMalware_Detection
from watchdog.events import FileSystemEventHandler
from ransomware_behave_db import evaluate
from watchdog.observers import Observer
import regex as re
import subprocess
import pathlib
import psutil
import time
import os


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
    

def check_PID_interface():
    with open("pid.txt", "r") as file:
        data = file.read()
    return int(data)

#--------------------------------------------------------------------------------------------------------

def kill_proc_tree(): #kills process tree, parent and child processes
    
    global last3minutes_processes
    #print("possible ransomware detected")
    
    pids = ""
    for pid in reversed(last3minutes_processes):
        if pid != os.getpid() and pid != check_PID_interface():
            pids += f"/PID {pid} "
    
    subprocess.run(f"taskkill {pids}/F /T", shell=False)
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

def trap_create(): #creates honeypot files

    try:
        for x in range(1, 500):
            with open(f"C:\\Users\\{username}\\Desktop\\_trapfile{x}.txt", "w") as file:
                file.write("trap file for ransomware detection")
                subprocess.run(f'attrib +h "C:\\Users\\{username}\\Desktop\\_trapfile{x}.txt"')
    except:
        pass


def start_protection(): #creates a folder that is going to be used as backup and gets machine's users

    global users_list
    global username
    procname = psutil.Process(os.getpid()).name()
    subprocess.run(f'wmic process where name="{procname}" CALL setpriority "above normal"', shell=True)
    subprocess.run(f'mkdir "C:\\Users\\{username}\\Desktop\\protected_backup"', shell=True) #creating protected_folder
    subprocess.run(f'xcopy "C:\\Users\\{username}\\Desktop" "C:\\Users\\{username}\\Desktop\\protected_backup" /Y', shell=True) #creating backup copy
    subprocess.run("takeown /F C:\\Windows\\System32\\vssadmin.exe", shell=True)
    subprocess.run(f'icacls C:\\Windows\\System32\\vssadmin.exe /grant "{username}":F', shell=True)
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
    trap_create()


def securing_files(active, user): #forbid all users from accessing folder

    if active:
        subprocess.run(f'icacls "C:\\Users\\{username}\\Desktop\\protected_backup" /deny "{user}":R', shell=True) #removing all users's permissions from folder

    else:
        subprocess.run(f'icacls "C:\\Users\\{username}\\Desktop\\protected_backup" /grant "{user}":R', shell=True) #giving all users's permissions from folder



def shadow_copy(active): #creates shadowcopy 
    if active:
        subprocess.run("wmic shadowcopy delete", shell=True) #deleting outdated shadowbackup
        subprocess.run('wmic shadowcopy call create Volume="C:\\"', shell=True) #creating shadowbackup


#--------------------------------------------------------------------------------------------------------

def checking_new_processes(): #verifies processes created on the last 3 minutes and analyze theirs path 

    global last3minutes_processes

    for process in psutil.process_iter():
        now = int(time.time())

        processtime = abs(process.create_time() - now)

        if processtime < 61:
            
            if process.pid not in last3minutes_processes:
                if process.pid != check_PID_interface():
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

        if "trapfile" in event.src_path:
            change_type[4] += 1

        last_change = time.time(), event.src_path, event.event_type
        data_list.append(last_change)

    def on_created(self, event):
        global change_type
        if "protected_backup" in event.src_path:
            pass

        else:
            change_type[0] += 1
        if "decrypt" in event.src_path.lower() or "restore" in event.src_path.lower() or "recover" in event.src_path.lower():
            print("possible ransomware, recover files being created.")
            try:
                kill_proc_tree()
            except:
                pass

    def on_deleted(self, event):
        global change_type
        if "protected_backup" in event.src_path:
            pass

        else:
            change_type[3] += 1

    def on_modified(self, event):
        global change_type
        if "protected_backup" in event.src_path:
            pass

        else:
            change_type[1] += 1

        if extract_extensions(event.src_path):
            try:
                PublicMalware_Detection(event.src_path)
            except:
                pass

    def on_moved(self, event):
        global change_type
        if "protected_backup" in event.src_path:
            pass

        else:
            change_type[2] += 1

#--------------------------------------------------------------------------------------------------------

def inicialize():
    global change_type, data_list, username
    start_protection()
    shadow_copy(True)
    src_path = f"C:\\Users\\{username}\\Desktop"
    event_handler= MonitorFolder()
    observer = Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while(True):
            checking_new_processes()
            try:
                
                if evaluate(change_type[0], change_type[1], change_type[2], change_type[3], change_type[4]):
                    kill_proc_tree()
                    print("Ransomware Detected!")
                
                time_since_last_change = abs(int(data_list[-1][0] - time.time() if any(data_list) else 0))
                
                if time_since_last_change > 4 or sum(change_type) > 20:
                    data_list.clear()
                    change_type = [0, 0, 0, 0, 0]

            except:
                pass

    except KeyboardInterrupt:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    inicialize()

