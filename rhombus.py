def rhombus(int):
    first = int // 2
    end = int // 2 + 1
    for i in range(int // 2):
        print((first * " ") + ((end - first) * "*"))
        first -= 1
        end += 1
    for i in range(int // 2 + 1):
        print((first * " ") + ((end - first) * "*"))
        first += 1
        end -= 1


def main():
    num = int(input("Enter a number"))
    rhombus(num)
    main()


if __name__ == "__main__":
    main()
