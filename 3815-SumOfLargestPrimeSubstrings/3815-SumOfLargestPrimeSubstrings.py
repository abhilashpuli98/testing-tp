# Last Updated: 2/5/2026, 9:20:46 AM
class Solution(object):
    def is_prime(self,n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        # Miller-Rabin primality test
        d, s = n - 1, 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in [2, 3, 5, 7, 11]:
            if a >= n:
                continue
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def sumOfLargestPrimes(self, s):
        primes = set()
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                num_str = s[i:j].lstrip('0')
                if num_str:
                    num = int(num_str)
                    if self.is_prime(num):
                        primes.add(num)
        return sum(sorted(primes, reverse=True)[:3])
            
        