usernames = ["bob123", "bammiller", "comfychowder", "cruxhawk", "fibblelagging"]
passwords = ["password123", "TnkSyU9k", "sxSQg8Pn", "yWe5AGGT", "tbkrbLa5"]

username = input("Username: ")
password = input("Password: ")

count = 0
loggedin = False

for name in usernames:
	if username == name:
		if password == passwords[count]:
			loggedin = True

if loggedin:
	print("Logged in as "+username)
else:
	if username in usernames:
		print("Password incorrect")
	else:
		print("User not")
