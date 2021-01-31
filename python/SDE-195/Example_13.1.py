import re

f = open("regex_sum_919036.txt")

text = f.read()
numbers = re.findall('[0-9]+', text)

sum = 0
for num in numbers:
    sum = sum + int(num)

print(sum)
