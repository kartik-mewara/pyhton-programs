letter='''Dear <|name|>
you are selected on the date
Date: <|date|> '''
name=input("Enter name of person\n")
date=input("Enter date of joining\n")
# print(letter)
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)
print(letter) 