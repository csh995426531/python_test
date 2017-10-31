number = 20
guess = int(input('enter an integer'))

if guess == number:
	print('等于 \
	对吧')
elif guess < number:
	print('小于')
else:
	print('大于')

print('Done')