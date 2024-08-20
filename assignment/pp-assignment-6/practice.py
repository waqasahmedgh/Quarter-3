import random
print(random.random())  # output is 0 to 0.1


import random
print(random.randint(1, 100))  # output between 1 to 100


import random
print(random.uniform(1.5, 10.5))  # Example output: 6.851409582727751

import random
print(random.choice(['apple', 'banana', 'cherry']))  # output may be 'banana' or apple or cherry

import random
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)  # Example output: [3, 1, 4, 2, 5]


import random
print(random.sample([1, 2, 3, 4, 5], 3))  # Example output: [5, 1, 3]




