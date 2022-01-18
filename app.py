import random
secret_number = random.randint(1, 9)
guess_count = 0
guess_limit = 5

while guess_count < guess_limit:
    number = int(input("Guess the correct number"))
    guess_count = guess_count + 1
    if number == secret_number:
        print("Congratulations You ave guessed the correct number")
    else:
        print("Wrong!!!!")    
else:        
   print("YOU HAVE MADE 5 WRONG GUESSES")