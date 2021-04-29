f=open("highscore.txt","r")
score=f.read()
new_score=667
f.close()
new_score=str(new_score)
if(score==""):
    print("empty we will add score")
    f=open("highscore.txt","w")
    f.write(new_score)
    f.close()
else:
    f=open("highscore.txt","r")
    l1=f.readlines()
    # print(len(l1))
    f.close()
    if(int(new_score)>int(l1[len(l1)-1])):
        print("adding")
        f=open("highscore.txt","a+")
        f.write(f"{new_score}\n")
        f.close()

    else:
        print("not adding")

    



