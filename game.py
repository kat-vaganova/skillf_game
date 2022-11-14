import numpy as np

set_number = np.random.randint(1, 100) 
print(set_number)
try_count = 0


while True:
    guess_number = int(input("Enter number: "))
    try_count += 1
    if set_number == guess_number:
        print((f'Congratulate! \n Guess number: {guess_number}. \n Try count: {try_count}'))
        break
    elif set_number > guess_number:
        print(f'Your number is less! Try again!')
    else:
        print(f'Your number is more! Try again!')
        
        
        
        
