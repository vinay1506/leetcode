
def maxsubstring(s:str) -> int:
    n=len(s)
    maxv=0
    left=0
    map={}
    for right in range(n):
        if s[right] in map:
            left+=1
        map[s[right]]=right
        maxv= max(maxv, right-left+1)
    return maxv
s = "abcabcbb"
result = maxsubstring(s)
print(result)  # Output should be 3, as the longest substring without repeating characters is "abc"
    