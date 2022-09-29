<p align="right"><strong>English</strong> | <a href="https://github.com/Grupo0b1t/eye-of-shiva/blob/main/READMEpt-br.md">Português</a></p>

# Eye of Shiva #

## Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Setup and how to use it](#Setup-and-how-to-use-it)
* [Description](#description)

## General Info

This tool is capable of identifying and blocking a ransomware attack on a Windows machine, in addition to recovering possibly compromised files.\
\
It counts with many ways of:
* Detecting a ransomware. Such as: 
    - File Hashing
    - Trap Files
    - By suspicious Files
    - By File System Changes
    - Machine Learning
* Preventing. Such as:
    - Protected Local Backup
    - Protected Shadow Copy
* Stopping:
    - Filtering and Killing Processes

## Technologies

This project is created with:
* Python3

Libraries used:
* psutil
* regex
* watchdog
* requests
* scikit-learn
* pillow

## Setup and how to use it

1. Download and install [Python](https://www.python.org/downloads/) on your computer
2. Simply download the [Eye of Shiva.zip](https://github.com/Grupo0b1t/eye-of-shiva/blob/main/Eye%20of%20Shiva/Eye%20of%20Shiva.rar) folder and run:
* On cmd: `python setup.py` for:
    - installing the dependencies
* `Eye of Shiva Setup.exe` to:
    - install the tool on your computer
* It's recommended to create a shortcut on your desktop as it would be easier to run our tool.


## Description

### Main screen

![App Screenshot](https://cdn.discordapp.com/attachments/669945882162233358/1025149527356874752/unknown.png)

You can activate/deacitvate the protection by clicking on the Power buttom at the main screen

### Advanced Settings

![App Screenshot](https://cdn.discordapp.com/attachments/669945882162233358/1025149565202092052/unknown.png)

* Create backup
    - By cliking on backup you can create an updated version of your shadow copy and delete the old one
    
* Lock/Unlock Backup Folder
    - By clicking on locked/unlock button you can grant access to yourself to edit the contents of your protected_folder located at your Desktop

