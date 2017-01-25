import json
from pathlib import Path
from Banner import Banner
#######################################################################
Banner.printBanner()
#######################################################################

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
filePATH = './.game/player.json'

choice = 0

myFile = Path(filePATH)
if not myFile.is_file():
	print("Initial file established!\n>")
	with open(filePATH, 'w') as outfile:
		json.dump([], outfile)

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

playerLevel = 1
playerMeso = 1000
playerHP = 50
playerATK = 1
playerDEF = 1
playerLUK = 1
PlayerCRT = 1

data = {}
data['Name'] = playerName
data['Class'] = playerClass
data['Level'] = playerLevel
data['Meso'] = playerMeso
data['SP'] = playerSP
data['AP'] = playerAP
data['EXP'] = playerEXP
data['Clan'] = playerClan
data['HP'] = playerHP
data['ATK'] = playerATK
data['DEF'] = playerDEF
data['LUK'] = playerLUK
data['CRT'] = PlayerCRT

with open(filePATH) as feedJson:
	feeds = json.load(feedJson)

feeds.append(data)

with open(filePATH, 'w') as outfile:
	json.dump(feeds, outfile)
	