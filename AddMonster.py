import json
from pathlib import Path
from Banner import Banner
#######################################################################
Banner.printBanner()
#######################################################################

filePATH = './.game/monsters.json'

myFile = Path(filePATH)
if not myFile.is_file():
	print("Initial file established!\n>")
	with open(filePATH, 'w') as outfile:
		json.dump([], outfile)


monsterName = ''
monsterLevel = 0
monsterMeso = 0
monsterDescription = ''
monsterHP = 0
monsterATK = 0
monsterDEF = 0
monsterLUK = 0
monsterCRT = 0

monsterName = input('Please Enter [name] of Monster\n> ')

monsterDescription = input('Please Enter [description] of Monster\n> ')

monsterLevel = int(input('Please Enter [level] of Monster\n> '))

monsterMeso = int(input('Please Enter amount of [meso] Monster gives\n> '))

monsterHP = int(input('Please Enter [HP] of monster\n> '))

monsterATK = int(input('Please Enter [ATK] of monster\n> '))

monsterDEF = int(input('Please Enter [DEF] of monster\n> '))

monsterLUK = int(input('Please Enter [LUK] of monster\n> '))

monsterCRT = int(input('Please Enter [CRT] of monster\n> '))

data = {}
data['Name'] = monsterName
data['Description'] = monsterDescription
data['Level'] = monsterLevel
data['Meso'] = monsterMeso
data['HP'] = monsterHP
data['ATK'] = monsterATK
data['DEF'] = monsterDEF
data['LUK'] = monsterLUK
data['CRT'] = monsterCRT

with open(filePATH) as feedJson:
	feeds = json.load(feedJson)

feeds.append(data)

with open(filePATH, 'w') as outfile:
	json.dump(feeds, outfile)

print('Monster \'{0}\' added successfully!'.format(monsterName))