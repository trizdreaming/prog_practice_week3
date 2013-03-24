def convert(x) :
	if 0 < x < 10:
		x = x + 10
		print x
	elif 10 < x < 100:
		x = x *0.1
		print x
	else :
		print 'false'


x = input('input message: ')
convert(x)