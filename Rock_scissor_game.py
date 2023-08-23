import random
condition=True
while condition==True:
 print("Winning Rules of the Rock paper and Scissor game as follows:\nrock vs paper->paper wins\nrock vs scissors->rock wins \npaper vs scissors->scissors wins ")
 print("Enter choice\n1. rock\n2. paper\n3. scissor ")
 Input=int(input())
 user_turn=''
 if Input==1:
  user_turn="rock"
 elif Input==2:
  user_turn="paper"
 elif Input==3:
  user_turn="scissor"
 print(f"User Choice is: {user_turn}")
 print("Now it is computer turn...")
 lst=["rock","paper","scissor"]
 computer_turn=random.choice(lst)
 print(f"Computer Choice is: {computer_turn}")
 if user_turn=="rock" and computer_turn =="paper":
   print(f"{user_turn} V/s {computer_turn}")
   print("paper wins => computer wins")
   Input1=input("Do You want to play again? Type 'Y' or Type 'N': ")
   if Input1=='Y':
     condition=True
   elif Input1=='N':
     condition=False
 elif user_turn=="rock" and computer_turn=="scissor":
  print(f"{user_turn} V/s {computer_turn}")
  print("rock wins => user wins")
  Input1=input("Do You want to play again? Type 'Y' or Type 'N': ")
  if Input1=='Y':
   condition=True
  elif Input1=='N':
   condition=False
 elif user_turn=="paper" and computer_turn=="scissor":
   print(f"{user_turn} V/s {computer_turn}")
   print("scissor wins => computer wins")
   Input1=input("Do You want to play again? Type 'Y' or Type 'N': ")
   if Input1=='Y':
     condition=True
   elif Input1=='N':
     condition=False
 elif user_turn==computer_turn:
  print("Draw")
  Input1=input("Do You want to play again? Type 'Y' or Type 'N': ")
  if Input1=='Y':
      condition=True
  elif Input1=='N':
     condition=False