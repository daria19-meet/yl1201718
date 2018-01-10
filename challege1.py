c=0

for i in range (1000):
	a= i %3
	b= i % 5
	#print("i: " + str(i) + " a: " + str(a))
	if a== 0 or b==0:
		c= c+i
print(c)

#fibonacci:

d=1
e=2
f=1
g=0
while e<4000000:
	if e%2==0:
		g=g+e
		print(g)
	f=d
	d=e
	e=e+f