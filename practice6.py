text = raw_input('input message: ')

text1 = text
text2 = text[::-1]

if text1 == text2 :
	print 'same'

else :
	print 'different'