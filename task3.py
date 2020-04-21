import random
set_number = 8
user_level = ""
count=0
while True:
    user_level = input('''Different levels for a user Enter easy for easy level
                              Enter medium for medium level
                              Enter hard for hard level : >''').lower()
    while user_level == 'easy' and count <6 :
        
        while True:
            try:
                guess = int(input("Guess a number between one and ten : "))
            except ValueError:
                print("Numbers only!!!!")
                continue
            else:
                break             
        count += 1
        guess_left= 6 - count
        guess_left=str(guess_left)
        if guess == set_number:
            print("You got it right")
            break
        elif guess < set_number:
            print("You picked a lower number!! you have " + guess_left + "guess left")
            print("That was wrong !!!")
        else:
            guess > set_number
            print("You picked a higher number!! you have " +
                  guess_left + "guess left")
            print("That was wrong!!")
        if not count < 6:
            print("Game Over!! The number is", set_number)
    while user_level =='medium' and count < 4:
         while True:
             try:
                 guess = int(input("Guess a number between one and twenty : "))
             except ValueError:
                print("Numbers only!!!!")
                continue
             else:
                  break    
         count +=1
         guess_left = 4-count
         guess_left = str(guess_left)
         if guess == set_number :
            print("You got it right")
            break
         elif guess < set_number:
            print("You picked a lower number!! you have " + guess_left + "guess left")
            print("That was wrong!!")
         else:
            guess > set_number 
            print("You picked a higher number!! you have " +  guess_left + "guess left")
            print("That was wrong")
         if not count < 4:
            print("Game Over!! The number is", set_number)
    while user_level == 'hard' and count < 3:
        while True:
            try:
                guess = int(input("Guess a number between one and ten : "))
            except ValueError:
                print("Numbers only!!!!")
                continue
            else:
                break
        count += 1
        guess_left= 3- count
        guess_left = str(guess_left)
        if guess == set_number:
            print("You got it right")
            break
        elif guess < set_number:
            print("You picked a lower number!! you have " +
                  guess_left + "guess left")
            print("That was wrong!!!")
        else:
             guess > set_number
             print("You picked a higher number!! you have " +
                  guess_left + "guess left")
             print("That was wrong!!")
        if not count < 3:
            print("Game Over!! The number is", set_number)
            
