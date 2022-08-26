import regex as re
import subprocess
import os

username = os.getlogin() #get username
users_list = []
get_users = subprocess.run("wmic useraccount get name", capture_output=True, shell=True) #getting machine's users
users = get_users.stdout.decode()
users = re.split("/W|Name|\r|\n", users)

for user in list(users):

    user = user.strip()

    if user == '':
        pass
        
    else:
        users_list.append(user)

def unlocking_files(folder): #allow users to accessing folder

    global users_list

    for user in users_list:

        subprocess.run(f'icacls "{folder}" /grant "{user}":R', shell=True) #giving all users's permissions from folder

unlocking_files(f"C:\\Users\\{username}\\Downloads\\protected_backup")
