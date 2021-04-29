try:
    open("poem.txt")
    a=1/0
# except Exception as e:
#     print(e)
except ZeroDivisionError as e:
    print("you cannot divide a number by zero")
else:
    print("great exist file ")
finally:
    print("done")