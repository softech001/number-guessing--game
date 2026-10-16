
 # 1 NUMBER GUESSING GAME####################################################################!!!!!!!!!!!!
   
secret_number= 8
for i in range(5):
     guess=int(input(" guess the number:"))
     print("you have",5-i, "chances left")
     if guess == secret_number:
            print("YOU GUESSED THE NUMBER CORRECTLY ")
            break 
        
     elif guess < secret_number:
            print("TOO LOW !! TRY AGAIN ")
     elif guess > secret_number:
            print(" TOO HIGH !! TRY AGAIN ")
else:
          print(" GAME OVERRRRRRRRRR" )
          print(" THE NUMBER IS ",secret_number)
        
