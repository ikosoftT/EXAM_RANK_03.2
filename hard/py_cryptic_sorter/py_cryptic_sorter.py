def count(s):
    i = 0
    for c in s:
        if c in ("a","e", "i", "o", "u"):
            i += 1
    return i

def cryptic_sorter(strings: list[str]) -> list[str]:
    strings.sort(key=lambda s:(len(s), s.lower(), s.isupper(), count(s)))
    return strings


print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))
print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))
print(cryptic_sorter(["hello", "world", "hi", "test"]))
print(cryptic_sorter([]))