class EmployeeSalary:
    hourly_payment = 400  # Устанавливаем почасовой уровень оплаты

    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days):
        hours = (7 - rest_days) * 8  # Рассчитываем часы работы
        return cls(name=name, hours=hours, rest_days=rest_days)

    @classmethod
    def get_email(cls, name):
        email = f"{name}@email.com"  # Генерируем email
        return cls(name=name, email=email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment  # Меняем значение hourly_payment

    def salary(self):
        if self.hours is None:  # Если часы не известны, рассчитываем их
            self.hours = (7 - self.rest_days) * 8
        return self.hours * self.hourly_payment  # Рассчитываем заработную плату

# Пример использования:
employee1 = EmployeeSalary.get_hours("Иван", rest_days=2)
print(f"Заработная плата {employee1.name}: {employee1.salary()}")

# Генерация email для сотрудника
employee1.email = EmployeeSalary.get_email(employee1.name).email
print(f"Email {employee1.name}: {employee1.email}")

# Изменение почасовой оплаты
EmployeeSalary.set_hourly_payment(500)
print(f"Новая заработная плата {employee1.name} с измененной оплатой: {employee1.salary()}")