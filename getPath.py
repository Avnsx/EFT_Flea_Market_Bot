import os
import configparser
import time
import win32api
config = configparser.ConfigParser()

#after writing this i figured i could have just extracted the path out of registry, but did not care enough to rewrite

if os.path.exists('config.ini'):
    print('[INFO:] Configuration file FOUND; no system scan needed.')
    print('[INFO:] Closing getPath.py within 5 seconds...')
    time.sleep(5)
    exit()
else:
    print('[INFO:] Configuration file NOT FOUND; running file scan on all drives, to locate required files...')
    print('[INFO:] Allow up to 60 seconds for this to finish!')
    print('[INFO:] A configuration file will be created in your installation folder.')
    print('[INFO:] You may edit the path inside it, if it determined the false file location.')
    print('\n[INFO:] DO NOT CLOSE! This process will either continue or close as soon as it is finished on its own...\n')
    path_found1 = None
    path_found2 = None
    path_found3 = None
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    for drive in drives:
    	for r,d,f in os.walk(drive):
    		for file1 in f:
    			if file1 == "EscapeFromTarkov.exe":
    				path_found1 = os.path.join(r,file1)
    				config['DEFAULT']["ClientPath"] = str(path_found1)
    				with open('config.ini', 'w') as configfile:
    					config.write(configfile)
    					print('[INFO:] Found & Added Game Client path ' + str(path_found1) + ' to config.ini')
    		for file2 in f:
    			if file2 == "BsgLauncher.exe":
    				path_found2 = os.path.join(r,file2)
    				config['DEFAULT']["LauncherPath"] =  str(path_found2)
    				with open('config.ini', 'w') as configfile:
    					config.write(configfile)
    					print('[INFO:] Found & Added BSG Launcher path ' + str(path_found2) + ' to config.ini')
    		for file3 in f:
    			if file3 == "sharedassets1.assets":
    				path_found3 = os.path.join(r,file3)
    				config['DEFAULT']["UnityPath"] =  str(path_found3)
    				with open('config.ini', 'w') as configfile:
    					config.write(configfile)
    					print('[INFO:] Found & Added Unity Asset path ' + str(path_found3) + ' to config.ini')

    if path_found1 is None:
        print('[ERROR:] Could not find Game Client path!')
        time.sleep(10)
        exit()

    if path_found2 is None:
        print('[ERROR:] Could not find BSG Launcher path!')
        time.sleep(10)
        exit()

    if path_found3 is None:
        print('[ERROR:] Could not find Unity Asset path!')
        time.sleep(10)
        exit()