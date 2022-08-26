<p align="right"><strong>English</strong> | <a href="https://github.com/Grupo0b1t/eye-of-shiva/blob/main/READMEpt-br.md">Português</a></p>

# Eye of Shiva #

## Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Setup and how to use it](#Setup-and-how-to-use-it)

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
* Python 3.10.4
\
Libraries used:
* OS
* pathlib
* psutil
* time
* subprocess
* regex
* watchdog
* requests
* hashlib
* sklearn
* tkinter
* PIL
* webbrowser

## Setup and how to use it

1. Download and install [Python](https://www.python.org/downloads/) on your computer
2. Simply download the [ANTI-RANSOMWARE](https://github.com/Grupo0b1t/eye-of-shiva/tree/main/ANTI-RANSOMWARE) folder and run:
* `machinelearning_ransomware_detector.py` for:
    - the actual tool
* `arq.py` to:
    - unlock the protected_backup
* It's not required to run `AddRegistry.py`, `PublicMalware_detection.py` and `ransomware_behave_db.py` because they are used automatically.
