"""
LeetCode 271 — Encode and Decode Strings
Pattern: Arrays & Hashing
Link: https://leetcode.com/problems/encode-and-decode-strings/

Approach: Length-prefix encoding. For each string, prepend its length 
followed by a '#' delimiter. On decode, read digits until '#', then 
slice exactly that many characters.

This works regardless of what characters appear in the strings 
(including '#' itself) because we always know how many chars to read.

Time:  encode O(n), decode O(n)   where n = total chars across all strings
Space: O(n) for the output
"""


class Solution:
    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        res, i = [], 0
        while i < len(s):
            j = s.find("#", i)
            if j == -1:
                raise ValueError("Malformed input: '#' delimiter not found during decoding.")
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res


# Local testing
if __name__ == "__main__":
    sol = Solution()

    # Basic case
    strs = ["Hello", "World", "Python", "Programming"]
    encoded = sol.encode(strs)
    print(f"Encoded: {encoded}")
    print(f"Decoded: {sol.decode(encoded)}")
    assert sol.decode(sol.encode(strs)) == strs

    # Edge cases — these are what interviewers ask about
    assert sol.decode(sol.encode([])) == []                    # empty list
    assert sol.decode(sol.encode([""])) == [""]                # list with empty string
    assert sol.decode(sol.encode(["", "", ""])) == ["", "", ""]  # all empty
    assert sol.decode(sol.encode(["a#b", "c#d"])) == ["a#b", "c#d"]  # contains delimiter
    assert sol.decode(sol.encode(["🔥", "한국"])) == ["🔥", "한국"]   # unicode

    print("All tests passed ✅")