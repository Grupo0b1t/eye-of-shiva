from machinelearning_ransomware_detector import securing_files, shadow_copy
from PIL import Image, ImageTk
import tkinter as tk
import subprocess
import webbrowser
import time
import json
import os

def find_images(images_json):
    with open(images_json, 'r', encoding='utf8') as f:
        return json.load(f)

images_json = "images_path.json"

inicialize_pid = None

username = os.getlogin()

class Base:
    """In this class, contains the base of the main window of the program"""

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("0B1T Ransonware Detector")
        self.window.call("wm", "iconphoto", self.window._w, tk.PhotoImage(file=find_images(images_json)["shiva_path"]))
        self.window.geometry("600x400")
        self.window.resizable(0, 0)

class Informations_Base:
    """In this class, contains the base of the informations window"""

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Additional Information")
        self.window.tk.call("wm","iconphoto", self.window._w, tk.PhotoImage(file=find_images(images_json)["shiva_path"]))
        self.window.geometry("300x363")
        self.window.resizable(0 ,0)

class Settings_Base:
    """In this class, contains the base of the settings window."""

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Settings")
        self.window.tk.call('wm','iconphoto', self.window._w, tk.PhotoImage(file=find_images(images_json)["shiva_path"]))
        self.window.geometry("400x270")
        self.window.resizable(0, 0)

class Background(Base):
    """In this class, contains the background of the main window

    Args:
        Base: Base of the main window of the program
    """

    def __init__(self):
        super().__init__()
        self.bg = tk.PhotoImage(file=find_images(images_json)["bg_path"])
        self.canvas = tk.Canvas(self.window, highlightthickness=0, bg="#13131C")
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")
        self.canvas.pack(fill="both", expand=True)

