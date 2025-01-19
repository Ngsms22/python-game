# rock beats scissors
# scissors beats paper
# paper beats rock
# random.choice()

import random
print("welcome to the game!: \n")
print("rules:rock beats scissors, scissors beats paper, paper beats rock")
print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit the game.")

rock_picture='''
Rock
          _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)


'''

paper_picture = '''
 Paper
          _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)

'''

scissors_picture = '''

 Scissors
          _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)


'''

pictures=[rock_picture, paper_picture, scissors_picture]
choices = ["rock","paper","scissors"]

decision="play"
while decision=="play":
    players_choice = input("which one are you going for(rock,paper or scissors):\n ").lower()
    index_players_choice=choices.index(players_choice)
    print(pictures[index_players_choice])
     

    if players_choice not in choices:
        print("wrong input, chose from the given options.")


    
    computers_choice = random.choice(choices)

    index_computers_choice=choices.index(computers_choice)
    print(pictures[index_computers_choice])
    print(f"Computer's choice is: {computers_choice}")


    if players_choice == computers_choice:
        print("It's a tie.")
    elif (players_choice == "rock" and computers_choice == "scissors") or \
        (players_choice == "scissors" and computers_choice == "paper") or \
        (players_choice == "paper" and computers_choice == "rock"):
      print("You win!")
    else:
        print("Computer wins!")

        print("_______________________")  # Add a blank line for better readability
    decision=input("enter 'play' to play again or enter 'quit' to stop: ")
if decision== "quit":
    print("we go again some other time. Goodbye.")