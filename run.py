#!/usr/bin/python

import os

pwd = os.path.abspath('')

name_list = ["5D Chess Data Interface", "5D Chess PGN Recorder", "OJCard_Mathbook_Puzzles", "GUI For Data Interface"]

print()
print("PLEASE START 5D CHESS ON STEAM VIA PROTON!")
print()
input("Press ENTER after the game has been launched")
os.system('cls' if os.name == 'nt' else 'clear')

print()
print("Choose a program to run")
print()

for index, name in enumerate(name_list):
    print(f"({index+1}) {name}\"")

print()
run_input = input()
os.system('cls' if os.name == 'nt' else 'clear')

if '1' in run_input:

    if os.path.isdir(os.path.join(pwd, 'Console_win10_x64_standalone_v0.4.3')):
        os.system(f"./protonhax run 1349230 \"{os.path.join(pwd, 'Console_win10_x64_standalone_v0.4.3', 'DataInterfaceConsole.exe')}\"")
    else:
        print("Error: File Not Found")

elif '2' in run_input:

    if os.path.isdir(os.path.join(pwd, '5DPGNRecorder0_7')):
        os.system(f"./protonhax run 1349230 \"{os.path.join(pwd, '5DPGNRecorder0_7', '5DPGNRecorderAndTimeReminder.exe')}\"")
    else:
        print("Error: File Not Found")

elif '3' in run_input:

    if os.path.isdir(os.path.join(pwd, 'Intro to 5D Chess - All Puzzles v2')):
        os.system(f"./protonhax run 1349230 \"{os.path.join(pwd, 'Intro to 5D Chess - All Puzzles v2', 'Code', 'DataInterfaceConsole.exe')}\"")

    else:
        print("Error: File Not Found")

elif '4' in run_input:

    if os.path.isdir(os.path.join(pwd, 'gui_data_interface')):
        os.system(f"./protonhax run 1349230 \"{os.path.join(pwd, 'gui_data_interface', 'gui_data_interface.exe')}\"")
