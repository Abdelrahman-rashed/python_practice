import os 
import math
import sys
import re
import random


def isvowel(s):
	v = list("AEIOU")

	if s in v:
		return True
	else: return False

def minion_game(string):
	vowel_list = []
	constant_list = []
	for a in string:
		if (isvowel(a) == True):
			if (a not in vowel_list):
				vowel_list.append(a)
		else:
			if(a not in constant_list):
				constant_list.append(a)
	#print('vowel_list = ', vowel_list )
	#print('constant_list = ', constant_list)

	#print('Length of vowel list', len(vowel_list))
	#print('Length of constant list', len(constant_list))

	## Vowels ... Kevin ...#

	## Now we get the vowels and constants separated
	## Counting words for kevin .. 
	## Create occurrance list
	## vowel_list = ['A']
	## Create counter list for Each element in vowel list

	occurrance_counter_for_vowel_characters = []
	vowel_compinations = []
	i = 0
	j = 0
	k = 0
	counter = 0

	vowel_compinations_counter = 0

	string_in_list_form =list(string)
	#print('string_in_list_form', string_in_list_form)
	for i in range(len(vowel_list)):
		for j in range(len(string_in_list_form)):
			if(vowel_list[i] == string_in_list_form[j]):
				#counter +=1
				#vowel_compinations_counter +=1
				# from this position till the end 
				#vowel_compinations.append(string_in_list_form[j])
				k = j
				while( k <= len(string_in_list_form) - 1):
					vowel_compinations_counter +=1
					k+=1

				#while(k <= (len(string_in_list_form) -1)):
					#vowel_compinations.append(str(string_in_list_form[k]) +  str(string_in_list_form[k+m]) )
					#m +=1
		occurrance_counter_for_vowel_characters.append(counter)
	
	#print(occurrance_counter_for_vowel_characters)
	#print(vowel_compinations)
	#print('vowel_compinations_counter', vowel_compinations_counter)


	## Constants .. stuart
	constant_compination_counter = 0
	m = 0
	n = 0
	l = 0
	for m in range(len(constant_list)):
		for n in range(len(string_in_list_form)):
			if(constant_list[m] == string_in_list_form[n]):
				l = n
				while( l <= len(string_in_list_form) - 1):
					constant_compination_counter +=1
					l +=1
	#print('Constant_compinations_counter',constant_compination_counter)

	if (constant_compination_counter > vowel_compinations_counter):
		print('Stuart',constant_compination_counter)
	elif (constant_compination_counter < vowel_compinations_counter):
		print('Kevin', vowel_compinations_counter )
	else:
		print('Draw')

test_string = 'BANANA'
minion_game(test_string)