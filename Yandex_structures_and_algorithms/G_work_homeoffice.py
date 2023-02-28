def decimal_to_binary(number: int) -> str:
    res_str = ''
    if number == 0:
        return '0'
    while number > 0:
        res_str += str(number % 2)
        number = number // 2
    return res_str[::-1]


if __name__ == '__main__':
    numb = int(input())
    print(decimal_to_binary(numb))
