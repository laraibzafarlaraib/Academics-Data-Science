from random import randint
import math

class nDimentionalVector:
    def __init__(self, dimensions=None):
        if dimensions is None:
            self.dimensions = randint(1, 20)
        else:
            self.dimensions = dimensions
        self.var = tuple(chr(97 + i) for i in range(self.dimensions))
        self.vector = tuple(randint(1, 100) for _ in range(self.dimensions))

    def magnitude(self):
        mag = math.sqrt(sum(x**2 for x in self.vector))
        return mag

    def direction(self):
        magnitude = math.sqrt(sum(x**2 for x in self.vector))
        direction = tuple(x / magnitude for x in self.vector)
        return direction

    def vector_addition(self, other):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have the same number of dimensions for addition.")
        result_vector = tuple(x + y for x, y in zip(self.vector, other.vector))
        return nDimentionalVector.from_vector(result_vector)

    def vector_subtraction(self, other):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have the same number of dimensions for subtraction.")
        result_vector = tuple(x - y for x, y in zip(self.vector, other.vector))
        return nDimentionalVector.from_vector(result_vector)

    def scalar_multiplication(self, other):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have the same number of dimensions for dot product.")
        result_scalar = sum(x * y for x, y in zip(self.vector, other.vector))
        return result_scalar

    @classmethod
    def from_vector(cls, vector):
        instance = cls(dimensions=len(vector))
        instance.vector = vector
        instance.var = tuple(chr(97 + i) for i in range(instance.dimensions))
        return instance

    def __str__(self):
        vector_str = ', '.join(f'{x}{v}' for x, v in zip(self.vector, self.var))
        return f"({vector_str})"

def main():
    vector1 = nDimentionalVector()
    vector2 = nDimentionalVector(dimensions=vector1.dimensions)

    print(f'Vector 1 has following attributes:')
    print(vector1)
    print(f'Vector 2 has following attributes:')
    print(vector2)
    print(f'Sum of two vectors is {vector1.vector_addition(vector2)}')
    print(f'Subtraction of two vectors is {vector1.vector_subtraction(vector2)}')
    print(f'Dot product of two vectors is {vector1.scalar_multiplication(vector2)}')

main()
