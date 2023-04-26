# Task 1
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) != len(girls):
    print("Кто-то может остаться без пары")
else:
    print('Идеальные пары')
for boy, girl in zip(sorted(boys), sorted(girls)):
    print(f'{boy} и {girl}')




# Task 2
cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]
person = 5
for cook in cook_book:
    print(f'\n{cook[0]}:')
    for i in cook[1]:
        print(f'{i[0]}, {i[1] * person} {i[2]}')


person = 5
for cook in cook_book:
  cook[0] = cook[0].capitalize()
  print(f'\n{cook[0]}:\n')
  for i in cook[1]:
    print(f'{i[0]}, {i[1] * person} {i[2]}')


person = 5
for dish, ingrs in cook_book:
  print(f'{dish.capitalize()}:')
  for name, q, measure in ingrs:
    print(f'{name}, {q*person} {measure}')
  print()