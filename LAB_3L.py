is_male = True
is_tall = True
#
if is_male and is_tall:
    print("You are tall male")
elif is_male and not is_tall:
    print ("is are a male but not a tall one")
elif not is_male and is_tall:
    print("Yor are tall woman")
else:
    print("you are not a tall woman")