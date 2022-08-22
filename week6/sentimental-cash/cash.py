from cs50 import get_float

while True:
    n = get_float('Change owed: ')
    n *= 100
    if n > 0:
        coins = [25, 10, 5, 1]
        counter = 0

        for c in coins:
            while n >= c:
                n -= c
                counter += 1
        print(counter)
        break
