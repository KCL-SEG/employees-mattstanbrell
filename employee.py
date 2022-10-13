
class Employee:
    def __init__(self, name, num_commission_contracts, commission_salary, bonus_commission):
        self.name = name
        self.num_commission_contracts = num_commission_contracts
        self.commission_salary = commission_salary
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return (self.num_commission_contracts * self.commission_salary) + self.bonus_commission

    def __str__(self):
        return self.name

    def get_commission_message(self):
        return f" and receives a commission for {self.num_commission_contracts} contract(s) at {self.commission_salary}/contract."

    def get_bonus_message(self):
        return f" and receives a bonus commission of {self.bonus_commission}."


class MonthlyContractor(Employee):
    def __init__(self, name, monthly_salary, num_commission_contracts=0, commission_salary=0, bonus_commission=0):
        super().__init__(name, num_commission_contracts,
                         commission_salary, bonus_commission)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return super().get_pay() + self.monthly_salary

    def __str__(self):
        msg = f"{super().__str__()} works on a monthly salary of {self.monthly_salary}"
        if self.num_commission_contracts > 0:
            msg += super().get_commission_message()
        elif self.bonus_commission > 0:
            msg += super().get_bonus_message()
        else:
            msg += "."
        msg += f" Their total pay is {self.get_pay()}."
        return msg


class HourlyContractor(Employee):
    def __init__(self, name, hourly_salary, hours_worked, num_commission_contracts=0, commission_salary=0, bonus_commission=0):
        super().__init__(name, num_commission_contracts,
                         commission_salary, bonus_commission)
        self.hourly_salary = hourly_salary
        self.hours_worked = hours_worked

    def get_pay(self):
        return super().get_pay() + (self.hourly_salary * self.hours_worked)

    def __str__(self):
        msg = f"{super().__str__()} works on a contract of {self.hours_worked} hours at {self.hourly_salary}/hour"
        if self.num_commission_contracts > 0:
            msg += super().get_commission_message()
        elif self.bonus_commission > 0:
            msg += super().get_bonus_message()
        else:
            msg += "."
        msg += f" Their total pay is {self.get_pay()}."
        return msg


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyContractor('Billie', 4000, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyContractor('Charlie', 25, 100, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyContractor('Renee', 3000, 4, 200, 0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyContractor('Jan', 25, 150, 3, 220, 0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyContractor('Robbie', 2000, 0, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyContractor('Ariel', 30, 120, 0, 0, 600)
