#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Sam', 'Nick', 'Veronika', 'Kuzya']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
     ['Sam', 23],
     ['Nick', 176],
     ['Veronika', 170],
     ['Kuzya', 90],
]


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('рост ', my_family_height[1][0], ' - ', my_family_height[1][1],' см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см


height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]
print('Общий рост моей семьи - ', height,'см')

# зачет!
