def get_sum(numb_str: list, numb2: int) -> list:
    numb1 = int(''.join(numb_str))
    res_numb = numb1 + numb2
    return list(str(res_numb))


if __name__ == '__main__':
    N = int(input())
    list_form = input().split()
    K = int(input())
    print(*get_sum(list_form, K))
