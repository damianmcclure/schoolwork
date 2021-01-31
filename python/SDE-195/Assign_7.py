file = open("color.txt").readlines()

colors = {}
# I used a dictionary so I don't have to define a bunch of variables

for line in file:
	color = line.strip()
	try:
		colors[color] = colors[color]+1
	except:
		colors[color] = 1

count = open("colorcount.txt", "w")
for color in colors:
	count.write(color.capitalize() + " " + str(colors[color])+"\n")

count.close()
