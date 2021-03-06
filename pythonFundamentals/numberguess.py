import random
"""
Asks the user to define a range,
then checks if the user has guessed the number or not
and shows how many tries were used
"""
def main():
    smaller = int(input("Enter the smaller number: "))
    larger = int(input("Enter the larger number: "))
    myNumber = random.randint(smaller, larger)
    count=0
    while True:
        count +=1
        userNumber = int(input("Enter your guess: "))
        if userNumber < myNumber:
            print("Too small")
        elif userNumber > myNumber:
            print("Too big")
        else:
            print("You've got it in", count, "tries!")
            break

if __name__ == '__main__':
    main()