from os import system
from time import sleep

def rctousd():
	print('=' * 5, 'RC to USD', '=' * 5, '\n')
	try:
		playerrc = int(input('How much RC do you want to convert to U$..: '))
	except ValueError:
		print('\nPlease, use only numbers. \n\nRestarting RC to USD')
		sleep(2.0)
		system('cls')
		rctousd()
	else:
		firstcalc = (playerrc / 6.35) / 100
		print('\n{:.0f} RC is qual to U${:.2f}'.format(playerrc, firstcalc))
		input('\nPress enter to start the software again')
		system('cls')
		start()

def usdtorc():
	print('=' * 5, 'USD to RC', '=' * 5, '\n')
	try:
		playerus = input('How much U$ do you want to convert to RC..: ')
	except ValueError:
		print('\nPlease, use only numbers. \n\nRestarting USD to RC')
		sleep(2.0)
		system('cls')
		usdtorc()
	else:
		seccalc = (playerus * 6.35) * 100
		print('\nU${:.2f} is equal to {:.0f} RC'.format(playerus, seccalc))
		input('\nPress enter to start the software again')
		system('cls')
		start()

def start():
	print('Welcome, this is a simple software to convert RC to U$ or U$ to RC.')
	sleep(0.8)
	print('SELECT\n')
	print('1 for RC to U$ \n2 for U$ to RC \n3 to Exit')
	selector = input('\nSelect..: ')
	if selector == '1':
		system('cls')
		rctousd()
	elif selector == '2':
		system('cls')
		usdtorc()
	elif selector == '3':
		exit()
	else:
		print('\nPlease, select 1 or 2 or 3 To Exit.')
		sleep(1.8)
		system('cls')
		start()

start()
