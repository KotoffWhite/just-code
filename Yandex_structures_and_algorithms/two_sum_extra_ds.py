def two_sum_extra_ds(numbers: list, x: int):
    """Функция возвращает пару чисел из списка numbers, сумма
    которых равна x"""
    previous = set()
    for a in numbers:
        y = x - a
        if y in previous:
            return f'{y} {a}'
        else:
            previous.add(a)
    return None


if __name__ == "__main__":
    N = int(input())
    numb_list = list(map(int, input().split()))
    x = int(input())

    print(two_sum_extra_ds(numb_list, x))
