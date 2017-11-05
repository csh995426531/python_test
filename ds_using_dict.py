ab = {
	'aa':'啊啊啊啊',
	'bb':'背背背背吧',
	'cc':'痴痴痴痴猜'
}

print("aa's address is",ab['aa'])

del ab['aa']

print('\nThere are{} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
	print('Contact {} at {}'.format(name,address))

ab['dd'] = '的点点滴滴打'

if 'dd' in ab:
	print("\ndd's address is",ab['dd'])