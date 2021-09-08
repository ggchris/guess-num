import random
r=random.randint(1,100)
count=0
while True:
	count+=1
	num=input("number:")
	num=int(num)
	if num==r:
		print("got it!")
		break
	elif num>r:
		print("smaller")
	elif num<r:
	 	print("bigger")
	print("count:",count)

