import random

#Ask user for input
numOfEc2 = int(input('Enter the amount of EC2 instances that you need names for: '))
#print('Please enter one of the following departments Marketing, Accounting, FinOps:')
department = input('Please enter an eligible department (i.e. Marketing, Accounting, FinOps):')


if (department.lower() == 'marketing') or (department.lower() == 'accounting') or (department.lower() == 'finops'):
    #Loop through a number of times as specified in numOfEc2
    for x in range(numOfEc2):
        randomName = ''
        randomChoiceSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        randomChars = random.choice(randomChoiceSet)

        #Generate 5 random characters
        for i in range(5):
            randomChars+=random.choice(randomChoiceSet)

        randomName = department + randomChars
        if x == 0:
            print()
            print('List of names:')
        print(randomName)
else:
    print('The department you have entered is not eligible to use this Name Generator.')