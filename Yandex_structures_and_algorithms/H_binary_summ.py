def binary_sum(numb1: str, numb2: str) -> str:
    num_1 = [*map(int, numb1)][::-1]
    num_2 = [*map(int, numb2)][::-1]
    max_size = max(len(num_1), len(num_2))
    num_1 += [0] * (max_size - len(num_1))
    num_2 += [0] * (max_size - len(num_2))
    res_str = ''
    overflow = 0
    for c, d in zip(num_1, num_2):
        cur_res = c + d + overflow
        overflow = cur_res // 2
        res_str += str(cur_res % 2)
    if overflow == 1:
        res_str += '1'
    return res_str[::-1]


if __name__ == "__main__":
    numb1 = input()
    numb2 = input()
    print(binary_sum(numb1, numb2))
