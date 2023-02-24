import random, os
from art import draw

choices = ["rock","paper","scissors"]

def determine_winner(player, opp):
   # Check if its a tie
   if player == opp:
      return("It's a tie game!")
   # Check if the player won
   elif ((player == "rock" and opp == "scissors") or
         (player == "paper" and opp == "rock") or
          (player == "scissors" and opp == "paper") ):
            return ("You won, congratulation!")
   
   # If they did not win, then we know they lost
   else:
       return ("You lost, sorry!")
   
playing, invalid = True, False


while playing:
    # Where you ask the player to make a selection
    # also this is where you let them know if their previous choice was invalid
    if not invalid:
      print("Choose rock, paper or scissors")
    else:
      print("Invalid input, please type rock, paper or scissors")
      invalid = False
    print("Or enter q to quit")

# Where I store results into a variable
# This gets player input and makes it lowercase and removes whitespace 

    player_choice = input().lower().strip()

# This generates a random choice for the computer opponent 
    opp_choice = random.choice(choices)

# Where it checks and sees if the player choice is a valid entry

    if player_choice in choices:
        print(" You chose:  "+ player_choice + draw(player_choice))
        print(" The opponent chose:  " + opp_choice + draw(opp_choice))
        print(determine_winner(player_choice, opp_choice))

# Where the loop ends if the player wants to leave

    elif player_choice == 'q':
        playing = False

    else:
        invalid = True

    # The iteration of the game is done, ask if you want to play the game again
    if playing and not invalid:
        replay = input("Do you want to play again?\nType \"yes\" to replay\nEnter anything else to end the game\n").lower().strip()
        print()
        playing = replay == "yes"

    # This clears the screen 
    os.system('cls' if os.name == 'nt' else 'clear')

print("Thank you for playing my game!")