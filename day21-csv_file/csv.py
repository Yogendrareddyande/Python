# CSV stands for Comma-Separated Values,

# import csv

# import os



# os.chdir('\\Users\\yogi\\OneDrive\\Desktop\\python')
# print(os.getcwd())

import csv
import os

# Always use the absolute path to the file


with open('EMp', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        print(row)

# L,append