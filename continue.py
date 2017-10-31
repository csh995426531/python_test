while True:
	ss = input('请输入退出命令')
	if ss == 'exit':
		print('Done')
		break
	elif len(ss)<4:
		print('太短')
		continue
	elif len(ss)>4:
		print('太长')
		continue
	print('命令错误')