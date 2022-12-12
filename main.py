# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    print(f'Hi,. {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyC')


number = 4
number2 = 5
result = number + number2
print (result)

num1 = num2  = 5
print(num1, num2)

num_1, num_2 = 5 , 7
print(num_1, num_2)

swap1 = 8
swap2 = 9
swap1, swap2 = swap2, swap1 + swap1
print(swap1,swap2)

swap2 -= number
print (swap2)
#z , x , *c =[1,2,3,4,5,6,7,]
#print(z,x,c)

x =float (input ( 'Введите число'))
y =float (input ( 'Введите число'))
r = x + y
print ('Результат' + str(r))


if x==0:
    print('if')
elif x > 0:
    print('elif')
    x = 0

    print(x)
else:
    print('else')


