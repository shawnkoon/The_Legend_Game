import json
from pathlib import Path
from Banner import Banner
#######################################################################
Banner.printBanner()
#######################################################################

filePATH = './.game/armors.json'

myFile = Path(filePATH)
if not myFile.is_file():
	print("Initial file established!\n>")
	with open(filePATH, 'w') as outfile:
		json.dump([], outfile)

armorName = ""
armorClass = ""
armorPrice = 0
armorDescription = ""
armorATK = 0
armorDEF = 0
armorLUK = 0
armorCRT = 0

choice = 0

armorName = input('What is the armor name?\n> ')
if armorName is '':
	while True:
		armorName = input('Please Enter armor name\n> ')
		if armorName is not '':
			break
armorClassList = "1. Rare\n2. Epic\n3. Unique\n4. Diamond\n5. Legendary\nPlease Enter a number!\n> "
print('My name is GM.Shawnkoon!')
while True:
	try:
		choice = int(input('What kind of Class is this?\n\n{0}'.format(armorClassList)))
		if choice > 0 and choice < 6:
			break
		print("Error! Please type a number between 1 - 5.\n")
	except Exception:
		print("Error! Please type a number between 1 - 5.\n")

if choice == 1:
	armorClass = 'Rare'
elif choice == 2:
	armorClass = 'Epic'
elif choice == 3:
	armorClass = 'Unique'
elif choice == 4:
	armorClass = 'Diamond'
elif choice == 5:
	armorClass = 'Legendary'

armorPrice = int(input('What is the armor Price?\n> '))
armorDescription = input('Please Describe this armor.\n> ')
armorATK = int(input('How much ATTACK does this armor gives?\n> '))
armorDEF = int(input('How much DEFFENCE does this armor gives?\n> '))
armorLUK = int(input('How much LUK does this armor gives?\n> '))
armorCRT = int(input('How much CRITICAL does this armor gives?\n> '))

data = {}
data['Name'] = armorName
data['Class'] = armorClass
data['Price'] = armorPrice
data['Description'] = armorDescription
data['ATK'] = armorATK
data['DEF'] = armorDEF
data['LUK'] = armorLUK
data['CRT'] = armorCRT

with open(filePATH) as feedJson:
	feeds = json.load(feedJson)

feeds.append(data)

with open(filePATH, 'w') as outfile:
	json.dump(feeds, outfile)

print('armor \'{0}\' added successfully!'.format(armorName))