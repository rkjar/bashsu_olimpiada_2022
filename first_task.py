"""
Студент Иван учится на бюджете только на 4 и 5, поэтому получает повышенную стипендию равную x рублей.
Также имеет достижения в науке и спорте, поэтому получает ПГАС, сумма которой равна y рублей.
Ивану предлагают устроиться в компанию "Компьютер и мышка", и обещают платить зарплату в z рублей.
Но занятость в компании будет более 20 часов, поэтому Иван точно забросит учебу и поэтому стипендию получать не будет.
Укажите в ответе выгодно ли Ивану устраиваться на работу?

Формат ввода
Первая строка содержит три положительных целых числа x, y и z (через пробел, без запятых)

Формат вывода
Для входных данных выведите в одной строке слово YES, если Ивану выгоднее устроиться на работу.
Либо NO, если сумма стипендий больше чем зарплата либо если невозможно определить.
"""

def money_comparison(x: int, y: int, z: int) -> str:
	return 'YES' if z > (x + y) else 'NO'


x, y, z = list(map(int, input().split()))
print(money_comparison(x, y, z))