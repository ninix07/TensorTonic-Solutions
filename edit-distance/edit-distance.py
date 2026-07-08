import numpy as np
def edit_distance(s1, s2):
    """
    Compute the minimum edit distance between two strings.
    """
    m = len(s1)
    n= len(s2)

    dp = np.zeros((m+1,n+1))
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j]=j
                continue
            elif j ==0:
                dp[i][j]=i
                continue

            if s1[i-1]==s2[j-1]:
                dp[i][j]= dp[i-1][j-1]

            else:
                dp[i][j] =1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])



    return int(dp[m][n])              
                
            
    