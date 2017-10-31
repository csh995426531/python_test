while True:
	s = input('请输入文字');
	if s == 'exit':
		break
	else:
		print('文字长度为：',len(s))
print('Done')


array = list(range(1,100,3))
for aa in array:
	print(aa)
	aa = aa+1
print('Done')
