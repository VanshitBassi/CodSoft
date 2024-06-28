import random
print("Gnerate the Passward by using the Random Characters: ")
# Upper_cas and Lower_case  strings has been taken for Genrating password.
lower_case = "hfjdksinrpostyu"
upper_case = "HFJDKSINRPOSTYU"
# The password will be generating when both strings are come together with in a string. 
string = lower_case + upper_case 
# Length of a Random Caracters are required for generating the password.
len = 8
# random .sample is use to return the selected elements from a sequence of string.
# join takes the list of string as an Argument that will returns the new string for genterating the password.
password = "".join(random .sample(string, len))
print("password:", password)
password
