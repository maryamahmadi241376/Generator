def less_or_greater(n):
    def get_divisors():
        if n <= 0:
            print("you can only enter positive numbers")
        else:
            for i in range(1, int(n / 2) + 1):
                if n % i == 0:
                    yield i

    s = 0
    if n <= 0:
        print("you can only enter positive numbers")
        pass
    else:
        for x in get_divisors():
            s += x
        if s == n:
            print(f'{n} is a perfect number')
        elif s < n:
            print(f'{n} is less than a perfect number')
        else:
            print(f'{n} is greater than a perfect number')


num = int(input("enter a number: "))
less_or_greater(num)
