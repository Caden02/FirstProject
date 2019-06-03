import numpy as np, os, json



lis = []
print('Enter six numbers: ')
for i in range(1,7):
    a = int(input())
    lis.append(a)
print(sorted(lis))













N = int(input())
b = N%2

if b == 0:
    if N in range(2,5):
        print('Not Wierd')
    elif N in range(6, 20):
        print('Wierd')
    elif N > 20:
        print('Not Wierd')
else:
    print('Wierd')

c = int(input().strip())
check = {True: 'Not Wierd', False: 'Wierd'}

print(check[
    c%2==0 and (
        c in range(2,6) or
            c > 20)
      ])





print(os.getcwd())



with open(r'C:\Users\Caden\Documents\testfile.txt', 'r+') as test:
    data = test.readlines()
    print(json.dump('hello', test))

    for line in data:
        words = line.split()
        print(words)








print('{:-^30}'.format('centered'))
print('{2}, {1}, {0}'.format('a', 'b', 'c'))


print('this {food} is {condition}.'.format(food='bacon', condition='good'))

for x in range(1, 11):
    print('{0:<2d} {1:<3d} {2:<4d}'.format(x, x*x, x*x*x))

inc = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(list(map(list, zip(*inc))))
base = []
for i in range(3):
    sec = []
    for row in inc:
        sec.append(row[i])
    base.append(sec)

print(base)





vec = [-4, -2, 0, 2, 4]

bar = [
    'John'
    'Max'
    'Mike'
    'Bill'
]


print([weapon.strip() for weapon in bar])

squares =[]

print([x**2 for x in range(10)])













