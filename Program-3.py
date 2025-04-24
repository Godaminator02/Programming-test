def generate_series(n: int):
    length = n if n % 2 == 1 else n - 1
    series = [2 * i + 1 for i in range((length + 1) // 2)]
    return series


a = int(input("Enter a number: "))
print(generate_series(a))
