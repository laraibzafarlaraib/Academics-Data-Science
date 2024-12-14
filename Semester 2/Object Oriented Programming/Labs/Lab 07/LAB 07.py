class Employee:
    def __init__(self,name,number,cnic,phone,address):
        self.number = number
        self.name= name
        self.cnic = cnic
        self.phone = phone
        self.address = address
        
    def __str__(self):
        return f"Employee Data:\nName: {self.name}\nNumber: {self.number}\nCNIC Number: {self.cnic}\nPhone: {self.phone}\nAddress: {self.address}"


class Salary(Employee):
    def __init__(self, number,name,cnic,phone,address, weeks, sal):
        super().__init__(number,name,cnic,phone,address)
        self.weeks = weeks
        self.sal = sal

    def cal(self):
        self.total = self.weeks * self.sal
        return self.total
    
    def __str__(self):
        return f"{super().__str__()},\nSalary of Employee: {self.cal()}"

class Hourly(Employee):
    def __init__(self, number,name,cnic,phone,address, hours, pay_rate):
        super().__init__(number,name,cnic,phone,address)
        self.hours = hours
        self.pay_rate = pay_rate

    def cal(self):
        self.total = self.hours * self.pay_rate
        if self.hours >= 40:
            for i in range(40-self.hours):
                self.total += 10000
        return self.total
    
    def __str__(self):
        return f"Salary of Hourly Employee: {self.cal()}"

class Payroll:
    def __init__(self):
        self.listt= []
        
    def add(self, a):
        self.listt.append(a)
        
    def show(self):
        for i in range(len(self.listt)):
            print(self.listt[i])

def main():
    emp1 = Salary("Laraib Zafar", 23, 3520247694918, +923258117699, "House no 8, street no 6, lahore", 5,4500)
    
    emp2 = Hourly("Laiba Zafar", 23, 3520247694918, +923258117699, "House no 8, street no 6, lahore" , 45, 8001)
    
    emp3 = Salary("Umber Junaid", 45, 3520247694918, +923245617699, "House no 14, Lahore", 8, 8500)
    
    emp4 = Hourly("Zainab Junaid", 45, 3520247694918, +923245617699, "House no 14, Lahore", 60, 2000)
    
    p = Payroll()
    p.add(emp1)
    p.add(emp2)
    p.add(emp3)
    p.add(emp4)
    p.show()
    
main()
        
