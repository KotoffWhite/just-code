def count_chaotic_days(temp_list: list) -> int:
    chaotic_counter = 0
    if len(temp_list) == 1:
        return 1
    for i in range(1, len(temp_list)-1):
        if temp_list[i] > temp_list[i-1] and temp_list[i] > temp_list[i+1]:
            chaotic_counter += 1
    if temp_list[0] > temp_list[1]:
        chaotic_counter += 1
    if temp_list[len(temp_list)-1] > temp_list[len(temp_list)-2]:
        chaotic_counter += 1
    return chaotic_counter


if __name__ == "__main__":
    numb_days = int(input())
    temp_list = list(map(int, input().split()))
    print(count_chaotic_days(temp_list))
