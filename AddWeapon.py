import json
from pathlib import Path
from Banner import Banner
#######################################################################
Banner.printBanner()
#######################################################################

filePATH = './.game/weapons.json'

myFile = Path(filePATH)
if not myFile.is_file():
	print("Initial file established!\n>")
	with open(filePATH, 'w') as outfile:
		json.dump([], outfile)

weaponName = ""
weaponClass = ""
weaponPrice = 0
weaponDescription = ""
weaponATK = 0
weaponDEF = 0
weaponLUK = 0
weaponCRT = 0

choice = 0

weaponName = input('What is the Weapon name?\n> ')
if weaponName is '':
	while True:
		weaponName = input('Please Enter Weapon name\n> ')
		if weaponName is not '':
			break
weaponClassList = "1. Rare\n2. Epic\n3. Unique\n4. Diamond\n5. Legendary\nPlease Enter a number!\n> "
print('My name is GM.Shawnkoon!')
while True:
	try:
		choice = int(input('What kind of Class is this?\n\n{0}'.format(weaponClassList)))
		if choice > 0 and choice < 6:
			break
		print("Error! Please type a number between 1 - 5.\n")
	except Exception:
		print("Error! Please type a number between 1 - 5.\n")

if choice == 1:
	weaponClass = 'Rare'
elif choice == 2:
	weaponClass = 'Epic'
elif choice == 3:
	weaponClass = 'Unique'
elif choice == 4:
	weaponClass = 'Diamond'
elif choice == 5:
	weaponClass = 'Legendary'

weaponPrice = int(input('What is the Weapon Price?\n> '))
weaponDescription = input('Please Describe this weapon.\n> ')
weaponATK = int(input('How much ATTACK does this weapon gives?\n> '))
weaponDEF = int(input('How much DEFFENCE does this weapon gives?\n> '))
weaponLUK = int(input('How much LUK does this weapon gives?\n> '))
weaponCRT = int(input('How much CRITICAL does this weapon gives?\n> '))

data = {}
data['Name'] = weaponName
data['Class'] = weaponClass
data['Price'] = weaponPrice
data['Description'] = weaponDescription
data['ATK'] = weaponATK
data['DEF'] = weaponDEF
data['LUK'] = weaponLUK
data['CRT'] = weaponCRT

with open(filePATH) as feedJson:
	feeds = json.load(feedJson)

feeds.append(data)

with open(filePATH, 'w') as outfile:
	json.dump(feeds, outfile)

print('Weapon \'{0}\' added successfully!'.format(weaponName))