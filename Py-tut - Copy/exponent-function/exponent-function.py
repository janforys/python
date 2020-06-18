def raise_to_power(base_number, pow_number):
    result = 1
    for i in range(pow_number):
        result = result * base_number
    return result

print(raise_to_power(2, 4))
