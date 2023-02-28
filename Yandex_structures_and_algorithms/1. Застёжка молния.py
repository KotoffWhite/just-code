# def moving_average(timeseries, K):
#     result = []  # Пустой массив.
#     # Первый раз вычисляем значение честно и сохраняем результат.
#     current_sum = sum(timeseries[0:K])
#     result.append(current_sum / K)
#     for i in range(0, len(timeseries) - K):
#         current_sum -= timeseries[i]
#         current_sum += timeseries[i+K]
#         current_avg = current_sum / K
#         result.append(current_avg)
#     return result


# n = int(input())
# main_str = input()
# main_list = main_str.split(' ')
# slice_m = int(input())
# main_list = [int(x) for x in main_list]
# result = moving_average(main_list, slice_m)
# for el in result:
#     print(el, end=' ')


# def moving_average(list_numb, k):
#     result = []
#     cur_sum = sum(list_numb[0:k])
#     cur_avg = cur_sum/k
#     result.append(cur_avg)
#     for i in range(0, N-k):
#         cur_sum -= list_numb[i] - list_numb[i+k]
#         cur_avg = cur_sum/k
#         result.append(cur_avg)
#     print(*result)


# N = int(input())
# list_numb = list(map(int, input().split()))
# # Окно сглаживания
# K = int(input())

# moving_average(list_numb, K)


# def two_sum(numbers: list, x: int) -> list:
#     result = []
#     for i in range(0, len(numbers)-1):
#         for k in range(i+1, len(numbers)):
#             cur_sum = numbers[i] + numbers[k]
#             if cur_sum == x:
#                 result.append([numbers[i], numbers[k]])
#     return result


# numbers = list(map(int, input().split()))
# x = int(input())

# print(*two_sum(numbers, x))

# n = int(input())
# main_str = input()
# main_list = main_str.split(' ')
# slice_m = int(input())
# main_list = [int(x) for x in main_list]
# def twosum(numbers, X):
# 	for i in range(0, len(numbers)):
# 		for j in range(i+1, len(numbers)):
# 			if numbers[i] + numbers[j] == X:
# 				str_1 = str(numbers[i]) + ' ' + str(numbers[j])
# 				return str_1 
# 	return None
# x = twosum(main_list, slice_m)
# print(x)

# N = int(input())
# numb_list = list(map(int, input().split()))
# x = int(input())


# def sum_two(numbers: list, x: int):
#     for i in range(0, len(numbers)):
#         for k in range(i+1, len(numbers)):
#             if numbers[i] + numbers[k] == x:
#                 return f'{numbers[i]} {numbers[k]}'
#     return None


# print(sum_two(numb_list, x))

# def sum_two(numbers: list, x: int):
#     numbers.sort()
#     left = 0
#     right = len(numbers)-1
#     while left < right:
#         cur_sum = numbers[left] + numbers[right]
#         if cur_sum == x:
#             return f'{numbers[left]} {numbers[right]}'
#         elif cur_sum < x:
#             left += 1
#         else:
#             right -= 1
#     return None


# N = int(input())
# numb_list = list(map(int, input().split()))
# x = int(input())

# n = int(input())
# main_str = input()
# main_list = main_str.split(' ')
# slice_m = int(input())
# main_list = [int(x) for x in main_list]


# def twosum_extra_ds(numbers, X):
#     # Создаём вспомогательную структуру данных с быстрым поиском элемента.
#     previous = set()

#     for A in numbers:
#         Y = X - A
#         if Y in previous:
#             str_1 = str(A) + ' ' + str(Y)
#             return str_1
#         else:
#             previous.add(A)

#     # Если ничего не нашлось в цикле, значит, нужной пары элементов в массиве нет.
#     return None


# x = twosum_extra_ds(main_list, slice_m)
# print(x)



