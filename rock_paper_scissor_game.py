import random
print("Welcome to Rock, Paper, Scissors!\nPLease enter '0' for Rock, '1' for Paper, and '2' for Scissors.")
user_choice = int(input("Player 1, enter your choice: "))
computer = random.randint(0, 2)
rock = '''
ROCK
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
SCISSORS
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
choices = [rock, paper, scissors]
print(f"user choose : \n{choices[user_choice]}")
if user_choice == 0 and computer == 2 :
    print(f"computer choose : \n{scissors}")
    print("You wins!")
elif user_choice == 2 and computer == 0 :
    print(f"computer choose : \n{scissors}")
    print("You Lose!")
elif user_choice > computer:
    print(f"computer choose : \n{choices[computer]}")
    print("YOU WIN!")
elif user_choice == computer :
    print("It's a draw!. \nTry again!")
elif user_choice not in [0,1,2]:
    print("Invalid input. Try again!")
input()
# if user_choice == 0 and computer == 2:
#     print(f"Player 1 chose:\n{rock}")
#     print(f"Computer chose:\n{scissors}")
#     print("Player 1 wins!")
# elif user_choice == 1 and computer == 0:
#     print(f"player 1 choses: \n {paper} ")
#     print(f"computer choses: \n {rock}")
#     print("player 1 wins!")
# elif user_choice == 2 and computer == 1 :
#     print(f"player 1 chooses : \n {scissors}")
#     print(f"computer chooses : \n {paper}")
#     print("user_choice wins!")
# elif user_choice == computer:
#     print("It's a draw!")
# else: 
#     print("Computer Wins!")
#     if computer == 0:
#         print(f"Computer chose:\n{rock}")
#     elif computer == 1:
#         print(f"Computer chose:\n{paper}")
#     elif computer == 2:
#         print(f"Computer chose:\n{scissors}")
# input()
