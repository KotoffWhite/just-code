def check_if_power_of_four(numb: int) -> bool:
    if numb == 0:
        return False
    while numb % 4 == 0:
        numb /= 4
    if numb == 1:
        return True
    return False


if __name__ == '__main__':
    numb = int(input())
    print(check_if_power_of_four(numb))
