def main():
    b = list(map(float, input("Введіть елементи списку через пробіл: ").split()))

    last_pos = -1
    for i in range(len(b)):
        if b[i] > 0:
            last_pos = i

    if last_pos == -1:
        print("Додатних елементів немає. Сума = 0")
    else:
        s = 0
        for i in range(last_pos + 1):
            s += b[i]

        print("Індекс останнього додатного елемента:", last_pos)
        print("Сума елементів до нього включно:", s)


if __name__ == "__main__":
    main()