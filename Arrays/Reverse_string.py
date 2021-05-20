string = 'Hi, my name is Mike.'

def reverse_string1(string):
	if not string or len(string) < 2 or not isinstance(string, str):
		raise ValueError('Input must be a string.')
	return string[::-1]

def reverse_string2(string):
	if not string or len(string) < 2 or not isinstance(string, str):
		raise ValueError('Input must be a string.')
	return ''.join(reversed([l for l in string]))

