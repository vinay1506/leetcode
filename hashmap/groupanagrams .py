from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    if not strs:
        return []
    anagrams = {}
    for word in strs:
        # Use sorted word as the key
        key = "".join(sorted(word))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    return list(anagrams.values())

# Example usage:
strs = ["eat", "tea", "tan", "ate", "vat", "bat"]
print(groupAnagrams(strs))
# Output: [["eat", "tea", "ate"], ["nat", "tan"], ["bat"]]
