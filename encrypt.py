import sys
from string import *
'''
Usage:
python3 encrypt.py word_to_encrypt first_coeficient second_coefient show_details 0:no details 1:all

Example:
python3 encrypt.py helloworld 5 4 0
a must be odd
'''
try:
	mot,a,b,show = sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
	if a % 2 == 0:
		raise ValueError('first_coeficient must be odd')
except IndexError:
	print('Wrong usage : read the code for details')
	
dico = dict((zip(ascii_lowercase,range(0,27))))
letter_list = list(ascii_lowercase)
new_word = []
for i in mot:
	index = letter_list.index(i)
	new_index = range(0,27).index(((index * a) + b) % len(letter_list))
	new_letter = letter_list[new_index]
	if show == 1:
		print(i,'=',index,' --> decalage --> ',new_index,'=',new_letter)
	new_word.append(new_letter)
res = ''.join(new_word)
if show == 0:
	print(res)