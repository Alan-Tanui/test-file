import sys

def get_num_employees():
    return int(input('Enter the number of Employees :'))

number = get_num_employees()

if number < 0 :
    print('Please Enter a Valid Number!!')

else :
    ages = []
    for i in range(number):
        age = int(input(f'Enter the age of Employees {i + 1}: '))
        ages.append(age)
   

    agetotal = sum(ages)

    names = []
    for i in range(number):
        name = str(input('Enter the Names of the Employees :')).strip().title()
        names.append(name)

    print('\n ---Employee Details ---')     
    for i in range(number):
        print(f'Name : {names[i]} -- Age {ages[i]}')

    print('\n --- Statistics ---')
    print(f'Total number of Employees : {number}') 
    print(f'Total age : {agetotal}')
    print(f'Average age : {round(agetotal / number)}')
 


