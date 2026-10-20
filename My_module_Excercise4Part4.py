### Part 4: Store your function in a module ###
#Copied from Part 3
def third_function(name):
    if name == "Anna":
        print(f"{name} may be your teacher")
        teacher = True
    else:
        print(f"{name} is not your teacher")
        teacher = False
    return teacher
