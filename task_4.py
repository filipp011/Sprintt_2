class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def create_employee(cls, name, rest_days=0, hours=None):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name=name, hours=hours, rest_days=rest_days)

    @classmethod
    def get_email(cls, name, email=None):
        if email is None:
            email = f"{name}@email.com"
        return email

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        effective_hours = self.get_hours()
        return effective_hours * EmployeeSalary.hourly_payment

    def get_hours(self):
        if self.hours is None:
            return (7 - self.rest_days) * 8
        return self.hours


if __name__ == "__main__":
    employee1 = EmployeeSalary.create_employee(name="Ivan", rest_days=2)
    employee1.email = EmployeeSalary.get_email(employee1.name)
    
    print(f"Employee Name: {employee1.name}")
    print(f"Hours Worked: {employee1.get_hours()}")
    print(f"Email: {employee1.email}")
    print(f"Salary: {employee1.salary()}")

    employee2 = EmployeeSalary.create_employee(name="Maria", hours=32)
    
    print(f"\nEmployee Name: {employee2.name}")
    print(f"Hours Worked: {employee2.get_hours()}")
    print(f"Email: {employee2.email}")
    print(f"Salary: {employee2.salary()}")

    EmployeeSalary.set_hourly_payment(500)
    
    print(f"\nNew Hourly Payment: {EmployeeSalary.hourly_payment}")
    print(f"New Salary for {employee1.name}: {employee1.salary()}")