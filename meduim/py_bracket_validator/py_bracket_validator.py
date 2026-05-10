def bracket_validator(s: str) -> bool:
    stack = []
    for c in s:
        if c in ["(", "{", "["]:
            stack.append(c)
        else:
            if c in [")", "}", "]"]:
                if stack:
                    last = stack[len(stack) - 1]
                else:
                    return False
                if (last == '(' and c == ')') or (last == "{"  and c == "}") or (last == "[" and c == "]"):
                    stack.pop()
                else:
                    return False
           
    return len(stack) == 0

print(bracket_validator("(] )"))
