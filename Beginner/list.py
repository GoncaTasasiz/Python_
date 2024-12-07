#list = ["abc", 2, "cde", 4, 0.4]

#list.append("ftt")

#list.extend([5, "thy"])

#print(list)

import random

friends = ["Alice", "Bob", "Charles", "David", "Emanuel"]

random_index = random.randint(0, len(friends)-1)

print(friends[random_index])


#Easiest way
print(random.choice(friends))