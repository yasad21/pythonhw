def my_steps(n):
        
        if(n<1 or n>25):
            raise ValueError()
        dp = {}
        dp[1] = 1
        dp[2] = 2

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp [i-2]
    
        return dp[n]
