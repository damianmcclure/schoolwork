import pandas as pd
import matplotlib.pyplot as plt

# I chose the degree type data set. It is in a file called data.csv
df = pd.read_csv('data.csv', encoding="utf-8-sig", index_col=0) # Index column set to 0 so it makes the first column the names of the rows.

# I chose bar graph
df.plot(kind='bar')

# Without rotation=0, it will have the text off-screen.
plt.xticks(rotation=0, fontsize=8)

# Save the file as data.png
plt.savefig('data.png')
