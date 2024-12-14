import time
class Address:
    def __init__(self, house, street, city, country):
        self.house = house
        self.street = street
        self.city = city
        self.country = country

    def format(self):
        return f"{self.house}, {self.street}, {self.city}, {self.country}."

        
class Bill:
    def __init__(self, no, name, address):
        self.no = no
        self.name = name
        self.sec = time.time()
        self.address = address
        self.items = []
        
    def add_items(self, particulars, rate, qty):
        self.items.append((particulars, rate, qty))
        
    def calc_total(self):
        total = 0
        for particulars, rate, qty in self.items:
            total += rate * qty
        return total

    def __str__(self):
        l = 'MOBILO\n'
        l+= 'Mobile City\n'
        l+= 'Deals in all kinds of Mobile sets and Accsessories\n'
        l+= 'Cell No: 0321-0000000\n'
        l+= 'CASHMENO\n'
        l+= f'No:{self.no}\n'
        l+= f'Date: {time.ctime(self.sec)}\n'
        l+= f'Customer Name: {self.name}\n'
        l+= f'Customer Address: {self.address.format()}\n'
        l+= '\n'
        l+= f'Particulars: \t\t Rate:\t\t Qty:\t\t Amount:\n'
        for particulars, rate, qty in self.items:
            l+= f'\n{particulars} \t\t {rate}\t\t {qty}\t\t {rate * qty}'
        total = self.calc_total()
        l+= f'\n\n\t\t\t\t\t\tTotal: {total}'
        l+= '\n'
        l+= '\nSignature:'
        l+= '\n'
        l+= '\nAddress: Basement # 2, Allahwala Plaza, Markaz K8, Islamabad'
        return l
        
def main():
    address = Address('house no 08', 'street no 06', 'Lahore', 'Pakistan')
    entity = Bill(1, "Laraib", address)
    entity.add_items('Mobile charger', 100, 2)
    entity.add_items('Hard drive', 1000, 1)
    entity.add_items('Samsung Z Fold', 9500, 3)
    print()
    print(entity)
    

    
if __name__=='__main__':
    main()


