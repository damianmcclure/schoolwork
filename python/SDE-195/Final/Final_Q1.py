courses = {
    "Engl-110": "Lisa Wood",
    "IT-269": "Anthony Brittingham",
    "IT-244": "Robert Ball",
    "CYBR-192": "Kay Ogilvie",
    "CYBR-210": "Tatyana Zidarov",
    "SDE-195": "Kim Graves"
}

f = open("courses.txt", "w")
for i in courses:
    f.write(i+", "+courses[i]+"\n")
f.close()
