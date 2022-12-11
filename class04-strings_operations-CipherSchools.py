# create a string using double quotes
string1 = "Python programming"

# create a string using single quotes
string1 = 'Python programming'


# create string type variables

name = "Python"
print(name)

message = "I love Python."
print(message)



greet = 'hello'

# access 1st index element
print(greet[1]) # "e"



greet = 'hello'

# access 4th last element
print(greet[-4]) # "e"



greet = 'Hello'

# access character from 1st index to 3rd index
print(greet[1:4])  # "ell"




message = 'Hola Amigos'
message[0] = 'H'
print(message)




message = 'Hola Amigos'

# assign new string to message variable
message = 'Hello Friends'

print(message); # prints "Hello Friends"





# multiline string 
message = """
Never gonna give you up
Never gonna let you down
"""

print(message)









str1 = "Hello, world!"
str2 = "I love Python."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)

# compare str1 and str3
print(str1 == str3)





greet = "Hello, "
name = "Jack"

# using + operator
result = greet + name
print(result)

# Output: Hello, Jack





greet = 'Hello'

# iterating through greet string
for letter in greet:
    print(letter)
    
    
    
    
    
greet = 'Hello'

# count length of greet string
print(len(greet))

# Output: 5








print('a' in 'program') # True
print('at' not in 'battle') # False




example = "He said, "What's there?""

print(example) # throws error






# escape double quotes
example = "He said, \"What's there?\""

# escape single quotes
example = 'He said, "What\'s there?"'

print(example)

# Output: He said, "What's there?"






name = 'Cathy'
country = 'UK'

print(f'{name} is from {country}')




 