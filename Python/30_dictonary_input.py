lang_dict={}

a=input("Enter name of first person\n")
b=input("Enter language of the person\n")
c=input("Enter name of second person\n")
d=input("Enter language of the person\n")
e=input("Enter name of third person\n")
f=input("Enter language of the person\n")
print(lang_dict)
updated_dict={
    a:b,
    c:d,
    e:f
}
lang_dict.update(updated_dict)
print(lang_dict)

# s1={8,7,6,"harry",[1,2]} this will give error as list cant be added as it is unhashable i.e mutable or changebale we can enter only item which is unchangeble