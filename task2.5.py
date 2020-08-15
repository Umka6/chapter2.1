# s = 'Быстрый Brow Box'
# def count_letters(s):
#     s.isuper = s.upper
#     s.islower = s.lower
#     s.count = 0
#     return len(s) - s.count(' ')
#
# print('В верхней строке', len(s.upper()), 'символов')
# print('В нижней строке', len(s.lower()), 'символов')

def up_low(s):
    u = sum(1 for i in s if i.isupper())
    l = sum(1for i in s if i.islower())
    print("Количество символов в верхнем регистре:%s, Количество символов в нижнем регистре: %s" % (u,l))

up_low("Быстрый Brow Fox")