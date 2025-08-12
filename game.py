print('----------STARTING NEW RUN----------')

import pandas as pd
import random

# for i in range(5):
#     print('Hello World')

lowest_num = 0
highest_num = 100

random_number = random.randint(lowest_num, highest_num)
print('PRINTING RANDOM NUMBER BETWEEN: ' , str(lowest_num) , ' AND ' , str(highest_num))
print(random_number)



print('----------FINISHED RUN----------')