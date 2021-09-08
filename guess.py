import random
r=random.randint(1,100)
while True:
	num=input("number:")
	num=int(num)
	if num==r:
		print("got it!")
		break
	elif num>r:
		print("smaller")
	elif num<r:
	 	print("bigger")


