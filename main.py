import random

# Game images 
rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Player side RPS choice
print("Welcome to Rock, Paper, Scissors!
       Can you beat the computer? ")
player = int(input("Type 0 for rock, 1 for paper, 
                    and 2 for scissors. \n"))

# Check if the input is valid. 
# Nonvalid input doesn't print game images. 
if player >= 3 or player < 0:
    print(f"{player} is a invalid number, so you lose!")
else:
    game_images = [rock, paper, scissors]

    if player == 0:
        print(f"{rock}")
    elif player == 1:
        print(f"{paper}")  
    else:
        print(f"{scissors}")

    # Computer side RPS choice
    r_p_s = [0, 1, 2]
    computer = random.choice(r_p_s)

    print("Computer choose: ")

    if computer == 0:
        print(f"{rock}")
    elif computer == 1:
        print(f"{paper}")
    else:
        print(f"{scissors}")

    # Rock choices
    if player == 0 and computer == 0:
        print("It's a tie. ")
    elif player == 0 and computer == 1:
        print("You lose. Paper beats Rock. ")
    elif player == 0 and computer == 2:
        print("You win! Rock beats Scissors! ")

    # Paper choices
    if player == 1 and computer == 0:
        print("You win! Paper beats Rock! ")
    elif player == 1 and computer == 1:
        print("It's a tie. ")
    elif player == 1 and computer == 2:
        print("You lose. Scissors beat Paper. ")

    # Scissors choices
    if player == 2 and computer == 0:
        print("You lose. Rock beats Scissors. ")
    elif player == 2 and computer == 1:
        print("You win! Scissors beat Paper! ")
    elif player == 2 and computer == 2:
        print("It's a tie. ")
