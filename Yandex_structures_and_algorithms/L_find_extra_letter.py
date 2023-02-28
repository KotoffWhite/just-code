def find_extra_letter(line1: str, line2: str) -> str:
    line1 = sorted(line1)
    line2 = sorted(line2)
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            return line2[i]
    return line2


if __name__ == '__main__':
    line1 = input()
    line2 = input()
    print(find_extra_letter(line1, line2))
