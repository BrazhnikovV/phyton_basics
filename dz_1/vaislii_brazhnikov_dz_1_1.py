

duration = int(input("Введите длительность:"));
total_days      = duration // (60 * 60 * 24)
rest_of_days    = duration % (60 * 60 * 24)
total_hours     = rest_of_days // (60 * 60)
rest_of_hours   = rest_of_days % (60 * 60)
total_minutes   = rest_of_hours // 60
rest_of_minutes = rest_of_hours % 60
total_seconds   = rest_of_minutes

print(
    total_days,    'Дней:',
    total_hours,   'Часов:',
    total_minutes, 'Минут:',
    total_seconds, 'Секунд:'
)
