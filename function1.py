def say_hello():
	print('hello world')


say_hello()
say_hello()




def print_max(a,b,c):
	if a > b:
		if a > c:
			print(a,'最大')
		elif a == c:
			print(a,'和',c,'最大')
		else:
			print(c,'最大')
	else:
		if b > c:
			print(b,'最大')
		elif b == c:
			print(b,'和',c,'最大')
		else:
		 	print(c,'最大')

print('比较数字大小')

a = int(input('第一个数'))
if a :
	b = int(input('第二个数'))
	if b :
		c = int(input('第三个数'))
		if a & b & c :
			print_max(a,b,c)

