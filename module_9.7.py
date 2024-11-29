def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

result = sum_three(2, 3, 4)
print(result)

result = sum_three(5, 7, 3)
print(result)

result = sum_three(10, 15, 5)
print(result)

result = sum_three(12, 13, 14)
print(result)