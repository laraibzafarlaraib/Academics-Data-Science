class Polynomial:
    
    def __init__(self, coefficients):
        # Initialize the polynomial with a list of coefficients.
        # The coefficients list should be in ascending order of powers.
        self.coefficients = coefficients

    @property
    def degree(self):
        # Calculate and return the degree of the polynomial.
        return len(self.coefficients) - 1

    def __str__(self):
        # Create a string representation of the polynomial.
        terms = []
        for i, coeff in enumerate(self.coefficients):
            power = self.degree - i
            if coeff != 0:
                term = f"{coeff}x^{power}" if power > 1 else f"{coeff}x" if power == 1 else str(coeff)
                terms.append(term)
        return " + ".join(terms)

    def evaluate(self, x):
        # Evaluate the polynomial for a given value of x.
        result = 0
        for coeff in self.coefficients[ : : -1]:
            result = result*x+coeff
        return result

    def add(self, other):
        # Add two polynomials and return a new Polynomial object.
        # Determine the length of the result coefficients based on the higher degree.
        result_degree = max(self.degree, other.degree)
        
        # Initialize the result coefficients with zeros.
        result_coefficients = [0] * (result_degree + 1)
        
        # Add coefficients from both polynomials.
        for i in range(self.degree + 1):
            result_coefficients[i] += self.coefficients[i]
        
        for i in range(other.degree + 1):
            result_coefficients[i] += other.coefficients[i]
        
        return Polynomial(result_coefficients)


    def subtract(self, other):
        # Subtract two polynomials and return a new Polynomial object.
        
        # Determine the length of the result coefficients based on the higher degree.
        result_degree = max(self.degree, other.degree)
        
        # Initialize the result coefficients with zeros.
        result_coefficients = [0] * (result_degree + 1)
        
        # Subtract coefficients from both polynomials.
        for i in range(self.degree + 1):
            result_coefficients[i] += self.coefficients[i]
        
        for i in range(other.degree + 1):
            result_coefficients[i] -= other.coefficients[i]
        
        return Polynomial(result_coefficients)


    def multiply(self, other):
        # Multiply two polynomials and return a new Polynomial object.
        result_degree = self.degree + other.degree
        result_coefficients = [0] * (result_degree + 1)
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result_coefficients[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(result_coefficients)

    def derivative(self):
        # Calculate the derivative of the polynomial and return a new Polynomial object.
        result_coefficients = [self.coefficients[i] * (self.degree - i) for i in range(self.degree)]
        return Polynomial(result_coefficients)

    
# Create polynomial objects with coefficients
poly1 = Polynomial([1, 2, 3])  # Represents 1x^2 + 2x + 3
poly2 = Polynomial([2, -1, 0, 4])  # Represents 2x^3 - x^2 + 4

# Display the polynomials
print("Polynomial 1:", poly1)
print("Polynomial 2:", poly2)

# Calculate the degree of the polynomials
print("Degree of Polynomial 1:", poly1.degree)
print("Degree of Polynomial 2:", poly2.degree)

# Evaluate the polynomials for a given value of x
x = 2
print(f"Evaluate Polynomial 1 at x={x}: {poly1.evaluate(x)}")
print(f"Evaluate Polynomial 2 at x={x}: {poly2.evaluate(x)}")

# Perform addition, subtraction, and multiplication
poly_add = poly1.add(poly2)
poly_subtract = poly1.subtract(poly2)
poly_multiply = poly1.multiply(poly2)

print("Polynomial Addition:", poly_add)
print("Polynomial Subtraction:", poly_subtract)
print("Polynomial Multiplication:", poly_multiply)

# Calculate the derivative of a polynomial
poly_derivative = poly1.derivative()
print("Derivative of Polynomial 1:", poly_derivative)


