# Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint as rand


def get_secret_number() -> int:
    return rand(0, 1001)


def clues(num: int, secret: int) -> bool:
    if num == secret:
        return True
    elif num > secret:
        print(f"The number is smaller than:\n{num}")
    else:
        print(f"The number is bigger than:\n{num}")
    return False


def main():
    num: int = 0
    secret: int = get_secret_number()

    print("Program is running."
          "I came up with a number try to guess it."
          "You have ten tries to do it.")
    for i in range(10, 0, -1):
        num = int(input("Try to guess the number i came up with.\n"))
        if clues(num, secret):
            print("Correct!")
            break
        else:
            print(f"Wrong. Try again you have {i} tries left")

    print(f"The number was {secret}")
    if input("Do you want to try again ?\n").lower() == "y":
        main()

    return 0


if __name__ == "__main__":
    main()
