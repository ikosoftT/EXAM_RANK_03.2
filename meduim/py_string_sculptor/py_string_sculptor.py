def string_sculptor(text: str) -> str:
    l = []
    i = 0
    j = 0
    char = ''
    while i < len(text):
        if text[i].isalpha():
            if j % 2 == 0:
                char = text[i].lower()
            else:
                
                char = text[i].upper()
            j+=1
            l += char
        else:
            l += text[i]
        i+=1
    return "".join(l)

print(string_sculptor("aBc123def"))


