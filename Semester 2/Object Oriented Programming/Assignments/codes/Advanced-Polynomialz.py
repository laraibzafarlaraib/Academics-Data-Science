class Polynomial:
    def __init__(self,coefficient):
        self.coefficient=coefficient

    def degree(self):
        return len(self.coefficient)-1

    def set_base(self, base):
        self.base_var = base

    def addition(self, other):
        if self.base_var == other.base_var:
            
            max_degree = max(self.degree(), other.degree()) #finding the degree of resulting polynomial.
            new_coefficients = [0] * (max_degree + 1) #to store new coefficients of resulting polnomials.
            
            for i in range(self.degree() + 1):
                new_coefficients[i] += self.coefficient[i]
        
            for i in range(other.degree() + 1):
                new_coefficients[i] += other.coefficient[i]
            result = Polynomial(new_coefficients)
            result.set_base(self.base_var)  # Set the base for the resulting polynomial
            return result
        else:
            print("Bases are not the same.")
            return None

    def subtract(self, other):
        if self.base_var == other.base_var:
            
            result_degree = max(self.degree(), other.degree())
            result_coefficients = [0] * (result_degree + 1)
            
            for i in range(self.degree() + 1):
                result_coefficients[i] += self.coefficient[i]
            
            for i in range(other.degree() + 1):
                result_coefficients[i] -= other.coefficient[i]
            
            result = Polynomial(result_coefficients)
            result.set_base(self.base_var)  # Set the base for the resulting polynomial
            return result
        else:  
            print("Bases are not the same.")
            return None
        
    def multiply(self, other):
        if self.base_var == other.base_var:
            result_degree = self.degree() + other.degree()
            result_coefficients = [0] * (result_degree + 1)

            for i in range(len(self.coefficient)):
                for j in range(len(other.coefficient)):
                    result_coefficients[i + j] += self.coefficient[i] * other.coefficient[j]
            result = Polynomial(result_coefficients)
            result.set_base(self.base_var)  # Set the base for the resulting polynomial
            return result
        else:
            
            print("Bases are not the same.")
            return None

    def show(self):
        j = ""
        for i in range(len(self.coefficient)):
            z = self.coefficient[i]
            #to check if the coefficient is not 0 before including it in the string.
            if z != 0:                      
                #to check if we are at the last term to avoid adding a + after the last term.
                if i == self.degree():
                    j+= f"{z}"
                else:
                    j += f'{z}{self.base_var}^{self.degree()-i}'
                    if i != self.degree(): #to not print + at the end
                        j += "+"
        print(j)

 
def main():
    # 1st polynomial
    a = Polynomial([1, 5, 4, 0, 8, 0, 2, 0, 0, 7])
    a.set_base("x")  
    print('1st polynomial is:')
    a.show()

    # 2nd polynomial
    b = Polynomial([0, 2, 4, 8, 6, 4, 10])
    b.set_base("x") 
    print('2nd polynomial is:')
    b.show()

    q = a.addition(b)
    print('Addition is:')
    q.show()

    q = a.subtract(b)
    print('subtraction is:')
    q.show()

    q = a.multiply(b)
    print('multiplication is:')
    q.show()

if __name__ == "__main__":
    main()