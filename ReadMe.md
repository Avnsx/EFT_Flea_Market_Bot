![GitHub Banner](https://raw.githubusercontent.com/Avnsx/EFT_Flea_Market_Bot/master/project_banner.PNG)

> master: https://github.com/yagamiraku/tarkov_flea_bot_toTherapis

> fork: https://github.com/astron4ik/tarkov_flea_bot_toTherapis

> this fork: https://github.com/Avnsx/EFT_Flea_Market_Bot

> UC thread: https://www.unknowncheats.me/forum/escape-from-tarkov/405112-updated-flea-market-bot.html

#Master: yagamiraku | fork: astron4ik | this fork: Avn

# Description: 
Escape from Tarkov Flea Market Bot
 > for the homies who live on the edge and for the moment

# Installation:
> Get python from below
https://www.python.org/downloads/release/python-383/
	"Windows x86-64 executable installer" from link above
		make sure to click add to PATH in the python installer
			also I would recommend doing customized > for all users

> install pip through the python installer itself or below
https://pip.pypa.io/en/stable/installing/

#Run the commands below in CMD
> Requires pip & CMD should be started as Admin

	python -m pip install --upgrade pip
	pip install requests
	pip install pywin32
	pip install UnityPy
	pip install psutil
	pip install --upgrade setuptools

#Download below to be able to use required win32api	
https://github.com/mhammond/pywin32/releases
"pywin32-228.win-amd64-py3.8.exe" from link
	above for 64-bit Windows & 64-bit Python

#Download Microsoft Build Tools 14.00+
https://go.microsoft.com/fwlink/?LinkId=691126
> Used it here for UnityPy
	it is a 5gb file unluckily; it is apart of the
	 auto update feature for further EFT and Unity Versions
		basically if Therapist does not get disabled or if they do not
			patch the way this code gets its PHPSESSID / session token we gucci

#Open EFT Launcher > Settings > and Set "Close Launcher when game starts"

# Information to Usage:

	this bot should make you up to 2-4 M roubles an hour
	you can further edit speed by reducing min_price
	the current settings are perfect to do less purchases
	and have the most less spent value at the same time
	
	we are aiming to do less purchases because we don't want
	our therapist > spent value on trader > to go to absurd
	amounts of roubles as it will look illegitimate;
	with current default settings you will be profiting around
	75 % of the value you are buying and reselling back to trader for.
	so let us say you got 2 million spent on therapist during usage;
	you will be left back with raw 1.5 million of those 2 million
	roubles straight in your inventory

	another factor is the time time.sleep(to_wait / 100)
	(CTRL + F to find) inside source.py
	below 100 to make it slower
	above 100 to make it quicker
	if you add time.sleep() anywhere it will break
	the entire code to the point the session cookie dies
	and your bot stops doing purchases completely, due to time outed
	session cookie so only edit the already existing
	time.sleep(to_wait / 100) (CTRL + F to find)
	time.sleep() operates in milliseconds

	all you really need to do is go to source.py and start it
	that will trigger getPath.py which gets the file paths
	and saves it to a file that gets then created as config.ini
	this will only be required on the first launch of source.py
	afterwards the bsg launcher will open and you may click play
	
	the game client should be launched and automaticaly instantly
	closed again, while the bot operates on low cpu usage and tarkov
	is closed. during that time, you can go watch videos or go afk.
	
	you can pretty much run this bot 24/7 but i would recommend
	2 hour cycles also do not use it during bsg updates such
	as server & patch maintenances as bsg will be actively checking
	their game for flaws and the requests to their server might
	get noticed

# Change log compared to older Versions:
1. heavy visual updates
2. fixed environment
	* fixed performance
	* crash free
	* smooth overall
	* fixed PHPSESSID fetch to make it more reliable
	* fixed various bugs within certain functions
4. auto start for bsg launcher
5. auto fetches client launcher and unity path and versions
	* allowing it to auto update its header request
	* forcing BSG to heavier measures to detect this bot
	* even if updating their game
6. informative error handling
	* allowing user to understand what is going on
7. proper instructive README.md

# Known Bugs:
1. on some systems the balance function, seems to be bugged out
	* as long as it says added item it buys the items
	* if it stops saying added item, restart it
	* i could not fix this as it did not occur for me at all

# Additional:
1. whenever you change your BSG folder location you will need to delete config.ini & run getPath.py again
	* it is recommended to delete __pycache__ sometimes if something breaks
2. you can also start the bot through a cmd popup with the .batch file inside the folder
	* this will delete pycache and clear your dns resolution cache
	* then start the bot in a cmd popout

# Ban Risk & Work status:
Detected and patched due to them adding captchas to the eft api. Gave up on this project due to lack of time, prolly easily unpatchable but it's up to you (:
If you're going for an unpatch; you have to add all the new auth stuff and also make sure you actually send the new BSGLauncher Useragent for all requests.
At the time of writing this all of that didn't exist in first place, so I never had to add them. Unfortunately since I released this bot(first public EFT Flea Market bot ever of it's kind) and all the people that learnt from this bot and made copies of theirs; so these type of bots got lots of attention and they've heavily updated and started checking through all their received requests.
I do no longer develop updates for this bot please stop asking. On the 11th of January 2021, was the last person that contacted me saying that he had ran the bot and apparently it still worked for him for a good week generating 10M until he got banned.

# Uninstall:
> You no longer wish to use this bot?
	check this article out on how to uninstall files:
	https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-10-4b55f974-2cc6-2d2b-d092-5905080eaf98
	
	the file names are Python 3.8 pywin32-228, Microsoft Visual C++ Build Tools, Python 3.8 (64-bit) & Python Launcher

	to delete the bot itsself; go to the download location and simply delete the folder "EFT_Flea_Market_Bot"

