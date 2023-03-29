import random


while True:
    comp_guess = random.randint(0,2)
    user_guess = input("Input rock/paper/scissor or q to quit: ").lower()
    if user_guess == "q":
        quit()
    elif user_guess in ["rock", "paper", "scissor"]:
        if user_guess == "rock" and comp_guess == 2:
            print("Win, hit the scissor with your rock")
            continue
        elif user_guess == "paper" and comp_guess == 0:
            print("Win, covered the rock with your paper")
            continue
        elif user_guess == "scissor" and comp_guess == 1:
            print("Win, cut the paper with your scissor")
            continue
        elif user_guess == "rock" and comp_guess == 0:
            print("What a tie!!!")
            continue
        elif user_guess == "paper" and comp_guess == 1:
            print("What a tie!!!")
            continue
        elif user_guess == "scissor" and comp_guess == 2:
            print("What a tie!!!")
            continue
        else:
            print ("you lose ......sucker")
            continue
    else:
        print("Fill in the appropriate data next time")
        continue
