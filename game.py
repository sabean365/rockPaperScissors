##Rock Paper Scissors Game
#import random for computer choice
import random
   
#header
print("++++++++++++++++++++++++++++++++++++")
print("Let's play ROCK, PAPER, SCISSORS!")
print("PLAYERS WILL PLAY BEST 3 out of 5.")
print("++++++++++++++++++++++++++++++++++++")

#assign global variables
yes = "y"
no = "n"
player_one = 0
player_two = 0
computer = 0

#Give player(s) choice of 1 or 2
choice_players = input("Type in the number of players (1 or 2): ")
#exception handling
while int(choice_players) != 1 and int(choice_players) != 2:
  choice_players = (input("Please enter 1 or 2"))

#If player is only 1
if int(choice_players) == 1:
  print("You are playing against Botman!")
  #confirm they want to continue
  choice_again = (input("Do you want to continue? Type y or n: ").lower())
  


  #error handling
  while choice_again != yes and choice_again != no:
    choice_again = (input("Please type only y or n: ").lower())

  #while loop for best 3 out of 5
  while choice_again == yes and player_one < 3 and computer < 3 or player_one == computer:    
     #assign variables
    random_list = ['rock', 'paper', 'scissors']

    #assign variables
    rock = "r"
    paper = "p"
    scissors = "s"

    #get user 1 input
    choice1 = (input("You are player 1. Please Enter r for rock, p for paper, s for scissors: "))
    #format choice
    choice_one = choice1.lower()
    #error handling
    while choice_one != rock and choice_one != paper and choice_one != scissors:
      choice_one =  (input("You did not enter a correct letter. Enter r for rock, p for paper, s for scissors: "))
 
    #computer-generated choice using random
    choice_two = random.choice(random_list)
    print(f"Botman chose {choice_two}")

    #calculate results
    if choice_one == rock:
      #user 1 = rock, user 2 = rock
      if choice_two == rock:
        print("You both chose rock. It's a tie!")
        player_one += 1
        computer += 1
          
      #user 1 = rock, user 2 = paper
      elif choice_two == paper:
        print("Paper covers rock. Botman wins!")
        computer += 1
            
      #user 1 = rock, user 2 = scissors
      else:
        print("Rock smashes scissors. You win!")
        player_one +=1
    
    elif choice_one == scissors:
      #user 1 = scissors, user 2 = rock
      if choice_two ==rock:
        print("Rock smashes scissors. Botman wins!")
        computer +=1
      
      #user 1 = scissors, user 2 = paper
      elif choice_two == paper:
        print("Scissors cuts paper. You win!")
        player_one +=1
      #user 1 = scissors, user 2 = scissors
      else:
        print("You both chose scissors. It's a tie!")
        player_one +=1
        computer +=1

    else:
      #user 1 = paper, user 2 = rock
      if choice_two ==rock:
        print("Rock covers paper. You win!")
        player_one +=1

      #user 1 = paper, user 2 = paper
      elif choice_two == paper:
        print("You both chose paper. It's a tie!")
        player_one +=1
        computer +=1

      #user 1 = paper, user 2 = scissors
      else:
        print ("Scissors cuts paper. Botman wins!")
        computer =+1

    #print the score
    print("You have " + str(player_one) + " points.")
    print("Botman has " + str(computer) + " points.")

    #calculate the winner
    if player_one > computer:
      print("You are the winner!")
    elif player_one < computer:
      print("Botman is the winner!")
    else:
        print("It's a tie!")
    
    #prompt to play again
    choice_again = (input("Do you want to continue: type y or n ").lower())
    while choice_again != yes and choice_again != no:
        choice_again = (input("Please type only y or n ").lower())

    #conditions to continue or not
    if choice_again == no: break
    elif choice_again == yes and player_one < 3 and computer < 3 or player_one == computer: continue

  #when game score is best 3 out of 5
  else: print("Sorry. You have finished the game.")

else: 
  #Prompt user to play or not
  choice_again = (input("Do you want to continue? Type y or n: ").lower())
  #exception handling
  while choice_again != yes and choice_again != no:
    choice_again = (input("Please type only y or n ").lower())

  #while loop to continue playing
  while choice_again != no and player_one <3 and player_two < 3: 
    #assign variables
    rock = "r"
    paper = "p"
    scissors = "s"
  
    #get user 1 input
    choice1 = (input("You are player 1. Please Enter r for rock, p for paper, s for scissors: "))
    #format choice
    choice_one = choice1.lower()
    #error handling
    while choice_one != rock and choice_one != paper and choice_one != scissors:
      choice_one =  (input("You did not enter a correct letter. Enter r for rock, p for paper, s for scissors: "))
      
    #get user 2 input
    choice2 = (input("You are player 2. Enter r for rock, p for paper, s for scissors: "))
    #format choice
    choice_two = choice2.lower()
    #error handling
    while choice_two != rock and choice_two != paper and choice_two != scissors: 
      choice_two =  (input("You did not enter a correct letter. Enter r for rock, p for paper, s for scissors: "))
      
    #calculate results
    if choice_one == rock:
      #user 1 = rock, user 2 = rock
      if choice_two == rock:
        print("You both chose rock. It's a tie!")
        player_one += 1
        player_two += 1
          
      #user 1 = rock, user 2 = paper
      elif choice_two == paper:
        print("Paper covers rock. Second player wins!")
        player_two += 1
            
      #user 1 = rock, user 2 = scissors
      else:
        print("Rock smashes scissors. First player wins!")
        player_one +=1
    
    elif choice_one == scissors:
      #user 1 = scissors, user 2 = rock
      if choice_two ==rock:
        print("Rock smashes scissors. Second player wins!")
        player_two +=1
      
      #user 1 = scissors, user 2 = paper
      elif choice_two == paper:
        print("Scissors cuts paper. First player wins!")
        player_one +=1
      #user 1 = scissors, user 2 = scissors
      else:
        print("You both chose scissors. It's a tie!")
        player_one +=1
        player_two +=1

    else:
      #user 1 = paper, user 2 = rock
      if choice_two ==rock:
        print("Rock covers paper. First player wins!")
        player_one +=1

      #user 1 = paper, user 2 = paper
      elif choice_two == paper:
        print("You both chose paper. It's a tie!")
        player_one +=1
        player_two +=1

      #user 1 = paper, user 2 = scissors
      else:
        print ("Scissors cuts paper. Second player wins!")
        player_two =+1   

    #print the score
    print("Player one has " + str(player_one) + " points.")
    print("Player one has " + str(player_two) + " points.")

    #conditional for winner
    if player_one > player_two:
      print("Player one is the winner!")
    elif player_one < player_two:
      print("Player two is the winner!")
    else:
      print("It's a tie!")

    #prompt to play again
    choice_again = (input("Do you want to continue: type y or n ").lower())
    #exception handling
    while choice_again != yes and choice_again != no:
      choice_again = (input("Please type only y or n ").lower())

    #conditions to continue or not
    if choice_again == no: break
    elif choice_again == yes and player_one < 3 and player_two < 3 or player_one == player_two: continue

  #when game has reached best 3 out of 5
  else: print("Sorry. You have finished the game.")
