employee_list = ["инженер-конструктор Игорь", "главный бухгалтер МАРИНА", "токарь высшего разряда нИКОЛАй", "директор аэлита"]

for idx in range(len(employee_list)):
    employee_parts = employee_list[idx].split(" ")
    print("Привет,", employee_parts[len(employee_parts) - 1].capitalize(), "!")
