def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    done = list1 + list2
    done.sort()
    return done

print(shadow_merge([1, 3, 5], [2, 4, 6]))
print(shadow_merge([1, 2, 3], [4, 5, 6]))