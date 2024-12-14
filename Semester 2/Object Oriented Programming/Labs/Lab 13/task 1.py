class Numbers:
    def __init__(self):
        self.even = []
        self.odd = []
        self.current_index = 0

    def add(self):
        times = int(input('How many numbers do you want to add? '))
        for _ in range(times):
            try:
                number = int(input('Enter a number: '))
                if self.is_even(number):
                    self.even.append(number)
                else:
                    self.odd.append(number)
            except ValueError:
                print('Enter a numerical value.')

    def alter(self):
        try:
            c = int(input('Enter the number to alter: '))
            new_number = int(input('Enter the new number: '))

            if self.is_even(c):
                if c in self.even:
                    index = self.even.index(c)
                    self.even[index] = new_number
                else:
                    print("Number not found.")
            else:
                if c in self.odd:
                    index = self.odd.index(c)
                    self.odd[index] = new_number
                else:
                    print("Number not found.")
        except ValueError:
            print('Enter a numerical value.')

    def delete(self):
        try:
            d = int(input('Enter the number to delete: '))
            if self.is_even(d):
                if d in self.even:
                    self.even.remove(d)
                else:
                    print("Number not found.")
            else:
                if d in self.odd:
                    self.odd.remove(d)
                else:
                    print("Number not found.")
        except ValueError:
            print('Enter a numerical value.')

    def search(self):
        try:
            s = int(input('Enter the number to search: '))
            if self.is_even(s):
                if s in self.even:
                    print(f"{s} found in the list.")
                else:
                    print(f"{s} not found.")
            else:
                if s in self.odd:
                    print(f"{s} found in the list.")
                else:
                    print(f"{s} not found.")
        except ValueError:
            print('Enter a numerical value.')

    def is_even(self, number):
        return number % 2 == 0

    def is_odd(self, number): 
        return not self.is_even(number)

    def order(self):
        combined_list = [val for pair in zip(self.odd, self.even) for val in pair]
        print(combined_list)

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        combined_list = [val for pair in zip(self.odd, self.even) for val in pair]
        if self.current_index < len(combined_list):
            result = combined_list[self.current_index]
            self.current_index += 1
            return result
        else:
            self.current_index = 0  
            raise StopIteration

    def __getitem__(self, index):
        combined_list = [val for pair in zip(self.odd, self.even) for val in pair]
        return combined_list[index]

    def __setitem__(self, index, value):
        combined_list = [val for pair in zip(self.odd, self.even) for val in pair]
        combined_list[index] = value
        
        self.odd = combined_list[::2]
        self.even = combined_list[1::2]

    def __str__(self):
        return f"Odd List: {self.odd}\nEven List: {self.even}"


def main():
    q = Numbers()

    choice = input('What do you want to do? \na) Add a new number \nb) Search a number \nc) Delete \nd) Alter \ne) Print all of the number list \nf) Iterate \ng) Indexing \n')
    if choice == 'a':
        q.add()

    elif choice == 'b':
        q.search()

    elif choice == 'c':
        q.delete()

    elif choice == 'd':
        q.alter()

    elif choice == 'e':
        q.order()

    elif choice == 'f':
        for num in q:
            print(num)

    elif choice == 'g':
        index = int(input('Enter the index to access: '))
        print(f"Value at index {index}: {q[index]}")

        new_value = int(input('Enter the new value: '))
        q[index] = new_value

        print("Updated Numbers:")
        print(q)

    else:
        print("Invalid choice.")

main()
