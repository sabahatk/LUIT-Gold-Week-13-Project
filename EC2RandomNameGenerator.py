import random

numOfEc2 = int(input('Enter the amount of EC2 instances that you need names for: '))
department = input('Please enter your department: ')

#Loop through a number of times as specified in numOfEc2
for x in range(numOfEc2):
    randomName = ''
    randomChoiceSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    randomChars = random.choice(randomChoiceSet)

    #Generate 5 random characters
    for i in range(5):
        randomChars+=random.choice(randomChoiceSet)

    randomName = department + randomChars
    print(randomName)
