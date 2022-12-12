#while True:
#    x = float(input())
#    count = 0
#    y = 1

#    while count < x:
#        count +=1
#        y *= count

#    else:
 #       print (x, y)


x= ''

while len(x) < 5:
    y = input('Enter a number:')
    if y == '0':
        continue
    if y == '1':
        break

    x+=y

else:
    print(x)

print(y)