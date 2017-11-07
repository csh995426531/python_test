import re
def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)

someth_temp = input('enter 文字:')

r = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'

something = re.sub(r,'',someth_temp)

if is_palindrome(something):
	print("Yes, it is a palindrome")
else:
	print("No, it is not a palindrome")