class Settings_Background(Settings_Base):
    def __init__(self):
        super().__init__()

        self.lock_folder = True
        self.automatic_backups = True

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        self.lock_on = ImageTk.PhotoImage(Image.open(find_images(images_json)["lock_On_path"]))
        self.lock_off = ImageTk.PhotoImage(Image.open(find_images(images_json)["lock_Off_path"]))

        self.backup_on = ImageTk.PhotoImage(Image.open(find_images(images_json)["backup_On_path"]))
        self.backup_off = ImageTk.PhotoImage(Image.open(find_images(images_json)["backup_Off_path"]))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        self.canvas = tk.Canvas(self.window, highlightthickness=0, bg="#13131C")
        self.canvas.create_image(0,0, anchor="nw")                                            #BACKGROUND
        self.canvas.pack(fill="both", expand=True)

        self.settings_label = tk.Label(self.window,
                                       text="Advanced Settings",
                                       fg="white",
                                       bg="#13131C",
                                       font=("@Yu Gothic UI Light", 17))
        self.settings_label.place(relx=0.253, rely=0.09, anchor="center")

        self.lock_folder_label = tk.Label(self.window,
                                          text="    Your backup is secure.",
                                          fg="#6C9FED",
                                          bg="#13131C",
                                          font=('@Yu Gothic UI Light', 13))

        self.description1_label = tk.Label(self.window,
                                       text="\t            A snapshot is created to protect the current state\nof the machine. (ShadowCopy)",
                                       fg="gray",
                                       bg="#13131C",
                                       font=("@Yu Gothic UI Light", 11))
        self.description1_label.place(relx=0.274, rely=0.375, anchor="center")

        self.automatic_backups_label = tk.Label(self.window, 
                                                text="Create a backup file.",
                                                fg="#6C9FED",
                                                bg="#13131C",
                                                font=("@Yu Gothic UI Light", 13))                                                                            
                                                
        self.settings_label = tk.Label(self.window,
                                       text="Lock/Unlock Backup Folder",
                                       fg="white",
                                       bg="#13131C",
                                       font=("@Yu Gothic UI Light", 15))
        self.settings_label.place(relx=0.314, rely=0.63, anchor="center")
                                             
        self.settings_label = tk.Label(self.window,
                                       text="Create Backup",
                                       fg="white",
                                       bg="#13131C",
                                       font=("@Yu Gothic UI Light", 15))
        self.settings_label.place(relx=0.1845, rely=0.24, anchor="center")
                                        
        self.description2_label = tk.Label(self.window,
                                       text="\t\t      Your files are backed up in a protected folder.\n\t         It is recommended to keep it locked.",
                                       fg="gray",
                                       bg="#13131C",
                                       font=("@Yu Gothic UI Light", 11))
        self.description2_label.place(relx=0.20, rely=0.765, anchor="center")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        self.lock_folder_button = tk.Button(self.window,
                                            image=self.lock_on,
                                            bg="#13131C",
                                            bd=0,
                                            highlightthickness=0,
                                            activebackground="#13131C",
                                            command=self.changeMode_lockFolder)

        self.automatic_backups_button = tk.Button(self.window,                                                 #BUTTONS
                                                  image=self.backup_on,
                                                  bg="#13131C",
                                                  bd=0,
                                                  highlightthickness=0,
                                                  activebackground="#13131C",
                                                  command=self.pressed)
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
        
        self.lock_folder_button.place(relx=0.89, rely=0.89, anchor="center")
        self.automatic_backups_button.place(relx=0.89, rely=0.50, anchor="center")
        self.automatic_backups_button.bind("<Enter>", self.on_enter)
        self.automatic_backups_button.bind("<Leave>", self.on_leave)

        self.lock_folder_label.place(relx=0.221, rely=0.89, anchor="center")
        self.automatic_backups_label.place(relx=0.222, rely=0.495, anchor="center")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def changeMode_lockFolder(self):
        global username

        if self.lock_folder:
            self.lock_folder_button.config(image=self.lock_off) 
            self.lock_folder_label.config(text="     Your backup is vulnerable!", fg="#FF5757")
            self.lock_folder_label.place(relx=0.247, rely=0.885, anchor="center")            
            self.lock_folder = False
            
        else: 
            self.lock_folder_button.config(image=self.lock_on) 
            self.lock_folder_label.config(text="     Your backup is secure.", fg="#6C9FED")
            self.lock_folder_label.place(relx=0.215, rely=0.885, anchor="center")            
            self.lock_folder = True

        securing_files(self.lock_folder, username)

    def on_enter(self, event):
        self.automatic_backups_button.config(image=self.backup_off)
    
    def on_leave(self, enter):
        self.automatic_backups_button.config(image=self.backup_on)
    
    def pressed(self):
        global username
        shadow_copy(self.automatic_backups)
        time.sleep(1)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Informations_Background(Informations_Base):
    def __init__(self):
        super().__init__()
        us_path = tk.PhotoImage(file=find_images(images_json)["_us_path"])
        self.canvas = tk.Canvas(self.window, width=40, height=40, highlightthickness=0, bg="#13131C")
        self.canvas.pack(fill="both", expand=True, anchor="center")
                
        self.info_label = tk.Label(self.window, 
                                   text="Who are we?",
                                   fg="white",
                                   bg="#13131C",
                                   font=("@Yu Gothic UI Light", 17))
        self.info_label.place(relx=0.50, rely=0.07, anchor="center")
        
        self.desc_label = tk.Label(self.window,
                                   text="We are cybersecurity students at\nFIAP University.\nWe have developed with great effort\nand dedication this software\ncapable of detecting and removing\nRansomware, one of the threats that\nmost affects companies today.",
                                   fg="gray",
                                   bg="#13131C",
                                   font=("@Yu Gothic UI Light", 13))                                   
        self.desc_label.place(relx=0.495, rely=0.350, anchor="center")
        
        self.img_label = tk.Label(self.window,
                                  image=us_path,
                                  bg="#13131C",
                                  width=300)
                                  
        self.img_label.us_path = us_path
        self.img_label.pack()


