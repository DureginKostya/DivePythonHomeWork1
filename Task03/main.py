'''Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и
на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.'''

MIN_VALUE = 0
MAX_VALUE = 100_000
LEFT_RANGE = 2
number = int(input('Введите число: '))

if MIN_VALUE <= number <= MAX_VALUE:
    if number < LEFT_RANGE:
        print('Число - "ни простое", "ни составное"')
    else:
        for i in range(LEFT_RANGE, int(number ** 0.5) + 1):
            if number % i == 0:
                print('Число - "составное"')
                break
        else:
            print('Число - "простое"')
else:
    print('Число должно быть положительным и не больше 100_000')