def get_list_of_primals(max_numb: int) -> list:
    main_list = list(range(0, max_numb+1))
    main_list[0] = None
    main_list[1] = None
    for numb in main_list:
        if numb is not None:
            for pos in range(numb*numb, max_numb+1, numb):
                main_list[pos] = None
    main_list = list(filter(lambda item: item is not None, main_list))
    return main_list


if __name__ == '__main__':
    numb = int(input())
    print(*get_list_of_primals(numb))
