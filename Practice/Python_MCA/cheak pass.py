def printStrongNess(pass_string):
     
    n = len(pass_string)
    
    low = False
    high=False
    num=False
    special=False
    normal="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
     
    for i in range(n):
        if pass_string[i].islower():
            low=True
        if pass_string[i].isupper():
            high=True
        if pass_string[i].isdigit():
            num=True
        if pass_string[i] not in normal:
            special=True
 
    print("Strength of password: ", end = "")
    if (low and high and
        num and special and n >= 8):
        print("Strong")
         
    elif ((low or high) and
          special and n >= 6):
        print("Moderate")
    else:
        print("Weak")
        
if __name__=="__main__":
     
    pass_string = input("Enter the password you want to cheak : ")
     
    printStrongNess(pass_string)