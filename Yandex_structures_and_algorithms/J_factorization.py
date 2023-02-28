def factorize(req_numb: int) -> list:
    res_list = []
    numb = 2
    while numb*numb <= req_numb:
        if req_numb % numb == 0:
            res_list.append(numb)
            req_numb //= numb
        else:
            numb += 1
    if req_numb > 1:
        res_list.append(req_numb)
    return res_list


if __name__ == '__main__':
    numb = int(input())
    print(*factorize(numb))
