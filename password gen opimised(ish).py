#change the variable for the amount of passwords you whant

num=10

import random
import string

mun=0

end=1

while (num>mun):
    
    num=num-1
    
    def get_random_string(length):
    
        letters = string.printable
        result_str = ''.join(random.choice(letters) for i in range(length))
        print("Random string of length", length, "is:", result_str)

    get_random_string(20)

end = input("end")