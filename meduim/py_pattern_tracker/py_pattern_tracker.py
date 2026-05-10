def pattern_tracker(text: str) -> int:
    count = 0
    i = 0
    while i < len(text) -  1:
        if text[i].isdigit() and text[i + 1].isdigit():
            if text[i + 1] > text[i]:
                count += 1
        i+=1 
    return count

print(pattern_tracker("01234567"))