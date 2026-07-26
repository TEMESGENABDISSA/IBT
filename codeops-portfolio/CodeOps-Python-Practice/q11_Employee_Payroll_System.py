from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self,name):

        self.name=name


    @abstractmethod
    def pay(self):
        pass



class FullTimeEmployee(Employee):

    def __init__(self,name,salary):

        super().__init__(name)
        self.salary=salary


    def pay(self):

        return self.salary



class PartTimeEmployee(Employee):

    def __init__(self,name,rate,hours):

        super().__init__(name)
        self.rate=rate
        self.hours=hours


    def pay(self):

        return self.rate*self.hours



class ContractEmployee(Employee):

    def __init__(self,name,salary,bonus):

        super().__init__(name)
        self.salary=salary
        self.bonus=bonus


    def pay(self):

        return self.salary+self.bonus



def print_payroll(employees):

    for employee in employees:

        print(
            employee.name,
            employee.pay()
        )