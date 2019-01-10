#Assignment-2

import random
import time
import os

#Clear the terminal screen (only for windows, for linux and mac use 'Cler' instead of 'cls')
os.system('cls')

#Generate a random integer initially
random_int = random.randint(1, 10)

#Get the input of range 1 - 10 from user
user_input = str(input("Guess a number between 1 & 10 : "))

#Correct the incorrect user inputs untill the integer matches randomly generated value
while (user_input.isnumeric() == False) or (int(user_input) != int(random_int)):
    random_int = random.randint(1, 10)
    if (user_input.isnumeric() == False):
        print ("You have made an invalid entry")
        time.sleep(3) #wait for 3 seconds before clearing the screen
        os.system('cls') #clear the screen
        user_input = str(input("Please enter an appropriate integer within the range 1 - 10 : "))

    elif (int(user_input) not in range(1, 11)):
        print ("The number you have entered is out of range")
        time.sleep(3) #wait for 3 seconds before clearing the screen
        os.system('cls') #clear the screen
        user_input = str(input("Please enter a number within the range 1 - 10 : "))

    elif (int(user_input) != int (random_int)):
        print ("Wrong, try again!")
        time.sleep(3) #wait for 3 seconds before clearing the screen
        os.system('cls') #clear the screen
        user_input = str(input("Guess a number between 1 & 10 again : "))

#Print the output when user input matches the randomly genetated value
print ("Correct!")