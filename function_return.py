def maximum(x,y):
	if x > y:
		return x
	elif x == y:
		return x,'等于',y
	else :
		return y

a = int(input('请输入第一个数'))
if a :
	b = int(input('请输入第二个数'))
	if a and b :
		print(maximum(a,b))