def whisper_cipher(text: str, shift: int) -> str:
    res = ""

    for c in text:
        if 'a' <= c <= 'z':
            res += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            res += chr((ord(c) - ord('A') + shift )% 26 + ord('A'))
        else:
            res += c
    return res
