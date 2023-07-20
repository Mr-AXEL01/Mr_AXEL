import random
user_input =input("if you are ready choose : rock , paper , scissors \n ")
computer_input = random.choice(['rock','paper','scissors'])
if user_input == computer_input :
    print("it's a tie , everybodyb win")
elif user_input=="rock" and computer_input=="paper" or user_input=="paper" and computer_input=="scissors" or user_input=="scissors" and computer_input=="rock" :
    print("unlucky , next time my friend")
elif user_input=="rock" and computer_input=="scissors" or user_input=="paper" and computer_input=="rock" or user_input=="scissors" and computer_input=="paper":
    print('we have a winner,congratulations')
else :
    print("that not an accepted choice . \n try again from the suggest list")