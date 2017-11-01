def print_max(x,y):
	''' 打印两个数值之间最大的那个

		如果可以，这两个值都应该是整数'''
	x = int(x)
	y = int(y)
	if x > y :
		print(x,'is maxnnmber') 
	elif x <y :
		print(y,'is maxnumber')
	else :
		print(x,'等于',y)
		''' aaaaa'''

print_max(5,6);
print(print_max.__doc__)
# help(print_max)