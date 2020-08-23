# Dianna Xu
# Class 110A - Hw 7
# You can play the game, "Rock, paper, scissors".

def rps(computer, user):
  if user == computer:
    print("Tie")
  elif user == "rock" or "rocks":
    if computer == "paper":
      print("Computer wins! Paper covers rock!")
    else:
      print("You win! Rock smashes scissors!")
  
  elif user == "paper" or "papers":
    if computer == "scissors":
      print("Computer wins! Scissors cuts paper!")
    else:
      print("You win! Paper covers rock!")

  elif user == "scissors" or "scissor":
    if computer == "rock":
      print("Computer wins! Rock smashes scissors!")
    else:
      print("You win! Scissor cuts paper")

def main():
  import random
    
  computer_choice = ["rock", "paper", "scissors"]

  user = input("Please enter your move: Rock, paper or scissors? ")
  user = user.lower()
  computer = random.choice(computer_choice)
  print("Computer's move is", computer)

  rps(computer, user)
  

if __name__ == "__main__":
  main()


    

'''
Please enter your move: Paper, Rock, or Scissors: Paper
Computer's move is Paper
Tie with Paper!


Please enter your move: Paper, Rock, or Scissors: paper
Computer's move is Scissors
Computer Wins! Scissors cut Paper!!


Please enter your move: Paper, Rock, or Scissors: scissors
Computer's move is Scissors
Tie with Scissors!

'''