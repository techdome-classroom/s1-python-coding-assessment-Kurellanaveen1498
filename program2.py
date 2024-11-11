def is_match(message: str, key: str) -> bool:
    m = len(message)
    k = len(key)
    
    dp = [[False] * (k + 1) for _ in range(m + 1)]
    
    dp[0][0] = True
    
    for j in range(1, k + 1):
        if key[j - 1] == '*':
            dp[0][j] = dp[0][j - 1] 
    
    for i in range(1, m + 1):
        for j in range(1, k + 1):
            if key[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif key[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j - 1] and message[i - 1] == key[j - 1]

    return dp[m][k]

print(is_match("aa", "a"))      # False
print(is_match("aa", "*"))      # True
print(is_match("cb", "?a"))     # False
print(is_match("abc", "a*"))    # True
print(is_match("abc", "*b"))    # True
print(is_match("abc", "abc?"))  # True
