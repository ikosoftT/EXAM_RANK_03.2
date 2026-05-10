def echo_validator(text: str) -> bool:
    i = 0
    j = len(text) - 1
    while i < len(text):
        if not text[i].isalpha() or not text[j].isalpha():
            if not text[i].isalpha():
                i += 1
            else:
                j -= 1
            continue
        if text[i].lower() == text[j].lower():
            i+=1
            j-=1
        else:
            return False
    return True

print(echo_validator("racecar")) 
print(echo_validator("A man a plan a canal Panama"))
print(echo_validator("race a car"))
print(echo_validator("Was it a car or a cat I saw"))