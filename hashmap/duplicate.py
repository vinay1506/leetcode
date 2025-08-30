def duplicateO(string: str) -> bool:
    n=len(string)
    map={}
    for i in range(n):
        if string[i] in map:
            return True
        map[string[i]]=i
    return False

s="vinay"
print(duplicateO(s))  # Output: False