import numpy as np
def edit_distance(s1, s2):
    """
    Compute the minimum edit distance between two strings.
    """
    m = len(s1)
    n= len(s2)

    dp = np.zeros((m+1,n+1))
    dp[0,:]= [i for i in range(0,n+1)]
    dp[:,0]= [i for i in range(0,m+1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i, j] = dp[i-1, j-1] if s1[i-1] == s2[j-1] else 1 + min(dp[i-1, j], dp[i, j-1], dp[i-1, j-1])


    return int(dp[m][n])              
                
            
    