import random
top_of_range = input("Input a maximum number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please fill in relevant datatype needed next time.")
        quit()
else:
    print("Fill in relevant data type next time")
    quit()

number_of_guesses = 0
random_guess = random.randint(0, top_of_range)



while (True): # i.e if guess != random_guess. if written like this, need to change 
    # how you wrote while loop accordingly.
    number_of_guesses += 1

    guess = input("Fill  in guess number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Fill in relevant data type next time")
        quit()

    
    if guess == random_guess:
        print("Got it right, genius.")
        break
    elif guess < random_guess:
        print("Your guess kinda lower.....")
        continue
    else:
        print("Your guess kinda upper.....")
        continue

print(" You have guessed", number_of_guesses, "times.")