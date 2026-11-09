n = int(input())

if n < 2:
    print("Ошибка")
else:
    first = True
    d = 2
    while n > 1:
        if n % d == 0:
            if not first:
                print(" ", end="")
            print(d, end="")
            first = False
            n //= d
        else:
            d += 1
    print()
