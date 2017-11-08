# encodding=UTF-8

class ShortInpitException(Exception):
	"""一个由用户定义的一场类"""
	def __init__(self,length,atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	text = input('Enter something -->')
	if len(text) < 3:
		raise ShortInpitException(len(text),3)
	#其他工作能在此处继续正常运行
except EOFError:
	print('Why did you do an EOF on me?')
except ShortInpitException as ex:
	print(('ShortInputException: The input was ' + '{0} long,\
expected at least {1}').format(ex.length,ex.atleast))
else:
	print('No exception was raised')