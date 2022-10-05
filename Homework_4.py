# задача 4. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

n = int(input('Введите первое число: '))
m = int(input('Введите второе число: '))  
def calc_lcm(n,m):
    if n > m:
        num = n
    else:
        num = m 
    while(True):
        if (( num % n == 0 and num % m == 0)):
            lcm = num
            break
        num += 1
    return lcm
  
print('НОК чисел', n, "и", m, 'Является число:', calc_lcm(m,n))        
