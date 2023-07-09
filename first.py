def check_triangle(arr: list[int]) -> None:
    arr_set = set(arr)

    if len(arr_set) == 2:
        print("Triangle is an isosceles triangle")
    elif len(arr_set) == 1:
        print("Triangle is a equilateral Triangle")
    else:
        print("Triangle is a scalene triangle")


def main():
    t_arr: tuple[str, str, str] = ("A", "B", "C")
    arr: list[int] = [0, 0, 0]
    num: int = 0

    print("Program is running.")

    for i in range(len(arr)):
        try:
            arr[i] = int(input(f"Enter {t_arr[i]} side of the triangle:\n"))
        except ValueError:
            print("Please enter integers.")
            main()

    for i in arr:
        if i <= 0:
            print("Not allowed number. Side must be more than zero!")
            main()

    for i in range(len(arr)):
        num = 0
        for j in range(len(arr)):
            if i == j:
                pass
            else:
                num += arr[j]
        if arr[i] > num:
            print(f"Side {t_arr[i]} = {arr[i]} is not allowed, such triangle can not exist.")
            main()

    check_triangle(arr)
    for i in range(len(arr)):
        print(f"Side {t_arr[i]} is equal to {arr[i]}")

    return 0


if __name__ == "__main__":
    main()
