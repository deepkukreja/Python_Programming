'''
message = 'Bobby\'s World'
print(message)
'''


"""
message = "Bobby's World"
print(message)
"""

'''
#For multi line comments we use
message = """Bobby's world was a good character in 1990's"""
print(message)
'''

"""
message = 'Hello World'
print(len(message)) #To find out the length of the string
print(message[0])  # Prints the character at index 0
print(message[0:5]) # Prints characters from index 0 to 4 (substring → 'Hello')
print(message[:5])  # Prints characters from the start up to index 4 (same as above → 'Hello')
print(message[6:])  # Prints characters from index 6 till the end
"""

'''
message = "Hello World"
print(message.lower())     #To convert the message into lower case
print(message.upper())     #To convert the message into upper case
print(message.count("Hello"))
print(message.count("l"))
print(message.count('World'))
print (message.find("World"))
print(message.find('Universe'))
'''


'''
message = "Hello World"
new_message= message.replace('Hello', 'Namaste')
message = message.replace('Hello', 'Namaste')
print(new_message)
print(message)
'''

'''
#below are the different ways of writing and printing a string
greeting = ('Hello')
name = ('Deep')
message = greeting + name
message = greeting + ', ' + name + '. Welcome!'
message = ' {} {}. Welcome!'.format(greeting, name) 
message = f'{greeting}, {name}, Welcome!'                 #fstring
print(message)
'''

'''
greeting = 'Hello'
name = 'Deep'
print(dir(name)) # dir(variable) returns a list of all attributes and methods that belong to the given variable/object. It helps you explore what operations you can perform on it.
print(help(str)) # help(str) displays the built-in documentation for the string (str) class. It explains what strings are and lists all available string methods with usage details.
help(str.lower)
'''