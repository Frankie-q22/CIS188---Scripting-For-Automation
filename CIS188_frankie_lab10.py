
#Your company has set up a new IT system and needs to set random initial passwords for each employee.   
# You have been provided a CSV file, called #employees.csv (attached), with a list of all employees in the company.  
# The list contains first name, last name, phone number and email for each #person.  
# You need to create a new CSV file which contains the first name, last name, email and a new randomly generated password.  

#The function definition for the random password generation, 

#generate random password 
# in the file called CIS188_Lab10_PassGenerator.py (attached), is provided to you.
#The program must:

#utilize the provided function definition to generate random passwords

#read the data from the given CSV file
#create a new CSV file with updated data based on the given file

#Note: if the csv file contains strange characters or doesn't read correctly, 
# open it in a plain text editor like notepad and Save As... 
# select Save type as "All types" and include .csv at the end of the filename. 
# If you continue to have trouble, you may need to open the file in Microsoft Excel or other spreadsheet software 
# and Save As... select Save type as "CSV (Comma delimited) (*.csv)"




#Frankie Quintero
import csv
import PassGenerator as pg

count = 0
# You have been provided a CSV file, called employee.csv, with a list of all employees in the company. 
exampleFile = open('.\employees.csv')
employee_data = list(csv.DictReader(exampleFile))
outputfile = open('Output.csv', 'w', newline="")
outputDictWriter = csv.DictWriter(outputfile,['fname', 'lname', 'email', 'password'])
outputDictWriter.writeheader()
for row in employee_data:
# Call Random Pw gen and create new list with those objects
    password = pg.gen_pass(16)
    # You need to create a new CSV file which contains the first name, last name, email and a new randomly generated password.  
    outputDictWriter.writerow({'fname':row['fname' ] ,'lname':row['lname' ] , 'email':row['email' ] , 'password':password  })
    count += 1

