class Solution:
    def compress(self, chars: list[str]) -> int:
        counter = 1
        left = 0
        right = 0
        n = len(chars)

        if n < 2:
            return n

        while right < n:
            if right + 1 < n and chars[right] == chars[right + 1]:
                counter += 1
            else:
                chars[left] = chars[right]
                left += 1

                if counter > 1:
                    for digit in str(counter):
                        chars[left] = digit
                        left += 1

                counter = 1

            right += 1

        return left