import math

#Ввод данных с пользователем в консоль

d1 = True
d2 = True
d3 = True

print("Напишите первый коэффициент: ")
while d1:
    try:
        a = int(input())
        d1 = False
    except:
        print("Введенное значение некорректно. Попробуйте ввести новое значние:")
        
print("Напишите второй коэффициент: ")
while d2:
    try:
        b = int(input())
        d2 = False
    except:
        print("Введенное значение некорректно. Попробуйте ввести новое значние:")

print("Напишите третий коэффициент: ")
while d3:
    try:
        c = int(input())
        d3 = False
    except:
        print("Введенное значение некорректно. Попробуйте ввести новое значние:")
        
print("Вы ввели",a,b,c)

#Решение биквадратного уравнения через дискриминант, при замене t^2 = x

#Проверка нулевых коэффициентов

if a == 0:
    if b == 0:
        print("Это не уравнение. Прошу,будьте серьезны")
    else:
        x = -c/b
        sqrX = math.sqrt(x)
        if x == 0:
            t1 = 0
            print("Корень один t =")
        else:
            t1 = sqrX
            t2 = -sqrX
            print("Два корня t1 = {} и t2 = {}".format(t1,t2))
            
elif b == 0:
    if c == 0:
        print("Корень t = 0")
    else:
        try:
            x = math.sqrt(-c/a)
            sqrX = math.sqrt(x)
            t1 = sqrX
            t2 = -sqrX
            print("Два корня t1 = {} и t2 = {}".format(t1,t2))
        except:
            print("Нет корней")
elif c == 0:
    t1 = 0
    try:   
        sqrX = math.sqrt(-a/b)
        t2 = sqrX
        t3 = -sqrX
        print("Три корня t1 = {}, t2 = {} и t3 = {}".format(t1,t2,t3))
    except:
        print("Корень лишь нулевой и он один")

#Решение через дискриминант при всех ненулевых коэффициентах

else:
    D = b**2 - 4*a*c
    print('Дискриминант равен:',D)

    if D > 0:
            x1 = (-b + math.sqrt(D))/(2*a)
            x2 = (-b - math.sqrt(D))/(2*a)
            if x1 > 0:
                t1 = math.sqrt(x1)
                t2 = -math.sqrt(x1)
                print('Первый и второй корень соответственно: t1=',t1,'t2=',t2)
            else:
                print('Корень х1 не дает действительных корней')
            if x2 > 0:
                t3 = math.sqrt(x2)
                t4 = -math.sqrt(x2)
                print('Еще два корня: t3=',t3,'t4=',t4)
            else:
                print("Корень х2 не дает действительных корней")
                
        
    elif D == 0:
        try:
            x = -b/(2*a)
        except:
            print('Беда')
        
        if x == 0:
            print('Один  корень: x1=', x)
        elif x > 0:
            t1 = math.sqrt(x)
            t2 = -math.sqrt(x)
            print('Два конечных корня:',t1,t2)
    
    else:
        print('Нет корней')
