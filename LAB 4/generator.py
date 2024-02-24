#1
def squares(N):
    for i in range(N):
        yield i ** 2

a = int(input())
c = squares(a)
for num in c:
    print(num)

#2
def even(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

a = int(input())
c = even(a)
print(','.join(map(str, c)))

#3
def div_3_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

a = int(input())
c = div_3_4(a)
for numers in c:
    print(numers)

#4
def squares(a, b):
    for num in range(a, b+1):
        yield num ** 2

a = int(input())
b = int(input())

for sq in squares(a, b):
    print(sq)


#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

a = int(input())
for nu in countdown(a):
    print(nu)