import random
print("WELCOME TO GUESS THE NUMBER GAME")
num = random.randint(1,100)
itr = 0
check = -1
while(check == -1):

    guess = int(input("Guess a number"))
    itr = itr + 1
    if(guess == num):
        print(f"You guessed correct number which is {guess}")
        check+= 1
    elif(guess > num):
        print(f"Number is less then {guess}")

    elif(guess < num):
        print(f"Number is greater then {guess}")    

print(f"your total number of guesses are {itr}")

# no frontend is present , it will be created in future !!