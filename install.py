#!/usr/bin/python3
import os
from time import sleep
from urllib.request import urlretrieve
import zipfile
import shutil
import requests

def getlatestrelease(user, repo):
    api = f"https://api.github.com/repos/{user}/{repo}/releases/latest"
    response = requests.get(api)
    response.raise_for_status()
    responseData = response.json()
    assets = responseData["assets"]
    if len(assets) < 1:
        print("could not find the latest version of {repo}, will install an earlier version instead")
        return None, "error"
    else:
        return assets[0]["browser_download_url"], None

pwd = os.path.abspath('')

protonhax_url = "https://raw.githubusercontent.com/jcnils/protonhax/refs/heads/main/protonhax"
protonhax_file =  os.path.join(pwd, "protonhax")

data_interface_url, error = getlatestrelease("GHXX","FiveDChessDataInterface")
if error:
    data_interface_url = "https://github.com/GHXX/FiveDChessDataInterface/releases/download/v0.4.3/Console_win10_x64_standalone_v0.4.3.zip"
data_interface_file = os.path.join(pwd, 'Console_win10_x64_standalone_v0.4.3', "data_interface.zip")

pgn_recorder_url, error = getlatestrelease("penteract","5D-PGN-Recorder")
if error:
    pgn_recorder_url = "https://github.com/penteract/5D-PGN-Recorder/releases/download/v0.7/5DPGNRecorder0_7.zip"
pgn_recorder_file = os.path.join(pwd, '5DPGNRecorder0_7', "pgn_recorder.zip")

puzzles_url = "https://drive.usercontent.google.com/download?id=1BUPUKyXMZKDcNs6qBoOZIj83zt_eeDgu&export=download&authuser=0&confirm=t&uuid=b3c309a7-576e-4b20-be8d-fef8fefbdba3&at=AEz70l6kvlJ0SSjd48drlycGwKz-:1740266070709"
puzzles_file = os.path.join(pwd, "puzzles.zip")

pgn_loader_url, error = getlatestrelease("mauer01", "gui-for-5dchess-datainterface")
if error:
    pgn_loader_url = "https://github.com/mauer01/gui-for-5dchess-datainterface/releases/download/v1.4/gui.for.5d.datainterface.exe"
pgn_loader_file = os.path.join(pwd, "gui_data_interface", "gui_data_interface.exe")

try:
    if os.path.exists(os.path.join(pwd,'protonhax')) is False:
        print("Downloading protonhax ...")
        urlretrieve(protonhax_url, protonhax_file)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Downloading protonhax ... FINISHED")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Re-downloading protonhax ...")
        os.remove(protonhax_file)
        urlretrieve(protonhax_url, protonhax_file)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Re-ownloading protonhax ... FINISHED")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

    os.system('chmod +x protonhax')

except Exception as e:
    print("Failed to download protonhax")
    os.system('cls' if os.name == 'nt' else 'clear')

print()
print("Choose what to download.")
print("You can choose more than 1 by seperating options with a comma.")
print()

download_names = ["5D Chess Data Interface", "5D Chess PGN Recorder", "OJCard Mathbook Puzzles", "GUI For Data Interface"]

for index, download in enumerate(download_names):
    print(f"({index+1}) {download}")

print()

download_input = input()
need_to_download = download_input.split(',')
os.system('cls' if os.name == 'nt' else 'clear')

if '1' in need_to_download:

    if os.path.exists(data_interface_file) is False:
        print(f"Downloading {download_names[0]} ...")
        os.mkdir(os.path.join(pwd, 'Console_win10_x64_standalone_v0.4.3'))
        urlretrieve(data_interface_url, data_interface_file)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Downloading {download_names[0]} ... FINISHED")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(f"Re-downloading {download_names[0]} ...")
        shutil.rmtree(os.path.join(pwd, 'Console_win10_x64_standalone_v0.4.3'))
        os.mkdir(os.path.join(pwd, 'Console_win10_x64_standalone_v0.4.3'))
        urlretrieve(data_interface_url, data_interface_file)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Re-downloading {download_names[0]} ... FINISHED")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

if '2' in need_to_download:

    if os.path.exists(pgn_recorder_file) is False:
        print(f"Downloading {download_names[1]} ...")
        os.mkdir(os.path.join(pwd, '5DPGNRecorder0_7'))
        urlretrieve(pgn_recorder_url, pgn_recorder_file)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Downloading {download_names[1]} ... FINISHED")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(f"Re-downloading {download_names[1]} ...")
        shutil.rmtree(os.path.join(pwd, '5DPGNRecorder0_7'))
        os.mkdir(os.path.join(pwd, '5DPGNRecorder0_7'))
        urlretrieve(pgn_recorder_url, pgn_recorder_file)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Re-downloading {download_names[1]} ... FINISHED")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

if '3' in need_to_download:

    if os.path.exists(puzzles_file) is False:
        print(f"Downloading {download_names[2]} ...")
        urlretrieve(puzzles_url, puzzles_file)
        with zipfile.ZipFile(puzzles_file) as zip_ref:
            zip_ref.extractall(os.path.join(pwd))
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Downloading {download_names[2]} ... FINISHED")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(f"Re-downloading {download_names[2]} ...")
        shutil.rmtree(os.path.join(pwd, 'Intro to 5D Chess - All Puzzles v2'))
        urlretrieve(puzzles_url, puzzles_file)
        with zipfile.ZipFile(puzzles_file) as zip_ref:
            zip_ref.extractall(os.path.join(pwd))
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Re-downloading {download_names[2]} ... FINISHED")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

if '4' in need_to_download:

    if os.path.exists(pgn_loader_file) is False:
        print(f"Downloading {download_names[3]} ...")
        os.mkdir(os.path.join(pwd, 'gui_data_interface'))
        urlretrieve(pgn_loader_url, pgn_loader_file)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Downloading {download_names[3]} ... FINISHED")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(f"Re-downloading {download_names[3]} ...")
        shutil.rmtree(os.path.join(pwd, 'gui_data_interface'))
        os.mkdir(os.path.join(pwd, 'gui_data_interface'))
        urlretrieve(pgn_loader_url, pgn_loader_file)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Re-downloading {download_names[3]} ... FINISHED")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')


for subdir in os.listdir(os.path.join(pwd)):
    if os.path.isdir(os.path.join(pwd, subdir)):
        for file in os.listdir(os.path.join(pwd, subdir)):
            if '.zip' in file:

                with zipfile.ZipFile(os.path.join(pwd, subdir, file), 'r') as zip_ref:
                    zip_ref.extractall(os.path.join(pwd, subdir))

print()
print("Please Enter the following string to your steam launch options")
print("It can be found under Properties > General in the steam library page for 5D Chess")
print()
print("protonhax init %COMMAND%")
print()
input("Press ENTER after you modified the launch option")
os.system('cls' if os.name == 'nt' else 'clear')
print("INSTALLATION FINISHED SUCCESSFULLY")
