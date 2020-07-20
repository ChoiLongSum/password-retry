
password = 'a123456'
x = 3
while True:
	trial = input('Please input password:')
	if trial == password:
		print('Correct password, login success')
		break
	elif x == 1:
		print('You inputted the wrong password 3 times, login fail!')
		break
	elif trial != password:
		x = x - 1
		print('Wrong password!', x,'trials left!')

