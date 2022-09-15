salary = [['Alice', 'Data Scientist', 122000],
          ['Bob', 'Engineer', 77000],
          ['Ann', 'Manager', 119000]]

# Method 1
import csv
with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(salary)



salary = [['Alice', 'Data Scientist', 122000],
          ['Bob', 'Engineer', 77000],
          ['Ann', 'Manager', 119000]]

# Method 2
import pandas as pd
df = pd.DataFrame(salary)
df.to_csv('file2.csv', index=False, header=False)


