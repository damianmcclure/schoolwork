# Dictionary of operator names and their symbols
operators = {
	"addition": "+",
	"subtraction": "-",
	"multiplication": "*",
	"division": "/",
	"percentage": "%",
	"exponent": "**" # In python exponent requires ** instead of ^
}

# Function used to calculate
def Calculate(num1, num2, operator):
	if operator in operators:
		answer = eval(str(num1) + operators[operator] + str(num2))
		return answer
	else:
		return "This is not a valid operation"

print("This program will calculate 2 numbers with your choice of operator.")
# Prints all the available operators
for operator in operators:
    print(operator)

f = open("answers.txt", "a")
# This will loop forever until the code breaks it
while True:
    operator = input("\nWhat operator do you want to use? (Type exit to quit) ")
	# Exits the program if they type exit
    if operator == "exit":
        break

    num1 = input("Type your first number ")
    num2 = input("Type your second number ")

	# Just in case user enters invalid input
    try:
        answer = Calculate(num1, num2, operator)
        print(str(num1)+" "+operators[operator]+" "+str(num2)+" = "+str(answer))
        f.write(str(num1)+" "+operators[operator]+" "+str(num2)+" = "+str(answer)+"\n")
    except:
        print("Input is not valid, error")

f.close()
