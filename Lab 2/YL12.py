# a = [5,7, 10, 13,15, 17,20, 22, 25]
# b= []
# c=input ("What number should I filter?")
# c= int (c)
# for value in a:
# 	if value > c:
# 		b.append(value)
# print (b)

import random 
x= random.randint (10,20)
y= random.randint (10,20)
a=[]
b=[]
c=[]
d=[]
for i in range (x):
	a.append(random.randint(10,20))
for i in range (y): 
	b.append(random.randint(10,20))
for value in a:
	if value in b:
		c.append(value)
		if value in c:
			d.append(value)

				

print(c)

print(d)

	