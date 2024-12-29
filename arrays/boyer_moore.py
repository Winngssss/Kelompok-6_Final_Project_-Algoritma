class BoyerMoore:
    def run(self, text, pattern):
        n = len(text)
        m = len(pattern)
        skip = [m] * 256

        for i in range(m - 1):
            skip[ord(pattern[i])] = m - i - 1

        i = m - 1
        while i < n:
            j = m - 1
            while j >= 0 and text[i] == pattern[j]:
                i -= 1
                j -= 1
            if j == -1:
                return i + 1
            i += skip[ord(text[i])]
        return -1