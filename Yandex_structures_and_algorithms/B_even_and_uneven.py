def same_evennes(numbers: list) -> str:
    evenness = 0
    for numb in numbers:
        if numb % 2 == 0:
            evenness += 1
    if evenness == len(numbers) or evenness == 0:
        return 'WIN'
    return 'FAIL'


if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    print(same_evennes(numbers))
