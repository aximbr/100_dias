#Day 4
import random

i = 100
j = 20e7

#Genrerates a random number between i and j
a = random.randrange(i,j)
try:
    b = random.randrange(j, i)
except ValueError:
    print("ValueError on randrange() since start > stop")

c = random.randint(100, 200)

try:
    random.randint(200, 100)
except ValueError:
    print("ValueError on randint() since 200 > 100")

print("i = ", i, " and j = ", j)
print("randrange() generated number ", a)
print("randint() generates number ", c)

