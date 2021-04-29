f=open("poem.txt","r")
txt=f.read()
# print(txt)
n=txt.find("twinkle")
# print(n)
if(n!=0):
    print('It contains "twinkle" ')
else:
    print('It does not contains "twinkle"')
f.close()