def number_base_converter(number: str, from_base: int, to_base: int) -> int:
    base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        return "ERROR"
    dec = 0
    number = number.upper()
    for c in number:
        if c not in base:
            return "ERROR"
        idx = base.index(c)
        if idx >= from_base:
            return "ERROR"
        dec = dec * from_base + idx

    res = ""
    while dec > 0:
        rem = dec % to_base
        res = base[rem] + res 
        dec //= to_base

    return res 

print(number_base_converter("2a", 16, 10))
print(number_base_converter("1010", 2, 10))
print(number_base_converter("FF", 16, 10))
print(number_base_converter("255", 10, 16))
print(number_base_converter("123", 10, 2))
print(number_base_converter("Z", 36, 10))
print(number_base_converter("123", 1, 10))
print(number_base_converter("G", 16, 10))
