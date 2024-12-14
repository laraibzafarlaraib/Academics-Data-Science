from random import*

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vector = (x,y,z)

    def __str__(self):
        return f'vector is {self.x}i+{self.y}j+{self.z}k\n{self.vector}'
    
    def add(self, other):
        added = f"({self.x + other.x}"
        added += ","
        added += f"{self.y + other.y}"
        added += ","
        added += f"{self.z + other.z})"

        return added
    
vector1 = Vector(2, 4, 6)
print(vector1)
vector2 = Vector(58, 89, 52)
print(vector2)
sum = vector1.add(vector2)
print('sum is',sum)

from random import randint

dimensions = 0
j = randint(1, 50)
vector = [randint(1, 100) for i in range(j)]
print(vector)

from random import randint

num_dimensions = 5

# Generate random variables for each dimension and store them in a dictionary
dimensions_dict = [chr(105 + i)for i in range(num_dimensions)]
goodgood=                  [ randint(1, 100) for i in range(num_dimensions)]

# Print the dictionary of dimensions
print(dimensions_dict,goodgood)

dimensions = randint(1,20)
j = randint(1, 50)
huhu = tuple(chr(97 + i)for i in range(dimensions))
# Use tuple() to convert the generator expression to a tuple
vector = tuple(randint(1, 100) for _ in range(dimensions))

print(huhu, vector)

for i in range (len(vector)):
    print(f'{vector[i]}{huhu[i]} ', end='')