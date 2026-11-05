class Solution:
    def twoEggDrop(self, n: int) -> int:
        f = [0] * 3
        d = 0

        while f[2] < n:
            d += 1
            for e in range(2, 0 , -1):
                f[e] = f[e-1] + f[e] + 1

        return d