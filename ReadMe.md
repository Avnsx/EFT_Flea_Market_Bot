> master: https://github.com/yagamiraku/tarkov_flea_bot_toTherapis

> fork: https://github.com/astron4ik/tarkov_flea_bot_toTherapis

> this fork: https://github.com/Avnsx/EFT_Flea_Market_Bot

#Master: yagamiraku | fork: astron4ik | this fork: Avn

#Description: 
Escape from Tarkov Flea Market Bot
 > for the homies who live on the edge and for the moment

#Installation:
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

#Information to Usage:

	this bot should make you up to 2-4 M roubles an hour
	you can further edit speed by reducing min_price
	the current settings are perfect to do less purchases
	and have the most less spent value at the same time

	another factor is the time
	time.sleep(to_wait / 100) (CTRL + F to find)
	below 100 to make it slower
	above 100 to make it quicker
	if you add time.sleep() anywhere it will break
	the entire code to the point the session cookie dies
	and your bot stops doing purchases completely, due to time outed
	session cookie so only edit the already existing
	time.sleep(to_wait / 100) (CTRL + F to find)

	all you really need to do is go to source.py and start it
	that will trigger getPath.py which gets the file paths
	and saves it to a file that gets then created as config.ini
	this will only be required on the first launch of source.py
	afterwards the bsg launcher will open and you may click play
	you can pretty much run this bot 24/7 but i would recommend
	2 hour cycles also do not use it during bsg updates such
	as server & patch maintenances as bsg will be actively checking
	their game for flaws and the requests to their server might
	get noticed

#Change log compared to older Versions:
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

#Known Bugs:
1. on some systems the balance function, seems to be bugged out
	* as long as it says added item it buys the items
	* if it stops saying added item, restart it
	* i could not fix this as it did not occur for me at all

#Additional:
1. whenever you change your BSG folder location you will need to delete config.ini & run getPath.py again
	* it is recommended to delete __pycache__ sometimes if something breaks
2. you can also start the bot through a cmd popup with the .batch file inside the folder
	* this will delete pycache and clear your dns resolution cache
	* then start the bot in a cmd popout

#Ban Risk:
> Of course there's always a ban risk whenever using 3rd party code! Use this at your own Risk.
	I personally used this blatantly for over a week and pretty much bought every possible item in the game at least once
	I have had a great time together with a buddy using and developing this bot; including hundreds of full geared runs

	Currently the only way to receive a ban through the usage of this - in as far as I know - is when a employee from BattleShitGames,
	who works in their statistical data analysis team manually checks over the Flea Market logs (which historically occurs every Thursday)

	It is your own responsibility to keep yourself up to date using various forums or other information sources to see if there were
	patches from BSG; to break or invalidate the usage of this bot.

# shoutout to my favorite Pepega nikita (:
