########################################################################
versionNumber = 1.0
bannerText = '''
        _____  _                 __                                _ 
       /__   \| |__    ___      / /   ___   __ _   ___  _ __    __| |
         / /\/| '_ \  / _ \    / /   / _ \ / _` | / _ \| '_ \  / _` |
        / /   | | | ||  __/   / /___|  __/| (_| ||  __/| | | || (_| |
        \/    |_| |_| \___|   \____/ \___| \__, | \___||_| |_| \__,_| v{0}
                                           |___/\n
'''.format(versionNumber)

def printBanner():
	print(bannerText)

printBanner()
#######################################################################
import os.path
#######################################################################

#######################################################################
firstTime = os.path.isfile('./.game/player')

playerName = ''
playerClass = ''
playerLevel = 0
playerMeso = 0
playerSP = 0
playerAP = 0
playerEXP = 0
playerClan = ''
playerHP = 0
playerATK = 0
playerDEF = 0
playerLUK = 0
PlayerCRT = 0

choice = 0

def InitializeAccount():
	global playerLevel
	playerLevel = 1
	global playerMeso
	playerMeso = 1000
	global playerHP
	playerHP = 50
	global playerATK
	playerATK = 1
	global playerDEF
	playerDEF = 1
	global playerLUK
	playerLUK = 1
	global PlayerCRT
	PlayerCRT = 1

def CreateAccount():
	fw = open('./.game/player','w')
	fw.write('playerName,'+playerName+'\n')
	fw.write('playerClass,'+playerClass+'\n')
	fw.write('playerLevel,'+str(playerLevel)+'\n')
	fw.write('playerMeso,'+str(playerMeso)+'\n')
	fw.write('playerSP,'+str(playerSP)+'\n')
	fw.write('playerAP,'+str(playerAP)+'\n')
	fw.write('playerEXP,'+str(playerEXP)+'\n')
	fw.write('playerClan,'+playerClan+'\n')
	fw.write('playerHP,'+str(playerHP)+'\n')
	fw.write('playerATK,'+str(playerATK)+'\n')
	fw.write('playerDEF,'+str(playerDEF)+'\n')
	fw.write('playerLUK,'+str(playerLUK)+'\n')
	fw.write('PlayerCRT,'+str(PlayerCRT)+'\n')
	fw.close()

if firstTime:
	# read file then extract informations.
	print('Hello ')
else:
	input('Hello new Player!\n> ')
	playerName = input('What is your name?\n> ')
	if playerName is '':
		flag = False
		while True:
			playerName = input('Please Enter player name\n> ')
			if playerName is not '':
				break
	input('\nHello {0}!! Welcome to \'The Legend\'\n> '.format(playerName))
	classList = "1. Warrior\n2. Thief\n3. Mage\n4. Archer\n5. Pirate\nPlease Enter a number!\n> "
	print('My name is GM.Shawnkoon!')
	while True:
		try:
			choice = int(input('What kind of Class do you want to be?\n\n{0}'.format(classList)))
			if choice > 0 and choice < 6:
				break
			print("Error! Please type a number between 1 - 5.\n")
		except Exception:
			print("Error! Please type a number between 1 - 5.\n")
	
	if choice == 1:
		playerClass = 'Warrior'
	elif choice == 2:
		playerClass = 'Thief'
	elif choice == 3:
		playerClass = 'Mage'
	elif choice == 4:
		playerClass = 'Archer'
	elif choice == 5:
		playerClass = 'Pirate'
	
	input('{0}. Great Choice {1}!! \n> '.format(playerClass, playerName))
	InitializeAccount()
	CreateAccount()
	