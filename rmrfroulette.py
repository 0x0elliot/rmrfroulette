import os
import random

remove_command='sudo rm -rf/'

print('''
WELCOME TO rm rf/* ROULETTE

PLEASE 

How to play:
1. Make your friend who has a linux as well run this script with you
2. The script would randomly decide if you would be rm rf/* 'ed
3. The one who survives, Wins. There are 6 max rounds.

''')

user_rights= os.geteuid()
if(user_rights==0):
	pass
else:
	print('Run the script as root dummy')
	quit()
input('\nPress enter to start.')

for i in range(3):
	fate= random.randrange(2)
	if(fate==0):
		print('You got lucky today..')
		input('Press enter to continue..')
		a='Looks like you have successfully won which is kinda weird.'
	elif(fate==1):
		print('Unfortunately, Your luck wasn\'t too good today.')
		os.system(remove_command)
		a='RIP'
print(a)
