from random import randint as rand


def allowed_num(num: int) -> bool:
    foo: int = 100_000_000
    if num < -foo or num > foo:
        return False
    return True


def even_or_odd(num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False


# We will use Miller–Rabin test. Assume that zero is a prime.
def miller_rabin(num: int) -> bool:
    d: float = num - 1
    s: int = 0
    a: int = 0
    x: float = 0
    y: float = 0

    while even_or_odd(int(d)):
        s += 1
        d /= 2

    for i in range(0, 25):
        a = rand(2, num - 2)
        x = (a ** d) % num
        for j in range(s + 2):
            y = (x**2) % num
            if y == 1 and x != 1 and x != num - 1:
                return False
            x = y
        # if y != 1:
        #     return False
    return True


def test(num: int) -> bool:
    if num < 0:
        num *= -1
    if num <= 3:
        return True
    if even_or_odd(num):
        return False
    else:
        if miller_rabin(num):
            return True
        else:
            return False


def main():
    num: int = 0

    print("Program is running.")

    try:
        num = int(input("Enter an integer ∊ [-100_000_000; 100_000_000].\n"))
    except ValueError:
        print(f"{num} is not allowed. Please enter an integer.")

    if not allowed_num(num):
        print("Such large number is not allowed.")
        main()

    if test(num):
        print(f"{num} is a prime.")
    else:
        print(f"{num} is a composite number.")

    return 0


if __name__ == "__main__":
    main()
