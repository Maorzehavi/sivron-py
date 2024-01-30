


import pandas as pd
import os
import matplotlib.pyplot as plt
from pprint import PrettyPrinter

printer = PrettyPrinter()

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))



# read the dataset
df = pd.read_csv('salaries.csv')
printer.pprint(df.head())
print(f"There are {len(df)} data in the dataset.")

# amount of data records per column
count = df.count()
print(f"There is {len(count)} columns in the dataset.")
printer.pprint(count)
print(df.keys())

#  # Check for missing values
print(df.isnull().sum())

# Histogram for salary distribution
df['salary_in_usd'].hist()
plt.title('Salary Distribution')
plt.xlabel('Salary in USD')
plt.ylabel('Frequency')
plt.show()

# Histogram for experience distribution
df['experience_level'].hist()
plt.title('Experience Distribution')
plt.xlabel('Experience')
plt.ylabel('Frequency')
plt.show()

# Histogram for work model distribution
df['work_models'].hist()
plt.title('Work Model Distribution')
plt.xlabel('Work Model')
plt.ylabel('Frequency')
plt.show()

# Histogram for work year distribution
df['work_year'].hist()
plt.title('Work Year Distribution')
plt.xlabel('Work Year')
plt.ylabel('Frequency')
plt.show()

# Histogram for company size distribution
df['company_size'].hist()
plt.title('Company Size Distribution')
plt.xlabel('Company Size')
plt.ylabel('Frequency')
plt.show()

# Histogram for company location distribution
df['company_location'].hist()
plt.title('Company Location Distribution')
plt.xlabel('Company Location')
plt.ylabel('Frequency')
plt.show()

# Histogram for company location distribution
usa_emps = df[df['company_location'] == 'United States']
print(f"There are {len(usa_emps)} employees in the USA.")
usa_emps['company_size'].hist()
plt.title('Company Size Distribution in the USA')
plt.xlabel('Company Size')
plt.ylabel('Frequency')
plt.show()

# Histogram for company location distribution
usa_comp = df[df['company_location'] == 'United States']
print(f"There are {len(usa_comp)} companies in the USA.")
usa_comp['company_size'].hist()
plt.title('Company Size Distribution in the USA')
plt.xlabel('Company Size')
plt.ylabel('Frequency')
plt.show()

# total salary in the USA
total_salary = usa_emps['salary_in_usd'].sum()
print(f"The total salary in the USA is {total_salary}.")
# average salary in the USA
avg_salary = int(usa_emps['salary_in_usd'].mean())
print(f"The average salary in the USA is {avg_salary}.")
# median salary in the USA
median_salary = usa_emps['salary_in_usd'].median()
print(f"The median salary in the USA is {median_salary}.")
# minimum salary in the USA
min_salary = usa_emps['salary_in_usd'].min()
print(f"The minimum salary in the USA is {min_salary}.")
# maximum salary in the USA
max_salary = usa_emps['salary_in_usd'].max()
print(f"The maximum salary in the USA is {max_salary}.")










