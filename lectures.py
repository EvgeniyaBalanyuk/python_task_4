# ===========================================================================================

# Лекция 4
# Циклы

#=============================================================================================

money = 10
while money > 0:
    print("Денег осталось ", money)
    money -= 1
print("Денег нет")

x = 7
while x != 0:
    if x % 2 == 0:
        print(x, "- четное число")
    else:
        print(x, "- нечетное число")
    x -= 1

sum_ = 0
number = 1
while number:
    number = int(input("Введите число: "))
    sum_ += number
print(sum_)

sum_ = 0
number = int(input("Введите число: "))
sum_ += number
while number:
    number = int(input("Введите число: "))
    sum_ += number
print(sum_)

# по этой теории какое бы число не ввели, получим 1
count = 0
n = int(input("Введите число: "))
while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n = (n * 3 + 1) / 2
    count += 1
print(n, count)


# ===================
# For
# ===================



company_name = "Netology"
for name in company_name:
    print(name)

company_name = "Netology"
for name in company_name:
    print(f"*{name.upper()}*", end='')


items = [1, 5, 9, 3, 67, 333, 557, 76]
ok_items = []
for item in items:
    print("Груз весит", item, "килограмм")
    if item <= 100:
        ok_items.append(item)
        print("Груз прошел проверку")
    else:
        print("Груз слишком большой")
print(ok_items)


text = "Python, высокоуровневый язык, программирования общего назначения, с динамической строгой типизацией и автоматическим управлением памятью"
n = 4
words = []
for word in text.split():  # split - разделяет по пробелам
    print(word)
    word = word.strip(',.!') # strip отрезает все символы вокруг слов
    if len(word) > n:
        words.append(word)
print(words)


companies_capitalization = [
    ['Orange', 1.3],
    ['Maxisoft', 1.5],
    ['Headbook', 0.8],
    ['Nicola', 2.2]
]
for company in companies_capitalization:
    # print(company)
    print(f"{company[0]}'s capitalization {company[1]}")

for name, cap in companies_capitalization:
    # print(company)
    print(f"{name}'s capitalization {cap}")

# Суммирование от 0 индекса
data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35]
]
sum_ = 0
index = 0
for row in data:
    sum_ += row[index]
    index += 1
print(sum_)

# Суммирование от -1 индекса
data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35]
]
sum_ = 0
index = -1
for row in data:
    sum_ += row[index]
    index -= 1
print(sum_)

professions = ['IT', 'Физика', 'Математика']
persons = [['Гейтс', 'Джобс', 'Возняк'], ['Энштейн', 'Фейнман'], ['Эвклид', 'Ньютон']]
for pro, names in zip(professions, persons):
    print(f'{pro}:')
    for name in names:
        print(name)
    print()

for pro, names in zip(professions, persons):
    print(f'{pro}:')
    print('\n'.join(names))
    print()

# таблица умножения
for row in range(1, 10):
    # print(row)
    for col in range(1, 10):
        print(row * col, end='\t')
    print()

# =========================
# break / continue
# =========================
phrace = "640кб должно хватить на всех. Легенда. Билл Гейтс."
for letter in phrace:
    if letter == ' ':
        break
    print(letter, end='')

phrace = "640кб должно хватить на всех. Легенда. Билл Гейтс."
for letter in phrace:
    if letter == ' ':
        continue
    print(letter, end='')


import random
number = random.randint(1, 100)
print(number)
max_tries = 3
tries = 0
while tries < max_tries:
    guess = int(input("Назовите свой вариант: "))
    if guess < number:
        print("Загаданное число больше")
    elif guess > number:
        print("Загаданное число меньше")
    else:
        print("Вы угадали!")
        break
    tries += 1
else:
    print(f"Вы проиграли, загаданное число {number}")


login_correct = 'admin'
pswd_correct = 'admin'
k = 3
for i in range(k):
    login = input('Введите логин: ')
    pswd = input('Введите пароль: ')
    if login != login_correct or pswd != pswd_correct:
        k -= 1
        print(f'Осталось {k} попытки')
    else:
        print('Добро пожаловать')
        break
else:
    print('Вход заблокирован')



# вывести среднее значение 3 столбца
api_response = [
    ['2017-12-26', '777', 184],
    ['2017-12-27', '111', 146],
    ['2017-12-28', '777', 98],
    ['2017-12-29', '777', 206],
    ['2017-12-30', '111', 254],
    ['2017-12-31', '777', 89],
    ['2018-01-01', '111', 54],
    ['2018-01-02', '777', 68],
    ['2018-01-03', '777', 74],
    ['2018-01-04', '111', 89],
    ['2018-01-05', '777', 104],
    ['2018-01-06', '777', 99],
    ['2018-01-07', '777', 145],
    ['2018-01-08', '111', 184],
]
sum_ = 0
for i in api_response:
    sum_ += i[2]
result = round(sum_ / len(api_response), 2)
print(result)