class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        f = [0] * (k+1)
        d = 0

        while f[k] < n:
            d += 1
            for e in range(k, 0 , -1):
                f[e] = f[e-1] + f[e] + 1

        return d