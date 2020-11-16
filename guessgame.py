#CODED BY SALAHMJ

import random
import colored

n = random.randint(1,10001)
c = colored.fg('green')
r = colored.attr('reset')
v = colored.fg('red')
b = colored.fg('blue')

'''
ONCE YOU GUESS THE NUMBER, PROGRAMME SHOULD END SO USE (BREAK) STATEMENT
'''

while True:
	m = int(input('Enter Your Guess Number: '))
	if m == n:
		print(c , 'YOU HAVE GUESSED IT CORRECTLY!!!' , n , r)
		break
	elif m < n:
		print(v , 'YOUR GUESS IS LOW' , r)
	elif m > n:
		print(b , 'YOUR GUESS IS HIGH' , r)
	else:
		pass
