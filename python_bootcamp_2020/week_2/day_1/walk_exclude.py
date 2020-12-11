import os
for dirpath, dirnames, filenames in os.walk('/home/tarun/Tarun/DSC@DSU'):
    dirnames[:] = [subfolder for subfolder in dirnames if subfolder!='.git']
    print(f'The current dirpath is {dirpath}')

    for subfolder in dirnames:
        print(f'SUBFOLDER OF {dirpath}: {subfolder}')

    for filename in filenames:
        print(f'FILE INSIDE {dirpath} : {filename}')

    print("\n")