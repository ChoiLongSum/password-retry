
password = 'a123456'
x = 3
while x > 0:
	trial = input('Please input password:')
	if trial == password:
		print('Correct password, login success')
		break
	elif trial != password:
		x = x - 1
		print('Wrong password!', x,'trials left!')

