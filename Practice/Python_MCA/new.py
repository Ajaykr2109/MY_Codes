#largest common substring in n strings
def lcs(a,b):
    n=len(a)
    m=len(b)
    dp=[[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=0
    return dp[n][m]
def main():
    n=eval(input("Enter the number of strings: "))
    arr=[]
    for i in range(0,n):
        x=input("Enter the string: ")
        arr.append(x)
    ans=arr[0]
    for i in range(1,n):
        ans=lcs(ans,arr[i])
    print(ans)
main()
