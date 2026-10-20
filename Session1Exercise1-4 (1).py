## Session 1: Python basics exercise 1-4 ##

## Exercise 1: Variables and data types ## Made by Rebecca

### Part 1: Your first variable ###
# Making a string variable
my_name = "Rebecca"
print(my_name)

# Showing which type of variable "my_name" is
print(type(my_name))

### Part 2: Strings ###
print("Null hypothesis: Eating ice cream does not improve mood")
null_hypothesis = "Null hypothesis: Eating ice cream does not improve mood"
print(null_hypothesis[0:4])                                         # Printing the first 4 characters in "null_hypothesis"
print(null_hypothesis[-4:])                                         # Printing the last 4 characters in "null_hypothesis"

### Part 3: String methods ###
split_var = null_hypothesis.split(" ")                              # splitting my variable by every space " " in it and storing it in a new variable
print(split_var[1])                                                 # The output is "hypothesis" because Python starts counting on 0, so [1] is "hypothesis"
print(split_var[1][1])                                              # Printing the second character in "split_var"
colon_split_var = null_hypothesis.split(":")                        # Splitting "null_hypothesis" by the colon and storing it in a new variable
hypothesis_word = split_var[1]                                      # Indexing the word "hypothesis" out of "split_var" and storing it in a new variable
print(hypothesis_word)                                              # The colon is attached to "hypothesis:"
hypothesis_word_upper = hypothesis_word.upper()                     # Making a new variable, where I make the "hypothesis_word" into upper case letters
print(null_hypothesis.replace("hypothesis", hypothesis_word_upper)) # Replacing the word "hypothesis" with "hypothesis_word_upper"
print(hypothesis_word_upper[0])                                     # Seeing if "hypothesis_word_upper" starts with a "H". It does :D
print(len(null_hypothesis))                                         # Getting the lenght of "null_hypothesis"

### Part 4: Numbers ###
integer = 10                                                        # Making a variable with integers (whole numbers)
floating = 2.5                                                      # Making a variable with floating points ( numbers with decimals)
print(type(integer))
print(type(floating))
print(integer+floating)                                             # Adding them gives me a floating number
print(integer-floating)                                             # Substracting them gives me a floating number
print(integer/floating)                                             # Dividing them gives me a floating number "4.0"
multiplied = integer*floating                                       # Multiplying them and storing it in a new variable
print(multiplied)                                                   # Gives me a floating point "25.0"

### Part 5: f-strings ###
subject_id = "S_01"
rt = 2.578
print(f"The current subject is {subject_id}.")
print(f"The current subject is {subject_id} and their reaction time is {rt:.2f}")

### Bonus ###
print(f"We failed to reject the {split_var[0].upper()} {split_var[1].upper()}")


#------------------------------------------------------------------------------#
## Exercise 2: Lists ##   Made by Magnus

### Part 1: Defining lists ###
# Make variables containing 10-item lists, one of each:
# All string items.
animals=["cow", "bird","dog","cat","horse","rat","mouse","hamster","dolphin","pig"]

# All integer items.
int=[1,2,3,4,5,6,7,8,9,10]

# All floating-point items.
float=[1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]

# Mixed strings, integers and floats.
mix=["magnus","rasmus","nikolaj","marius",10,11,12,10.10,11.11,12.12]

combined_1=[animals,int,float]

### Part 2: Indexing lists ###
# Return the 4th item of each of lists 1-3.
print(animals[3],int[3],float[3])
# Return the first item of combined. Do you notice anything unexpected about the output?
print(combined_1[0])
# Now figure out how to index the first word only from combined.
print(combined_1[0][0])

### Part 3: Changing list items ###
# Now let’s take advantage of list mutability:
# Replace an item in one of your lists with another, using indexing.
animals[1]="snake"
print(animals)

# Append an item to the end of one of your lists.
animals.append("crow")

# Insert a new item between two existing items.
animals.insert(1,"koala")

# Replace the first item of combined with a new item, then print combined. How much changed?
combined_1[0]="sport"
print(combined_1)

### Bonus ###
combined_1[0] = combined_1[1][9]       # 10, the last item of the int list
combined_1[1] = animals[4]             # "cat" (see note below)
combined_1[2] = float[4] * int[6]      # 1.5 * 7 = 10.5

print(combined_1)   # [10, 'cat', 10.5]

#------------------------------------------------------------------------------#
## Exercise 3: Loops ##   Made by Paula

### Part 1: Loops ###
senses = ["hearing", "seeing", "touch", "smell", "taste"]

for sense in senses:
    print(sense)

### Bonus ###
for sense in senses:
    print(f"One of the five human senses is {sense}.")

### Part 2: Counter variables in for loops ###
sense_number = 1
for sense in senses:
    print(f"Sense number {sense_number} is {sense}.")
    sense_number += 1

### Part 3: For loops by list indexing ###
numeric_order = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eight", "ninth", "tenth"]
len_order = len(numeric_order)
print(len_order)
order_range = range(len_order)
print(order_range)
for index in order_range:
    print(f"{index + 1}: {numeric_order[index]}")

### Part 4: While loops ###
counter = 0
while counter < 30:
    print(f"My age is {counter}, not yet 30.")
    counter += 2


#------------------------------------------------------------------------------#
## Exercise 4: Functions and modules ##   Made by Rebecca

### Part 1: Write your own simple function ###
def first_function():
    print("This is my first function!")

first_function()                               # Calling the function

### Part 2: Inputs and relational operators ###
def second_function(name):
    if name == "Anna":
        print(f"{name} may be your teacher")
    else:
        print(f"{name} is not your teacher")

second_function("Rebecca")                     # Calling the function with my own name. Prints my else statement
second_function("Anna")                        # Calling the function with "Anna". Prints my if statement

### Part 3: Outputs & relational/logical operators ###
# Defining function
def third_function(name):
    if name == "Anna":
        print(f"{name} may be your teacher")
        teacher = True
    else:
        print(f"{name} is not your teacher")
        teacher = False
    return teacher

teacher_anna = third_function("Anna")          # Storing output in new variable
print(teacher_anna)                            # Returns "True" and no I wouldn't be able to get it without return, because teacher is local and unreachable inside the function definition

### Part 4: Store your function in a module ###
import my_module

module = my_module.third_function("Anna")
print(module)                                  # It works

### Part 5: Get creative ###
import word_length

word_length.word_lengths("If you're reading this, then that means my code works! YAY!")