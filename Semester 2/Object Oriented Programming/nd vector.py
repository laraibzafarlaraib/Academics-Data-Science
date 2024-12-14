import math
from random import randint

class NDimensionalVector:
    def __init__(self, dimensions=None, values=None):
        if dimensions is not None and values is not None:
            if len(values) != dimensions:
                raise ValueError("Number of values must match the specified dimensions.")
            self.dimensions = dimensions
            self.vector = tuple(values)
        elif dimensions is not None:
            self.dimensions = dimensions
            self.vector = tuple(randint(1, 100) for _ in range(self.dimensions))
        else:
            raise ValueError("Specify either dimensions or both dimensions and values.")

    def magnitude(self):
        mag = math.sqrt(sum(x**2 for x in self.vector))
        return mag

    def dot_product(self, other):
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have the same number of dimensions for dot product.")
        result_dot_product = sum(x * y for x, y in zip(self.vector, other.vector))
        return result_dot_product

    @classmethod
    def from_vector(cls, vector):
        return cls(dimensions=len(vector), values=vector)

    def __str__(self):
        vector_str = ', '.join(str(x) for x in self.vector)
        return f"({vector_str})"


def main():
    vector_2d_a = NDimensionalVector(dimensions=2)
    vector_2d_b = NDimensionalVector(dimensions=2)

    print("2D Vector A:", vector_2d_a)
    print("2D Vector B:", vector_2d_b)
    print("Magnitude of 2D Vector A:", vector_2d_a.magnitude())
    print("Dot Product of 2D Vectors A and B:", vector_2d_a.dot_product(vector_2d_b))
    print()

    # 3d vectors
    vector_3d_a = NDimensionalVector(dimensions=3)
    vector_3d_b = NDimensionalVector(dimensions=3)

    print("3D Vector A:", vector_3d_a)
    print("3D Vector B:", vector_3d_b)
    print("Magnitude of 3D Vector A:", vector_3d_a.magnitude())
    print("Dot Product of 3D Vectors A and B:", vector_3d_a.dot_product(vector_3d_b))
    print()

    # 4d vectors
    vector_4d_a = NDimensionalVector(dimensions=4)
    vector_4d_b = NDimensionalVector(dimensions=4)

    print("4D Vector A:", vector_4d_a)
    print("4D Vector B:", vector_4d_b)
    print("Magnitude of 4D Vector A:", vector_4d_a.magnitude())
    print("Dot Product of 4D Vectors A and B:", vector_4d_a.dot_product(vector_4d_b))
    print()

    # 5d vectors
    vector_5d_a = NDimensionalVector(dimensions=5)
    vector_5d_b = NDimensionalVector(dimensions=5)

    print("5D Vector A:", vector_5d_a)
    print("5D Vector B:", vector_5d_b)
    print("Magnitude of 5D Vector A:", vector_5d_a.magnitude())
    print("Dot Product of 5D Vectors A and B:", vector_5d_a.dot_product(vector_5d_b))
    print()

if __name__ == "__main__":
    main()
