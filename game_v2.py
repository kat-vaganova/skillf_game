import numpy as np
from random import randint

set_number = np.random.randint(1, 100) 
print(set_number)
try_count = 0


def random_predict(number):
    """Рандомно угадываем число

    Args:
        number (int): Загаданное число
        
    return число попыток
    """
    while True:
        guess_number = randint(1, 100) 
        try_count += 1
        if set_number == guess_number:
            print(f' \n Guess number: {guess_number}. \n Try count: {try_count}')
            break
        else:
            continue
        
        
        # if  __name__ ==  "_main_":
        #     random_predict(number)