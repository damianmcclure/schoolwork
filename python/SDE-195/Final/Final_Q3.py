import matplotlib.pyplot as plt

labels = 'Quizzes', 'Exercises', 'Assignments', 'Projects', 'Final Exam'
sizes = [1, 2, 2, 3, 2]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')

plt.savefig('finalq3data.png')
