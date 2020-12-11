import os

for folder, subfolders, filenames in os.walk('/home/tarun/Tarun/DSC@DSU'):
    print(f'The current folder is {folder}')

    for subfolder in subfolders:
        print(f'SUBFOLDER OF {folder}: {subfolder}')

    for filename in filenames:
        print(f'FILE INSIDE {folder} : {filename}')

    print("\n")