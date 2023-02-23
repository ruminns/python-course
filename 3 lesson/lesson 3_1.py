print ("Какое число больше?")
print ("Наше число: 30, ваше:")

a = 30
b = int(input())

if b >= 100:
    print (b, 'больше 100')
elif 100 > b > 50:
    print (b, 'больше 50 и меньше 100')
else:
    print (b, 'меньше 50')

if a > b:
    print ('30 больше', b)
else:
    print (b, 'больше 30')