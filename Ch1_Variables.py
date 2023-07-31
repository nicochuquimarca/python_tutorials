# Chapter 2: Variables and simple data types
mess = "Hello Python world!" # Text as variable
print(mess)                  # Print variable

# Changing the variable assignation
mess = "Hello Python Crash Course world!" # New text as variable
print(mess)                               # Test

# Explore data types
  # Strings
s1 = "This is a string"
s2 = 'This is also a string'

print(s1.title()) # stringobject.title() puts the first letter of each word in uppercase
                  # title() is method, which is an action that Python can perform on a piece of data
print(s2.upper()) # stringobject.upper() puts all letters in uppercase
print(s2.lower()) # stringobject.lower() puts all letters in lowercase

# String concatenation
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name # Concatenation
print(full_name.title()) # Prints the full name with the first letter of each word in uppercase

# Create a new personalized message
nombre = "Nicolás"
apellido = "Chuquimarca"
nombre_completo = nombre + " " + apellido
nombre_completo


