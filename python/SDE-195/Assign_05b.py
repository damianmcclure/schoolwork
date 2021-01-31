try:
	number = input("Enter a number between 1 and 10 to see its multiples: ")
	if int(number) <= 10:
		for i in range(100):
			num = int(number)*(i+1)
			if num > 100:
				break;
			print(num)
	else:
		print("Number cannot be bigger than 10, error")
except:
	print("Invalid input, error")
