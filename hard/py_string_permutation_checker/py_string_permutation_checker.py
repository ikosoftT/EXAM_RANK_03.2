def string_permutation_checker(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    i = 0
    c = 0
    seen = []
    while i < len(s1):
        j = 0
        while j < len(s2):
            if s1[i].isalpha() and s2[j].isalpha(): 
                if s1[i] == s2[j]:
                    if not s1[i] in seen:
                        c +=1
                        seen.append(s1[i])
            else:
                break
            j+=1
        i+=1
    
    return  c == len(s1)

# print(string_permutation_checker("abc", "bca"))
# print(string_permutation_checker("abc", "def"))
# print(string_permutation_checker("listen", "silent"))
# print(string_permutation_checker("hello", "bello"))
# print(string_permutation_checker("", ""))
# print(string_permutation_checker("a", ""))
print(string_permutation_checker("a gentleman", "elegant man"))
# print(string_permutation_checker("Abc", "abc"))
# print(string_permutation_checker("aaa", "abc"))