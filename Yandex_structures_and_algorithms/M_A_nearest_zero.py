def get_zero_distance(numbers: str) -> list:
    res_list = list()
    numbers = [int(numb) for numb in numbers.split()]
    ind_zero_left = numbers.index(0)
    ind_zero_right = numbers.index(0)
    for i in range(len(numbers)):
        if ind_zero_left == ind_zero_right:
            min_dist = ind_zero_right-i
        else:
            min_dist = min(i-ind_zero_left, ind_zero_right-i)
        res_list.append(min_dist)
        if numbers[i] == 0:
            ind_zero_left = i
            try:
                ind_zero_right = numbers.index(0, ind_zero_left+1)
            except ValueError:
                ind_zero_right = len(numbers)*2
    return res_list


if __name__ == '__main__':
    N = int(input())
    house_numbs = input()
    print(*get_zero_distance(house_numbs))
