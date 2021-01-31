try:
	sum = 0
	for i in range(5):
		tmp = input("Enter number "+str(i+1)+": ")
		if (int(tmp) % 2) == 0: 
			print(tmp+" is even")
		else: 
			print(tmp+" is odd")
		sum = int(tmp)+sum
	print("Total of all numbers is "+str(sum))
except:
	print("invalid input, error")
