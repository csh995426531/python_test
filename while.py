number = 23
running = True
print('猜数字游戏\n开始：')
guess = int(input('输入一个数字'))
while running:
	guess = int(input('请再次输入'))
	if guess == number:
		print('你猜对了')
		running = False
	elif guess < number:
		print('你猜小了')
	else:
		print('你猜大了')
else:
	print('游戏结束')