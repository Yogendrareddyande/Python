# CSV stands for Comma-Separated Values,

import csv

import os



os.chdir('\\Users\\yogi\\OneDrive\\Desktop\\python')
print(os.getcwd())


# Always use the absolute path to the file
# Read ()
# import csv

# with open("employees.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# L,append

'''
with open("employees.csv", "w") as file:
    file.write("ID,Name,Age,Department,Salary\n")
    file.write("1,Yogi Reddy,23,IT,45000\n")
    file.write("2,Anjali,25,HR,40000\n")
    file.write("3,Ravi Kumar,28,Finance,52000\n")
    file.write("4,Sneha,24,Marketing,48000\n")
    file.write("5,Arjun,26,IT,50000\n")
    file.write("6,Meena,27,Admin,43000\n")
    file.write("7,Vikram,29,Sales,55000\n")
    file.write("8,Kiran,30,Finance,60000\n")
    file.write("9,Deepa,22,Support,41000\n")
    file.write("10,Sravan,31,Manager,65000\n")

print("✅ employees.csv file created successfully!")
'''
