def get_num_employees():
    return int(input('Enter the number of Employees :'))

number = get_num_employees()

ages = []
for i in range(number):
    age = int(input(f'Enter the age of Employees {i + 1}: '))
    ages.append(age)

agetotal = sum(ages)

print(f'Total age : {agetotal}')
print(f'Average age : {round(agetotal / number)}')
       


