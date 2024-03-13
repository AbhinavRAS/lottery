import random
lottery = random.randint(1, 100)
while(lottery>0):
    Your_Number = int(input("Enter your number: "))
    if (Your_Number==lottery):
        print("Congratulations! You Won the Lottery!")
    elif(Your_Number>lottery):
        print("Your number is too high!")
    else:
        print("Your number is too low!")
    
print("Thank you for playing!")
