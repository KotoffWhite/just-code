def find_neighbours(numbers, req_row: int, req_col: int) -> list:
    res_list = []
    if req_col != 0:
        try:
            res_list.append(numbers[req_row][req_col-1])
        except:
            pass
    try:
        res_list.append(numbers[req_row][req_col+1])
    except:
        pass
    if req_row != 0:
        try:
            res_list.append(numbers[req_row-1][req_col])
        except:
            pass
    try:
        res_list.append(numbers[req_row+1][req_col])
    except:
        pass
    return (sorted(res_list))


if __name__ == '__main__':
    rows = int(input())
    columns = int(input())
    numbers_list = [[]]
    numbers_list = [[int(c) for c in input().split()] for _ in range(rows)]
    req_row = int(input())
    req_col = int(input())
    print(*find_neighbours(numbers_list, req_row, req_col))
