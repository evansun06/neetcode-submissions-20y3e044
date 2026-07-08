class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # collect number of unique characters:
        char_set = set()

        for char in s:
            char_set.add(char)

        max_len = 0
        for char in char_set:
            char_count = 0
            other_count = 0
            left = 0
            for right in range(len(s)):
                # update the map
                if s[right] == char:
                    char_count += 1
                else:
                    other_count += 1
                
                while other_count > k:
                    if s[left] == char:
                        char_count -= 1
                    else:
                        other_count -= 1

                    left += 1
                
                if (char_count + other_count) > max_len:
                    max_len = char_count + other_count

        return max_len



