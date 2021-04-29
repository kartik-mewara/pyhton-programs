hindi_dict={
    "pankha":"fan",
    "aadmi":"man",
    "kitab":"book",
    # "kitab":"copy"
}
print(hindi_dict.keys())
a=input("Enter what you want to search from above\n")
print(hindi_dict.get(a))
# print(hindi_dict.get("kitab"))