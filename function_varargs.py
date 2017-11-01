def total(a=5,*numbers,**phonebook):
	print('a is',a)

	for number in numbers:
		print('number is',number)

	for phone,book in phonebook.items():
		print(phone,'is',book)


print(total(10,1,3,5,6,Jack=1123,John=2231,Inge=1560))