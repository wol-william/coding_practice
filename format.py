# Task 1: Changing text to uppercase
# Task 2: changing text into lowercase
# Task 3: changing text into title case
# Task 4: change text into capitalize case

# Task 5:Check wether the text is uppercase or lowercase
# Task 6: Slicing
# Task 7: Replace

#Task 1
# Step 1: Create a variable to hold the text
# Step 2: Change the content of the text variable and store in a new variable
# Step 2: Print the changed text

text = "Coding is Fun"
changed_text = text.upper()
print(changed_text)

#Task 2
# Step 1: Create a variable to hold the text
# Step 2: Change the content of the text variable and store in a new variable
# Step 2: Print the changed text

text = "Coding is Fun"
changed_text = text.lower()
print(changed_text)

#Task 3
# Step 1: Create a variable to hold the text
# Step 2: Change the content of the text variable and store in a new variable
# Step 2: Print the changed text

text = "coding is fun"
changed_text = text.title()
print(changed_text)

#Task 4
# Step 1: Create a variable to hold the text
# Step 2: Change the content of the text variable and store in a new variable
# Step 2: Print the changed text

text = "coding is Fun"
changed_text = text.capitalize()
print(changed_text)

#Task 5
# Step 1: Create a variable to hold the text
# Step 2: Check the content of the text variable and store the result in a new variable
# Step 2: Print the changed text

text = "CODING IS FUN"
checked_text = text.islower()
print(checked_text)

#Task 6
# Step 1: Create a variable to hold the text
# Step 2: slice the content of the text variable and store the result in a new variable
text = "CODING IS FUN"
sliced_text = text[1:]
print(sliced_text)

#Task 7
# Step 1: Create a variable to hold the text
# Step 2: Replace the content of the text variable and store the result in a new variable
# Step 3: Print the replace text
text = "Coding is Fun"
replaced = text.replace('fun','hard')
print(replaced)

#recap
text = "CODING IS FUN"
print(len(text))