import random 

random_number = random.randint(1, 20) 
chance = 3 

print("Welcome to the Guessing Game! \nGuess a number between 1 and 20"); 
print("You have 3 chances to guess the correct number."); 
while chance > 0: 
    guess = int(input("Take a guess: ")); 
    chance -= 1 
    if guess == random_number: 
        print("Great, You nailed it!"); 
        break 
    elif guess < random_number: 
        print("low"); 
    else: 
        print("high!"); 

if chance > 0: 
    print("You have", chance, "chance(s) left."); 
else: 
    print("Sorry, you're out of chances. The number was", random_number);