def parabolic_equ(a: int, x: int, b: int, c: int) -> int:
    return (a*x*x + b*x + c)


if __name__ == "__main__":
    a, x, b, c = map(int, input().split())
    print(parabolic_equ(a, x, b, c))
