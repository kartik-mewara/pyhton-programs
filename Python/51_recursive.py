def sumn(num):
    if(num==1):
        return 1
    elif(num==0):
        return 0
    return num+sumn(num-1)
    

st=sumn(6)
print(st)