class SiteButton(Background):
    """Open site

    Args:
        Background: Background of the main window
    """

    def __init__(self):
        super().__init__()
        self.team = ImageTk.PhotoImage(Image.open(find_images(images_json)["team_path"]))
        self.open_site_button = tk.Button(self.window,
                                          image=self.team,
                                          bg="#14141D",
                                          bd=0,
                                          activebackground="#14141D",
                                          highlightthickness=0,
                                          command=self.open_site)

        self.open_site_button.place(relx=0.945, rely=0.915, anchor="center")
    
    def open_site(self):
        webbrowser.open_new(r"https://eyeofshiva.surge.sh")


class Informations_Button(Background):
    def __init__(self):
        super().__init__()
        self.info_path = Image.open(find_images(images_json)["info_path"])
        self.info_img = ImageTk.PhotoImage(self.info_path)
        self.info_button = tk.Button(self.window,
                                     image=self.info_img,
                                     bg="#14141D",
                                     bd=0,
                                     highlightthickness=0,
                                     activebackground="#14141D",
                                     command=Informations_Background)
        self.info_button.place(relx=0.87, rely=0.915, anchor="center")


class Settings_Main_Button(Background):
    """Open settings

    Args:
        Background: Background of the main window
    """
    def __init__(self):
        super().__init__()
        self.settings_img = ImageTk.PhotoImage(Image.open(find_images(images_json)["settings_path"]))
        self.settings_button = tk.Button(self.window,
                                         image=self.settings_img,
                                         bg="#14141D",
                                         bd=0,
                                         highlightthickness=0,
                                         activebackground="#13131C",
                                         command=Settings_Background)
        self.settings_button.place(relx=0.795, rely=0.918, anchor="center", width="40", height="40")


class MainButton(Background):
    """Main button to turn the program on and off

    Args:
        Background: Background of the main window
    """

    def __init__(self):
        super().__init__()
        self.is_on = False
        self.button_on_path = Image.open(find_images(images_json)["button_on_path"])
        self.button_off_path = Image.open(find_images(images_json)["button_off_path"])

        self.button_on = ImageTk.PhotoImage(self.button_on_path)
        self.button_off = ImageTk.PhotoImage(self.button_off_path)

        self.button = tk.Button(self.window, image=self.button_off, bd=0, command=self.changeMode)
        self.button.place(relx=0.5, rely=0.29, anchor="center", width="165", height="165")

        self.button_label = tk.Label(self.window, 
                                     text="Protection Disabled",
                                     font=("@Yu Gothic UI Light", 20),
                                     fg="white", 
                                     bg="#171721")
        
        self.button_label_description = tk.Label(self.window, 
                                                 text="Your files are vulnerable from Ransomware",
                                                 fg="gray", 
                                                 font=('@Yu Gothic UI Light', 17),
                                                 bg="#171721")
        self.button_label.place(relx=0.5, rely=0.55, anchor="center")
        self.button_label_description.place(relx=0.5, rely=0.64, anchor="center")

    def changeMode(self):
        """Turn on or off main button"""

        global inicialize_pid

        if self.is_on:
            self.button.config(image=self.button_off) 
            self.button_label.config(text="Protection Disabled", fg="white") 
            self.button_label_description.config(text="Your files are vulnerable against Ransomware")
            self.is_on = False
            
        else: 
            self.button.config(image=self.button_on) 
            self.button_label.config(text="Protection Enabled", fg="white")
            self.button_label_description.config(text="Your files are protected from Ransomware")
            self.is_on = True
            inicialize = subprocess.Popen('python ".\\machinelearning_ransomware_detector.py"', shell=False)
            inicialize_pid = inicialize.pid

        if not self.is_on:
            subprocess.call(['taskkill', '/F', '/T', '/PID',  str(inicialize_pid)])
            

class Main(Informations_Button, MainButton, SiteButton, Settings_Main_Button):
    def __init__(self):
        super().__init__()
        self.window.mainloop()

if __name__ == "__main__":
    Main()