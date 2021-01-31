def myemail(fname, lname):
	tmp1 = fname[:1].lower()
	tmp2 = lname[:5].lower()
	return tmp1+tmp2+"01@my.blueridgectc.edu"

print(myemail("Amelia", "Earhart"))
