class EmployeeSalary:
    hourly_payment = 400  # Устанавливаем почасовой уровень оплаты

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours  # Обязательный параметр для инициализации
        self.rest_days = rest_days  # Обязательный параметр для инициализации
        self.email = email  # Обязательный параметр для инициализации

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8  # Рассчитываем часы работы
        return cls(name, hours, rest_days, email)  # Создаем и возвращаем объект

    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"  # Генерируем email
        return cls(name, hours, rest_days, email)  # Создаем и возвращаем объект

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment  # Меняем значение hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment  # Рассчитываем заработную плату


# Пример использования:
email_ivan = "ivan@example.com"  # Здесь задайте нужный email
employee1 = EmployeeSalary.get_hours("Иван", rest_days=2, email=email_ivan)
print(f"Заработная плата {employee1.name}: {employee1.salary()}")

# Вывод email для сотрудника
print(f"Email {employee1.name}: {employee1.email}")

# Изменение почасовой оплаты
EmployeeSalary.set_hourly_payment(500)
print(f"Новая заработная плата {employee1.name} с измененной оплатой: {employee1.salary()}")