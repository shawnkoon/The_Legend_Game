class Banner:
	'prints the banner about legend'
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
		print(Banner.bannerText)