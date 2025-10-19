#-------- EXERCISE_1: DICE GAME --------

#long story short I want to try making 6 projects in total from the video below
#https://www.youtube.com/watch?v=yVl_G-F7m8c
#the only rule is that I need to attempt doing the project/exercises without cheating (aka googling the answers)

#created on 18 10 2025
#author: me

#list of things the program must do:
#   ask if user wants dice to be rolled (use input)
#   use if/else command to make sure the user uses y or n
#   randomly generate 2 numbers between 1 and 6
#   close code only if n is selected (hence loop? idk tbh)

#lets import randomness
import random

#then let's start with introduction and input
print("-------- " \
"\n hey fella lets feed that gambling addiction " \
"\n do u wanna roll 2 dices")

answer = input("reply with yes or no (y/n): ")



#also I know there must be nicer way to do this 
#but I'm going to do a list of acceptable answers
y = ["y", "Y","yeah","yep","aye"]
n = ["n","N","no","fuck you"]

# now the if statements
#its gonna be a pain to loop this hellscape

#im using a while condition where as long as the user didn't say no, the game continues
while any(elem in answer for elem in n) == False:

    # if the input string answer contains any of the strings in the y variable, then 2 dices are rolled between 1 and 6
    if any(elem in answer for elem in y) == True:
        ######edit: i've set up the dice in advance
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        ######edit: i've discovered f strings, I'm gonna use them here
        print(f"\n thats my boy \n \n[ {die1} , {die2} ]")
        print ("\n", "another one?")
        answer = input("reply with yes or no (y/n): ")
    else:
        print("\n... \nI didn't understand any of that \n\n"
        "alright one more time ")
        answer = input("reply with yes or no (y/n): ")
        # in the else statement, if the user starts writing gibberish the program will ask for a new input
        #!!!!!!!!!!! *IMPORTANT*: FOR NOW THE INPUT ACCEPTS GIBBERISH CONTAINING y or n INSIDE THE STRING REGARDLESS OF CONTEXT, PLEASE FIX LATER IF POSSIBLE

if any(elem in answer for elem in n) == True:
    print ("\n... \n... \n... \n"\
    "coward"
    "\n" \
    "\n" \
    "----- END OF COMMUNICATION -----")





