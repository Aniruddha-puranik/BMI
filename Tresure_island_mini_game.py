print('''

          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You are in a jungle, you can either go left or right choose one direction.\n(left,right)")

in_direction = direction.lower()

if in_direction == "left":
  action = input("You find a lake, across the lake there is a mansion you can swim or wait for the boat. \n(swim,wait) ")
  
  in_action = action.lower()

  if in_action == "wait":
    door = input("You reached the mansion now you can see three doors in front of you red, yellow and blue which one will you choose\n(red,yellow,blue)")

    in_door = door.lower()

    if in_door == "yellow":
      print("CONGRATULATIONS YOU FOUND THE TREASURE, YOU WIN !!!")
    elif in_door == "red":
      print("It was a burning room! GAME-OVER!!!")
    elif in_door == "blue":
      print("There was a hungry beat inside the room you got eaten! GAME-OVER!!!")
    else:
      print ("Before you reached the doors you stepped on a land mine. GAME-OVER!!!")


  elif in_action == "swim" :
    print ("You got eaten by a shark. GAME-OVER!!!")
  else:
    print ("Please enter a valid input, Start again")

elif in_direction == "right" :
  print ("You lost in the jungle.  GAME-OVER!!!")
else :
  print ("Please enter a valid input, Start again")
