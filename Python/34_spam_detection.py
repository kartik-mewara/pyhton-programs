# st=input("Enter the string to detect spam key words in it")
st="hello buy"
a=st.find("buy now")
b=st.find("make a lot of money")
c=st.find("subscribe this")
d=st.find("click this")
if(a>-1 or b>-1 or c>-1 or d>-1):
    print("this is spam")
else:
    print("not spam")    