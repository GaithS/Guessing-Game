import random

def main():
    number = random.randint(1, 100)
    print("Try to guess the number between 1 and 100!")
    cont = True

    guess_count = 0
    
    while cont: 
        guess = input("Enter number  ")
        guess_count += 1
        try:
            guess = int(guess)
            if guess > number: 
                print("Lower")
            elif guess < number: 
                print("Higher")
            elif guess == number:
                cont = False
                print(f"Correct! The number was {number} and you got it in {guess_count} of tries")    
        except ValueError: 
            print("Enter a valid integer")

if __name__ == "__main__":
    main()
