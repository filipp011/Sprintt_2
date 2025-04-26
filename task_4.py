class EmployeeSalary:
    hourly_payment = 400  # Устанавливаем почасовой уровень оплаты

    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(self):
        if self.hours is None:
            # Если hours неизвестно, рассчитываем часы по формуле
            self.hours = (7 - self.rest_days) * 8
        return self.hours

    def get_email(self):
        if self.email is None:
            # Генерируем email, если он неизвестен
            self.email = f"{self.name}@email.com"
        return self.email

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        # Рассчитываем заработную плату
        return self.get_hours() * EmployeeSalary.hourly_payment


# Пример использования класса
if __name__ == "__main__":
    employee1 = EmployeeSalary(name="Ivan", rest_days=2)
    
    print(f"Employee Name: {employee1.name}")
    print(f"Hours Worked: {employee1.get_hours()}")  # Ожидается: 40 (5 дней * 8 часов)
    print(f"Email: {employee1.get_email()}")         # Ожидается: Ivan@email.com
    print(f"Salary: {employee1.salary()}")           # Ожидается: 16000 (40 * 400)

    employee2 = EmployeeSalary(name="Maria", hours=32)
    
    print(f"\nEmployee Name: {employee2.name}")
    print(f"Hours Worked: {employee2.get_hours()}")  # Ожидается: 32 (передано в конструктор)
    print(f"Email: {employee2.get_email()}")         # Ожидается: Maria@email.com
    print(f"Salary: {employee2.salary()}")           # Ожидается: 12800 (32 * 400)

    # Изменяем почасовую оплату
    EmployeeSalary.set_hourly_payment(500)
    
    print(f"\nNew Hourly Payment: {EmployeeSalary.hourly_payment}")  # Ожидается: 500
    print(f"New Salary for {employee1.name}: {employee1.salary()}")   # Ожидается: 20000 (40 * 500)