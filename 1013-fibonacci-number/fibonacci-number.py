class Solution:
    def fib(self, n: int) -> int:
        return self.fibo(n,{})
        
    def fibo(self,n,memo):
        if n == 1 or n == 0 :
            return n
        if n not in memo:
            memo[n] = self.fibo(n-1,memo) + self.fibo(n-2,memo)
        return memo[n]

        
   

    
        