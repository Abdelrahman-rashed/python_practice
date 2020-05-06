import math 
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split() # strip the inputs with the spaces


n = int(first_multiple_input[0])

m = int(first_multiple_input[1])


matrix = []

for _ in range(n):
	matrix_item = input()
	matrix.append(matrix_item)



# print('m =',m)
# print('n=',n)
# print('\n')	
# print(first_multiple_input)
print('\n')
print('matrix = ',matrix)

# print('\n')
# print(input_shape)

col1 = []
col2 = []
col3 = []

col1_2 = []

whole_string = []

for i in range(len(matrix)):
	col1.append(matrix[i][0])
print(col1)

for j in range(len(matrix)):
	col2.append(matrix[j][1])
print(col2)

for k in range(len(matrix)):
	col3.append(matrix[k][2])
print(col3)

whole_string = col1 + col2 + col3

print(whole_string)

str1 = ""
string = str1.join(whole_string)
print('word_string = ', string)

# p = re.compile('\w+')

# final_word = p.findall(string)
# print('final_word =',final_word )
x, y = map(int, input().split())
a = []
for _ in range(x):
	a.append(input())

print('a=',a)
b = ""
for z in zip(*a):
	b +="".join(z)

print('b=',b) 


print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))