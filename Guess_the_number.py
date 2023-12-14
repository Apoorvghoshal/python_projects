import random
print("welcome to the number guessing game \n The correct number is in between 1 to 10")
x=int(11)
The_number = random.randint(1,x)
guess = 0
count=0
while guess != The_number:
    guess = int(input("Enter the Number you guessed: "))
    if (guess != The_number):
        count=count+1
        print("Sorry...Wrong Answer\n try again")
print("Yah! You have guessed the right number")
print(f"Your game score is {10-count}")